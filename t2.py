count = 0
patients = [
    {"name": "Aarav", "age": 14, "temperature": 36.8},
    {"name": "Riya", "age": 15, "temperature": 38.9},
    {"name": "Kabir", "age": 14, "temperature": 37.2},
    {"name": "Anaya", "age": 15, "temperature": 39.1},
    {"name": "Vihaan", "age": 14, "temperature": 36.5}
]

for patient in patients:
    if patient["temperature"] > 38:
        count+=1

print(count)