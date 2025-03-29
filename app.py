from flask import Flask, jsonify, request
from engine import ContentEngine

app = Flask(__name__)
app.config['REDIS_URL'] = "redis://localhost:6379/0"

content_engine = ContentEngine(app)

@app.route('/train', methods=['POST'])
def train():
    content_engine.train("products.csv")
    return jsonify({"message": "Training complete!"})

@app.route('/recommend/<item_id>', methods=['GET'])
def recommend(item_id):
    num = int(request.args.get('n', 5))
    results = content_engine.predict(item_id, num)
    return jsonify([
        {"id": rec_id.decode(), "score": float(score)}
        for rec_id, score in results
    ])

if __name__ == '__main__':
    app.run(debug=True)
