#sample_project.py

sample_data = [
    {"id": 1, "name": "A", "score": 95},
    {"id": 2, "name": "B", "score": 88},
    {"id": 3, "name": "C", "score": 92},
]

for row in sample_data:
    print(f"ID: {row['id']}, Name: {row['name']}, Score: {row['score']}")
