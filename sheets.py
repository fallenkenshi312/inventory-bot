import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Load Google credentials from Render environment variable
google_creds = json.loads(os.environ["GOOGLE_CREDENTIALS"])

# Google Sheets API scopes
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Create credentials object
creds = Credentials.from_service_account_info(
    google_creds,
    scopes=scopes
)

# Connect to Google Sheets
client = gspread.authorize(creds)

# Open your Google Sheet
sheet = client.open("Porus Pipe Inventory").sheet1


# Function to add transaction data
def add_transaction(data):

    row = [
        data["type"],
        data["date"],
        data["party"],
        data["item"],
        data["quantity"],
        data["rate"],
        data["amount"]
    ]

    sheet.append_row(row)

    return "Transaction Added Successfully"