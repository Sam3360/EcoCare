patients = [
    {"name": "Aarav", "age": 14, "steps": 8200},
    {"name": "Riya", "age": 15, "steps": 4200},
    {"name": "Kabir", "age": 14, "steps": 10500},
    {"name": "Anaya", "age": 15, "steps": 3100},
    {"name": "Vihaan", "age": 14, "steps": 7600}
]
for patient in patients:
    if patient["steps"]<5000:
        print(patient["name"])
        
