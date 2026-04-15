def detect_intent(query: str):
    q = query.lower()

    if any(word in q for word in ["price", "cost", "charge"]):
        return "pricing"

    elif any(word in q for word in ["services", "offer"]):
        return "services"

    elif any(word in q for word in ["book", "appointment"]):
        return "booking"

    else:
        return "ai"