# 1

print("=========================================================")
numbers = [1,2,2,3,4,4,5]
num = set(numbers)
print(num)
# 2

print("=========================================================")
a = {1,2,3,4}
b = {3,4,5,6}
c =a.intersection(b)
print(c)

#3 

print("=========================================================")
numbers = {1,2,2,3,4,4,5}

sets = {}
unique_words = 0
for num in numbers:
    if num in sets:
        sets[num] +=1
    else:
        sets[num] = 1
        unique_words+=1
        
print(f"Unique words are :- {unique_words}")
        

print("=========================================================")
python_students = {"Ravi", "Kiran", "Arjun", "Rahul"}
java_students = {"Kiran", "Rahul", "Suresh"}

s_b = python_students.intersection(java_students)
print(f"Studying in both python and java are :- {s_b}")


print("=========================================================")
python_students = {"Ravi", "Kiran", "Arjun", "Rahul"}
java_students = {"Kiran", "Rahul", "Suresh"}

only_pyth = python_students.difference(java_students)
print(f"ONLY PYTHON STUDENTS ARE :- {only_pyth}")

6

print("=========================================================")
a = {1,2}
b = {1,2,3,4,5}

c = a.issubset(b)
print(c)

7

print("=========================================================")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

c = set(list1).symmetric_difference(set(list2))
print(c)
8 

print("=========================================================")
list = [1,2,3,2,4,5,1,6,3]

orgi_list = []
duplicate = []

for i in list:
    if i in orgi_list:
        duplicate.append(i)
    else:
        orgi_list.append(i)
print(duplicate)


print("=========================================================")
a = {1,2,5,7}
b = {1,2,3,4,5}

c = a.symmetric_difference(b)
print(c)

print("=========================================================")
all_students  = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
present_students = {5,7,2,1,3,8,11,15,17,20}

print(f"present Students are :- {all_students.intersection(present_students)}")
print(f"Absent students are :-{all_students.symmetric_difference(present_students)}")
total = 0
for i in range(len(all_students)):
    total += 1
total_p = 0
for i in range(len(present_students)):
    total_p+= 1
print(f"total students are :- {total}")
print(f"attendance percentage is  :- {(total_p/total)*100}")

print("=========================================================")