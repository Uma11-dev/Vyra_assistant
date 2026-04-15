from fastapi import FastAPI
from app.intent import detect_intent
from app.rag import ask_vyra
from pydantic import BaseModel

app = FastAPI()

chat_history = []


class BookingRequest(BaseModel):
        name : str
        email: str
        phone : str
        session_type : str
        question : str
        Date_of_birth : str
        Time_of_birth : str
        Location_of_birth : str
        Current_Location : str
        Availability_date_and_time : str


@app.post("/chat")
def chat(query: str):
    intent = detect_intent(query)

    if intent == "pricing":
        return {"response": 
     """
Prediction — ₹1,200  
Foundational — ₹1,499  
Dharmic — ₹2,499  
Intensive — ₹3,999+  
Synastry — ₹3,000  
Past Life — ₹2,500  

Let me know what you're drawn to 🤍
"""
    }

    elif intent == "services":
        return {"response":"""
Here’s what you can explore at Luna’s Sanctum 🤍

There are two ways to approach your situation:

• Prediction Session (₹1,200)  
Future possibilities based on your current patterns and timing  

• Deep Readings — Karmic Pattern Mapping  
Understanding why things are happening  

This includes:
- Foundational Session (₹1,499) — one situation  
- Dharmic Reading (₹2,499) — life patterns  
- Intensive Insight (₹3,999+) — deep karmic + past life  

Other sessions:
• Synastry (detailed compatibility reading)(₹3,000)
            """}

    elif intent == "booking":
        return {"response": "Booking steps..."}

    else:
        reply, _ = ask_vyra(query, chat_history)
        return {"response": reply}
    
   

@app.post("/book")
def book_session(data: BookingRequest):

    # For now, just print (later store in DB)

    print(data)

    return {
        "message": "Booking request received. You will be contacted within 24 hours."
    }