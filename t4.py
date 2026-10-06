patients = [
    {"name": "Aarav", "heart_rate": 82},
    {"name": "Riya", "heart_rate": 110},
    {"name": "Kabir", "heart_rate": 76},
    {"name": "Anaya", "heart_rate": 125}
]
s = 0

avg = 0

for patient in patients:
    a = patient["heart_rate"]
    s+=a


avg = s / len(patients)
print(avg)
