

# AI Product Recommendation System

## Project Overview

The **AI Product Recommendation System** is a web application that allows users to get personalized product recommendations based on their preferences. The system strictly filters products by **category** and **price** and provides relevant recommendations in a clean, text-based layout.

This project demonstrates:

* Frontend integration with Flask backend
* AI-style filtering of user input (keywords, categories, price limits)
* Clean and professional UI for displaying product recommendations
* A scalable design for expanding product datasets

---

## Features

1. **Category Filtering:** Returns products strictly matching the categories mentioned by the user (e.g., phones, headphones, smartwatches).
2. **Price Filtering:** Filters products based on price constraints such as "under $500".
3. **Keyword Filtering:** Matches product names with relevant keywords from the user query.
4. **No Duplicates:** Ensures unique recommendations for each query.
5. **Professional Layout:** Displays products in a clean, text-only card-style format.
6. **Expandable Dataset:** Products are stored in a JSON file and can be expanded easily.

---

## Folder Structure

```
product_recommendation_system/
│
├── app.py                 # Flask backend server
├── .env                   # Environment file for configuration (optional)
├── products.json          # Product dataset
├── templates/             
│   └── index.html         # Frontend UI
└── venv/                  # Python virtual environment
```

---

## Requirements

* Python 3.8 or higher
* Flask
* Flask-CORS

Install dependencies using:

```bash
pip install flask flask-cors
```

---

## Getting Started

1. **Clone the repository:**

```bash
git clone Shreyabagal
cd product_recommendation_system
```

2. **Activate virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Flask server:**

```bash
python app.py
```

5. **Open the frontend:**

Visit `http://127.0.0.1:5000` in your browser.

---

## How to Use

1. Enter your product preference in the search box. Examples:

   * `"phone under $600"`
   * `"headphones and smartwatches under $300"`

2. Click **Get Recommendations**.

3. The system will display a list of products matching your query, with their names and prices.

---

## Dataset

* Products are stored in `products.json`
* Each product has:

  * `name` – Name of the product
  * `category` – Product category (e.g., phone, laptop, headphones)
  * `price` – Price in USD

You can expand the dataset by adding more products in JSON format.

---


## Author

* Shreya Ramchandra Bagal

---
