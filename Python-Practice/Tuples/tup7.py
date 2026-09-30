students = (
    ("Ravi", 85),
    ("Kiran", 92),
    ("Arjun", 78)
)
highest = students[0]
for student in students:
    if student[1] > highest[1]:
        highest = student
print(highest)
    