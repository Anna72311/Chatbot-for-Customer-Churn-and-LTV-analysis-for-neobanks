from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from responses import get_response, get_topics
import os

app = Flask(__name__)
CORS(app)

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')

@app.route('/')
def index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    lang = data.get("lang", "en")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    response = get_response(user_message, lang)
    return jsonify(response)

@app.route("/api/topics", methods=["GET"])
def topics():
    lang = request.args.get("lang", "en")
    return jsonify({"topics": get_topics(lang)})

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
