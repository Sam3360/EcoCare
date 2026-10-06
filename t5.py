n = ""
h = 0
patients = [
    {"name": "Aarav", "heart_rate": 82},
    {"name": "Riya", "heart_rate": 110},
    {"name": "Kabir", "heart_rate": 76},
    {"name": "Anaya", "heart_rate": 125},
    {"name": "Vihaan", "heart_rate": 95}
]

for patient in patients:
    if patient["heart_rate"]>h:
        h = patient["heart_rate"]
        n = patient["name"]




print(f"{n} has the highest heart rate: {h}")
