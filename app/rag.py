import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()

# Create Claude client
client = Anthropic()

# This function reads your knowledge base file
def load_knowledge_base():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "data", "knowledge_base.txt")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# This is the main function — it sends user question + knowledge to Claude
def ask_vyra(user_message: str, chat_history: list = []):
    
    # Load the knowledge base
    knowledge = load_knowledge_base()
    
    # System prompt — this defines Vyra's personality and rules
    system_prompt = f"""
You are Vyra, an intelligent assistant for Luna's Sanctum — a spiritual services platform.

Your role is to:
- Answer questions about Luna's Sanctum services clearly
- Help users understand which session suits them
- Guide users toward booking when appropriate
- Never provide full readings or detailed personal interpretations

Your tone should be:
- Calm and grounded
- Slightly mystical but clear
- Not dramatic or preachy

Use ONLY the information below to answer. Do not make up services or prices.

--- KNOWLEDGE BASE ---
{knowledge}
--- END OF KNOWLEDGE BASE ---
"""
    
    # Add the new user message to chat history
    chat_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Send everything to Claude
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=system_prompt,
        messages=chat_history
    )
    
    # Extract Claude's reply
    vyra_reply = response.content[0].text
    
    # Add Vyra's reply to chat history
    chat_history.append({
        "role": "assistant",
        "content": vyra_reply
    })
    
    return vyra_reply, chat_history