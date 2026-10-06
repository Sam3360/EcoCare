patients = [
    {"name": "Aarav", "temperature": 36.7, "heart_rate": 82},
    {"name": "Riya", "temperature": 38.9, "heart_rate": 110},
    {"name": "Kabir", "temperature": 37.1, "heart_rate": 76},
    {"name": "Anaya", "temperature": 39.2, "heart_rate": 125},
    {"name": "Vihaan", "temperature": 36.5, "heart_rate": 95},
    {"name": "Sara", "temperature": 38.5, "heart_rate": 102}
]
for patient in patients:
    if patient["temperature"]>38 or patient["heart_rate"]>100:
        name = patient["name"]
        print(f"Patient {name} needs attention!!!")
