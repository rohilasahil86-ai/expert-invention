from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = Flask(__name__)
CORS(app)

menu = """
SPICE GARDEN RESTAURANT
Location: near Eminent Mall, Hisar
Timing: 10:00 AM - 11:00 PM
Contact: +91 8607118678

VEG ITEMS:
- Paneer Butter Masala - Rs 220 (Bestseller)
- Dal Makhani - Rs 180
- Veg Biryani - Rs 200
- Veg Thali - Rs 250

NON-VEG ITEMS:
- Butter Chicken - Rs 280 (Bestseller)
- Chicken Biryani - Rs 250
- Mutton Curry - Rs 320
- Non-Veg Thali - Rs 350

DRINKS:
- Lassi - Rs 80
- Cold Coffee - Rs 120
- Soft Drinks - Rs 60

COMBOS:
- Butter Chicken + 2 Naan + Drink - Rs 380
- Veg Thali + Drink - Rs 290
"""

system_prompt = f"""Tu Spice Garden Restaurant ka friendly assistant hai.
Menu se suggest kar. Hindi aur English dono chalegi.
Short aur clear jawab do.
Sirf ye emojis use karo: 😊 🍽️ 👍 😋 🙏
Menu: {menu}"""

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    history = data.get('history', [])
    
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_message})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == '_main_':
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
 