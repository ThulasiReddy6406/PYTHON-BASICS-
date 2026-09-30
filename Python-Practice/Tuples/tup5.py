numbers = (1,2,3,2,4,2,5)
max = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
print(f"MAX NUM = {max}")