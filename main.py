from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Google Apps Script Web App URL
GOOGLE_SHEETS_URL = "https://script.google.com/macros/s/AKfycbyxpEjkF056_GQZMgDAwFzATUB2F3MJyLpaJ_PYHV7Op0QIoc99Mvgr--7edXHE_9Nb6Q/exec"

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        required_fields = ["userId", "userName", "grade1", "grade2", "surah", "ayah"]

        if not all(field in data for field in required_fields):
            return jsonify({"status": "error", "message": "Missing fields"}), 400

        # Forward data to Google Sheets
        response = requests.post(GOOGLE_SHEETS_URL, json=data, headers={"Content-Type": "application/json"})
        return jsonify({"status": "sent", "google_response": response.text})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Needed for Vercel to detect the app
app = app
