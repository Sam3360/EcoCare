patients = [
    {"name": "Aarav", "age": 14, "heart_rate": 82},
    {"name": "Riya", "age": 15, "heart_rate": 110},
    {"name": "Kabir", "age": 14, "heart_rate": 76},
    {"name": "Anaya", "age": 15, "heart_rate": 125}
]

for patient in patients:
    if patient["heart_rate"] > 100:
        print(patient["name"], patient["heart_rate"])


        