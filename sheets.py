import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Load Google credentials
google_creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])

# Google Sheets API scopes
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Create credentials
creds = Credentials.from_service_account_info(
    google_creds,
    scopes=scopes
)

# Connect to Google Sheets
client = gspread.authorize(creds)

# Open sheet
sheet = client.open("Porus Pipe Inventory").sheet1


# Add message to sheet
def update_sheet(message):
    sheet.append_row([message])

    return "Message Added Successfully"