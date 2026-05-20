import re

def classify_transaction(text):

    if "sale" in text.lower():
        return "Sale"

    elif "purchase" in text.lower():
        return "Purchase"

    return None

def extract_data(text):

    date = re.search(r"\d{2}/\d{2}/\d{4}", text)

    qty = re.search(r"Qty[: ]+(\d+)", text)

    rate = re.search(r"Rate[: ]+(\d+)", text)

    amount = re.search(r"Total[: ]+(\d+)", text)

    party = re.search(r"Party[: ]+(.+)", text)

    return {

        "date": date.group(0) if date else "",

        "qty": qty.group(1) if qty else "",

        "rate": rate.group(1) if rate else "",

        "amount": amount.group(1) if amount else "",

        "party": party.group(1) if party else ""
    }