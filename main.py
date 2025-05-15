from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Setup Google Sheets access
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open your Google Sheet by its name
sheet = client.open("qirat-records").sheet1  # Change this to your actual sheet name

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        sheet.append_row([
            data.get('userId', ''),
            data.get('userName', ''),
            data.get('grade1', ''),
            data.get('grade2', ''),
            data.get('surah', ''),
            data.get('ayah', '')
        ])
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
