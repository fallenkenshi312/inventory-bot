from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SPREADSHEET_ID = "1ePL6iNZZQt1hkY5QiELfR8p_zMfNX6kLTy2QCckkzJk"

def update_sheet(transaction_type, data):

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    service = build("sheets", "v4", credentials=creds)

    sheet_name = "Purchase" if transaction_type == "Purchase" else "Sale"

    values = [[
        data["date"],
        data["party"],
        "Porous Pipe",
        data["qty"],
        data["rate"],
        data["amount"]
    ]]

    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{sheet_name}!A2",
        valueInputOption="USER_ENTERED",
        body={"values": values}
    ).execute()