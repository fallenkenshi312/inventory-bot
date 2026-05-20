from fastapi import FastAPI, Request

from classifier import classify_transaction, extract_data

from sheets import update_sheet

app = FastAPI()

@app.post("/webhook")

async def webhook(request: Request):

    data = await request.json()

    try:

        message = data["entry"][0]["changes"][0]["value"]["messages"][0]

        text = message["text"]["body"]

        transaction_type = classify_transaction(text)

        extracted_data = extract_data(text)

        if transaction_type:

            update_sheet(transaction_type, extracted_data)

        return {"status": "success"}

    except Exception as e:

        return {"error": str(e)}