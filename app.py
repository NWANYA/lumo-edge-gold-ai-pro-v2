import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "name": "LUMO EDGE GOLD AI PRO V2",
        "market": "XAUUSD",
        "status": "online",
        "features": [
            "GOLD signal engine",
            "BUY and SELL alerts",
            "Entry, Stop Loss and Take Profit",
            "Risk management"
        ],
        "message": "Service is running. Market data is not connected yet."
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
