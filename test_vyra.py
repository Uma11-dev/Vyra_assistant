from app.intent import detect_intent
from app.rag import ask_vyra

chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Vyra: Until next time 🤍")
        break

    intent = detect_intent(user_input)

    if intent == "pricing":
        reply = """
Prediction — ₹1,200  
Foundational — ₹1,499  
Dharmic — ₹2,499  
Intensive — ₹3,999+  
Synastry — ₹3,000  
Past Life — ₹2,500  

Let me know what you're drawn to 🤍
"""

    elif intent == "services":
        reply = """
I offer:

• Prediction Session  
• Karmic Pattern Mapping  
• Synastry  
• Past Life Reading  

I can guide you if you're unsure 🤍
"""

    elif intent == "booking":
        reply = """
To book:

1. Fill form  
2. Pay via UPI: chauhanuma09@okaxis  
3. Send screenshot  
4. Share availability  

Sessions available in call, audio, or PDF 🤍
"""

    else:
        reply, chat_history = ask_vyra(user_input, chat_history)

    print(f"\nVyra: {reply}\n")