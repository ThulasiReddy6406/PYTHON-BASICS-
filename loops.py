'''
for i in range(1,101):
    print(i)
i = 1
while i <= 100:
    print(i)
    i += 1
    '''
#===============================
'''
i = 100
while i >= 1:
    print(i)
    i -= 1

for i in range(100,0,-1):
    print(i)
    '''
#===============================
'''
n = int(input("Enter the number :- "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

i = 1
n = int(input("Enter the number :- "))
while i<=10:
    print(f"{n} X {i} = {n*i}")
    i = i+1
'''
#===============================
# num = [1,4,9,16,25,36,49,64,81,100]
# for i in range(len(num)):
#     print(num[i])
    
# num = (1,4,9,16,25,36,49,64,81,100,36)
# x = int(input("Enter the number :- "))

# i = 0
# found = False

# while i < len(num):

#     if num[i] == x:
#         print(f"NUMBER {x} FOUND AT INDEX {i}")
#         found = True
#         break

#     i += 1

# if not found:
#     print("NOT FOUND")

# tup = (1,4,9,16,25,36,49,64,81,100,)

# x = int(input("NUMBER :- "))
# i = 0
# idx =0
# found = False
# while i < len(tup):
#     if(x == tup[i]):
#         print(f"Found num {x} at index {idx}")
#         found = True
#     i += 1
#     idx += 1
    
# if not found:
#     print("Not found")

# i = 0
# n = 3
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

i=1
n = 5
fac = 1
# for i in range(1,n+1):
#     fac = fac * i
# print(f"Factorial of {n} = {fac}")

while i < n:
    fac = fac*(i+1)
    i+=1
print(fac)