import os
import json
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

def main():
    # Load service account credentials from the secret environment variable
    service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_JSON'])
    credentials = Credentials.from_service_account_info(
        service_account_info,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    client = gspread.authorize(credentials)

    # Get the spreadsheet ID from the environment; raise error if not provided
    spreadsheet_id = os.environ.get('SPREADSHEET_ID')
    if not spreadsheet_id:
        raise Exception("Spreadsheet ID not set. Add it to your GitHub secrets as SPREADSHEET_ID.")

    # Open the spreadsheet (first sheet by default)
    sheet = client.open_by_key(spreadsheet_id).sheet1

    # Get current UTC time (format as needed)
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    # Append the current time as a new row in column A
    sheet.append_row([current_time])
    print("Appended current time:", current_time)

if __name__ == "__main__":
    main()
