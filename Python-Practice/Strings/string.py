# vowels = 'a','e','i','o','u'

# string = "programming"
# count = 0
# for char in string:
#     if char in vowels:
#         count += 1
# print(count)
# print("=================")

# string = "programming"
# rev_string = ''
# for i in string:
#     rev_string =  i + rev_string  
# print(rev_string)

# string = "ProGram g42ng"

# # Initialize counters
# uppercase = 0
# lowercase = 0
# digits = 0
# spaces = 0

# # Loop through each character
# for char in string:
#     if char.isupper():
#         uppercase += 1
#     elif char.islower():
#         lowercase += 1
#     elif char.isdigit():
#         digits += 1
#     elif char.isspace():
#         spaces += 1

# # Print the final counts
# print(f"Uppercase: {uppercase}")
# print(f"Lowercase: {lowercase}")
# print(f"Digits: {digits}")
# print(f"Spaces: {spaces}")

# str = "mada"
# revstr = ''
# for char in str:
#     revstr = char + revstr
    
# if revstr == str:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# str = "programming"
# n = ''
# for char in str:
#     if char not in n:
#         n = n+ char
# print(n)
    
    
# text = "programming"

# # 1. Track the max frequency and the character
# max_char = ""
# max_count = 0

# # 2. Check the count of each character
# for char in text:
#     count = text.count(char)
#     if count > max_count:
#         max_count = count
#         max_char = char

# print(max_char)  # Output: r

# text = "aabbcdde"

# count = {}

# for char in text:
#     count[char] = count.get(char, 0) + 1

# for char in text:
#     if count[char] == 1:
#         print(char)
#         break

password = "Hello123"

missing = []

if len(password) < 8:
    missing.append("minimum 8 characters")

for char in password:
    if char.upper() not in password:
        missing.append("uppercase letter")

if not any(char.islower() for char in password):
    missing.append("lowercase letter")

if not any(char.isdigit() for char in password):
    missing.append("digit")

if not any(not char.isalnum() for char in password):
    missing.append("special character")

if len(missing) == 0:
    print("Valid Password")
else:
    for requirement in missing:
        print("Missing:", requirement)