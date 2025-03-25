import os
import json
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

def main():
    # If running locally, load credentials from file; otherwise from env variable.
    if os.path.exists('credentials.json'):
        with open('credentials.json') as f:
            service_account_info = json.load(f)
    else:
        service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_JSON'])

    credentials = Credentials.from_service_account_info(
        service_account_info,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    client = gspread.authorize(credentials)

    # Get the spreadsheet ID either from file or environment
    spreadsheet_id = os.environ.get('SPREADSHEET_ID', 'YOUR_LOCAL_SPREADSHEET_ID')
    if spreadsheet_id == 'YOUR_LOCAL_SPREADSHEET_ID':
        raise Exception("Set your local spreadsheet ID or use environment variable.")

    sheet = client.open_by_key(spreadsheet_id).sheet1

    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([current_time])
    print("Appended current time:", current_time)

if __name__ == "__main__":
    main()
