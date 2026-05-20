from fastapi import FastAPI
from sheets import add_transaction

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Inventory Bot Running Successfully"}


@app.post("/add")
def add_data():

    sample_data = {
        "type": "Purchase",
        "date": "2026-05-20",
        "party": "ABC Manufacturer",
        "item": "Porous Pipe",
        "quantity": 100,
        "rate": 50,
        "amount": 5000
    }

    result = add_transaction(sample_data)

    return {
        "status": "success",
        "message": result
    }