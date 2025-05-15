from flask import Flask, request, jsonify
from flask_cors import CORS
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Google Sheets setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open your Google Sheet by its name
sheet = client.open("qirat-records").sheet1  # Replace with your actual sheet name

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        # Append data row to Google Sheet
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

if __name__ == '__main__':
    app.run()
