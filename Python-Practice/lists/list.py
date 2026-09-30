
numbers = [10, 25, 3, 45, 12]
max = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
print(f"Highest number is {max}")
print("========================")

even = 0
odd = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even += 1
    else:
        odd +=1
print(f"Even :- {even}\nOdd :- {odd}")
print("=============================")

numbers = [1,2,2,3,4,4,5,5]
print(f"Original numbers:- {numbers}")
num = set(numbers)
print(f"After Remove duplicates :- {num}")
print("=============================")

numbers = [10, 25, 3, 45, 12]

high = numbers[0]
s_high = 0
for i in range(len(numbers)):
    if numbers[i] > high:
        high = numbers[i]
for i in range(len(numbers)):
    if numbers[i] > s_high and numbers[i] < high:
        s_high = numbers[i]
print(f"2nd highest :- {s_high}")
print("=============================")

numbers = [-5, 10, -2, 8, -9, 7]

p = []
n = []

for i in range(len(numbers)):
    if numbers[i] > 0:
        p.append(numbers[i])
    else:
        n.append(numbers[i])
print("=============================")
print(f"Positive :- {p}")
print(f"Negative :- {n}")

print("=============================")

list = [1,2,3,4,5]

for i in range(len(list)):
     list[i] = list[i+2]
print(list)