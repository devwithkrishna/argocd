from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)

# Set your image version here
IMAGE_VERSION = "v2"

@app.route("/health")
def health():
    return jsonify(
        status="OK",
        timestamp=datetime.utcnow().isoformat() + "Z"
    ), 200

@app.route("/version")
def version():
    return jsonify(version=IMAGE_VERSION), 200


@app.route("/greeting")
def greeting():
    name = request.args.get("name", "stranger")
    return jsonify(message=f"Nice to meet you {name}"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
