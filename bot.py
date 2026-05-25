from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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

messages = [{"role": "system", "content": f"""Tu Spice Garden Restaurant ka friendly assistant hai.
Menu se suggest kar. Hindi/English dono chalegi.
Short aur clear jawab do. Emojis use karo. 😊 🍽️ 👍 😋 🙏
Menu: {menu}"""}]

print("\n" + "="*40)
print("   SPICE GARDEN RESTAURANT BOT")
print("="*40)
print("how," \
" how are you sir/mam " \
"how can i help you today")
print("(write quit and end conversation)")
print("="*40 + "\n")

while True:
    user_input = input("Aap: ").strip()
    if not user_input:
        continue
    if user_input.lower() == 'quit':
        print("Bot: Shukriya! Phir aana!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"\nBot: {reply}\n")
    print("-"*40)