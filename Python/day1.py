print("hello")

def add(a,b):
    return a + b

print(add(3,4))

# Print your name and city.
name="ananya"
city="balrampur"
print(name)
print(city)

# User se age lo aur check karo adult hai ya nahi.

age = int(input("Enter your age : "))
if(age < 18):
    print("you are not eligible")
else:
    print("you are  eligible")

# 1 se 10 tak numbers print karo using loop.

for i in range(1,11):
    print(i)

# Function banao jo 2 numbers add kare.

def add(a,b):
    return a+b

print(add(12,1))

#write a program to remove duplicate number

arr= [1,2,4,5,6,7,8,]
newarr = [] 
def removeDuplicate():
    for i in arr:
        if i not in newarr :
            newarr.append(i)
    return newarr



print(removeDuplicate())
   
# Ek program likho jo check kare ki number even hai ya odd.
a = int(input("Enter Number to check even or odd :"))
def Check():
    if  a % 2 == 0 :
        return "even number"
    return "odd numner"

print(Check())

# Question:

# 1 se 50 tak numbers print karo lekin:

# agar number 3 se divisible hai → "Fizz"

# agar number 5 se divisible hai → "Buzz"

# agar 3 aur 5 dono se divisible hai → "FizzBuzz"

# warna number print karo

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Program likho jo:
# even numbers alag list me
# odd numbers alag list me
numbers = [12,5,7,20,33,40]
odd=[]
even=[]
for i in numbers:
    if i % 2 == 0 :
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)

# 🔴 Interview Question 5 (Logic Test)

# Program likho jo 1 se 100 tak numbers print kare lekin:

# 7 aaye to skip karo

# 50 aaye to loop break karo

for i in range(1,100):
    if i == 7 :
        continue
    elif i == 50:
        break
    else:
        print(i)

# List me largest number find karo using loop.

numbers = [10,90,5,20,8,30]
max = 0

for num in numbers:
    if num > max:
        max = num
print(max)

# Program likho jo list me duplicate numbers detect kare.

# Example:

input = [1,2,3,2,4,5,1]
output =[]
newInput = []

for item in input:
    if item not in newInput:
        newInput.append(item)
    else:
        output.append(item)
print(newInput)
print(output)

# List reverse karo without using reverse()

num = [1,2,3,4,5,6,7,8,9,10]

print(num[::-1])  

# Check karo string palindrome hai ya nahi

data = "my name is ananya"
rev = data[::-1]
if data == rev:
     print("true")
else:
    print("false")
#second largest

num = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,6,7,8,989]
max_num = num[0]
second_max = num[0]

for i in num:
    if i > max_num:
        second_max = max_num
        max_num = i
    if i > second_max and i < max_num:
        second_max = i

print(second_max) 