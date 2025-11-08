from flask import Flask, request, jsonify, render_template
import json
import re

app = Flask(__name__)

# Load products
with open("products.json", "r") as f:
    PRODUCTS = json.load(f)

STOPWORDS = {"i", "want", "a", "an", "the", "and", "new", "please", "show", "me", "find"}

# Categories available
CATEGORIES = {"phone", "laptop", "headphones", "tablet", "smartwatch", "camera"}

def extract_max_price(user_input):
    match = re.search(r'under \$?(\d+)', user_input.lower())
    return int(match.group(1)) if match else None

def extract_categories(user_input):
    return [cat for cat in CATEGORIES if cat in user_input.lower()]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_input = data.get("input", "").strip().lower()

    if not user_input:
        return jsonify({"recommendations": []})

    # Extract filters
    max_price = extract_max_price(user_input)
    categories = extract_categories(user_input)
    keywords = [word for word in user_input.split() if word not in STOPWORDS]

    recommendations = []
    for p in PRODUCTS:
        if categories and p['category'] not in categories:
            continue
        if max_price and p['price'] > max_price:
            continue
        if keywords and not any(k in p['name'].lower() for k in keywords) and p['category'] not in categories:
            continue
        # Avoid duplicates
        if p not in recommendations:
            recommendations.append(p)

    return jsonify({"recommendations": recommendations})
    

if __name__ == "__main__":
    app.run(debug=True)
