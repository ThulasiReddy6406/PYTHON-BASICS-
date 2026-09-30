student = {
    "name": "Ravi",
    "age": 20,
    "branch": "CSE"
}

keyy = input("Enter a key :- ")

for key in student:
    if key == keyy:
        print("Found")
        break
        
print("Not Found")