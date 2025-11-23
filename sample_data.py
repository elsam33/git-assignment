#sample_project.py

sample_data = [
    {"id": 1, "name": "A"},
    {"id": 2, "name": "B"},
    {"id": 3, "name": "C"},
]

for row in sample_data:
    print("ID: " + str(row['id']) + ", Name: " + row['name'])

