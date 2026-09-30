marks = {
    "Ravi": 85,
    "Kiran": 92,
    "Arjun": 78,
    "Rahul": 88
}

highest = 0
student = ''

for mark in marks:
    if marks[mark] > highest:
        highest = marks[mark]
        student = mark
print(student , end = '')
print(highest)
        
    