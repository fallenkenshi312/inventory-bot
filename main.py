from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from sheets import update_sheet

app = FastAPI()

VERIFY_TOKEN = "inventorybot123"

@app.get("/")
def home():
    return {"message": "Inventory Bot Running Successfully"}

@app.get("/webhook")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    return PlainTextResponse("Verification failed", status_code=403)

@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]

        update_sheet(message)

        print("Message received:", message)

    except Exception as e:
        print("Error:", e)

    return {"status": "success"}