
import time
import random

name = input("Enter your bestie's name: ")

hearts = ["💗", "💕", "💖", "💝", "❤️"]

print("\n" + "✨" * 20)
time.sleep(1)

print("\n🎂 HAPPY BIRTHDAY", name.upper(), "🎂")
time.sleep(1)

print("\n💐 Dear Bestie 💐")
time.sleep(1)

messages = [
    "You are not just my best friend, you are my happiness! 💕",
    "Thank you for making my life more beautiful! 🌸",
    "May all your dreams come true! ✨",
    "Our friendship is forever and ever! 🫂",
    "Keep smiling and shining always! 🌟"
]

for message in messages:
    print("\n" + random.choice(hearts), message)
    time.sleep(1)

print("\n🎁 Sending you unlimited love and happiness!")
print("🥳 Have an amazing birthday, Bestie!")
print("\n" + "💖" * 20)
print("LOVE YOU FOREVER BESTIE! 🫂")
