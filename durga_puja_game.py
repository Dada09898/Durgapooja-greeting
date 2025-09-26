import random
import time

# Asuras = Bugs in code
asuras = ["Segmentation Fault", "Null Pointer", "Infinite Loop", "Syntax Error", "Memory Leak"]
# Maa Durga's Weapons
weapons = ["Trishul", "Chakra", "Bow & Arrow", "Sword", "Lotus"]

print("🕉️ Welcome to Durga Puja Coding Battle 🕉️")
print("🚩 Maa Durga is here to destroy the Asuras (bugs)!\n")

while asuras:
    bug = random.choice(asuras)
    weapon = random.choice(weapons)
    input(f"⚡ Press Enter to attack {bug} with {weapon}... ")
    print(f"✅ Maa Durga destroyed {bug} using {weapon}!\n")
    asuras.remove(bug)
    time.sleep(1)

print("🎉 All Asuras (bugs) are gone! Happy Durga Puja! 🔱")
