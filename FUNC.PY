
# def addition(a,b):
#     return a+b

# print(addition(2,3))

# name = input("Enter the name :- ")

# def greet(name):
#     print(f"Hello {name}\nWelcome to python")
# greet(name)

# num = int(input("Enter the NUmber :-  "))

# def cheak_num(num):
#     if num > 0:
#         print("Positive")
#     elif num < 0:
#         print("Negative")
#     else:
#         print("Zero")
# cheak_num(num)

num = int(input("Enter the NUmber :-  "))
def print_table(num):
    for i in range(1,num+1):
        for j in range(1,11):
            print(f"{i} X {j} = {i*j}")
        print("=============")
print_table(num)

    