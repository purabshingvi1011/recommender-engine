# 🧠 Content-Based Product Recommender

This is a simple, production-ready content-based recommendation engine built using Python, Flask, TF-IDF, and Redis. It recommends similar products based on their textual descriptions using Natural Language Processing (NLP).

## 🚀 Features

- Recommends similar products based on content (no user history needed)
- Uses TF-IDF vectorization + cosine similarity
- Stores similarity scores in Redis for fast lookup
- Exposes a REST API via Flask
- Deployable to Heroku or locally
- Easy to integrate with a frontend

## 🏗 How It Works

1. Load product descriptions from a CSV file (`products.csv`)
2. Vectorize the descriptions using **TF-IDF** with unigrams, bigrams, and trigrams
3. Compute pairwise **cosine similarity**
4. Store the top similar items for each product in Redis
5. Expose recommendations through a simple API

## 📁 Folder Structure

```
product_recommender/
├── app.py              # Flask API
├── engine.py           # Core TF-IDF recommender logic
├── products.csv        # Sample product dataset
├── requirements.txt    # Dependencies
├── Procfile            # For Heroku deployment
├── runtime.txt         # Python version (Heroku)
└── README.md           # This file
```

## 🔧 Requirements

- Python 3.9+
- Redis server running locally or in the cloud
- pip packages (see `requirements.txt`)

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/purabshingvi1011/recommender-engine.git
cd recommender-engine
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Start Redis locally

```bash
brew install redis        # if not installed
brew services start redis # to start it
```

Or run manually:

```bash
redis-server
```

### 4. Run the Flask app

```bash
python app.py
```

## 📬 API Endpoints

### 🔁 Train the engine

```http
POST /train
```

Loads data from `products.csv`, builds the similarity model, and stores results in Redis.

### 🎯 Get recommendations

```http
GET /recommend/<product_id>?n=<num_results>
```

Example:

```bash
curl http://localhost:5000/recommend/1?n=5
```

## 📊 Sample Products

| ID  | Description                          |
|-----|--------------------------------------|
| 1   | Active classic boxers                |
| 2   | Active sport boxer briefs            |
| 3   | Alpine guide pants                   |
| 4   | Alpine wind jacket                   |
| 5   | Ascensionist jacket                  |

## 🧠 Future Improvements

- Add collaborative filtering
- Build a hybrid recommender
- Add a UI for browsing recommendations
- Store results to a database

## 👋 Author

**Purab Shingvi**  
[GitHub](https://github.com/purabshingvi1011)
