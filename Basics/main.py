# Python basics
# Chapter by Chapter
# Revision before start dsa

"""Chapter 1: Variables & Data Types"""
print("1] Variables & Data Types")

# Variables
name = "Ayanabha"
age = 21
height = 5.8
is_student = True 

print("My name is ",name)
print("I am ",age," years old.")
print("My height ",height," feet/inc.")
print("Yes I am a student and this is ",is_student)

# Type checking
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


"""Chapter 2: Input & Output"""
# print("2] Input & Output")

# # IO operations
# f_name = input("Enter your friend name: ")
# f_age = int(input("Enter your friend age: "))
# f_height = float(input("Enter your friend height: "))

# print("My friend's name is ",f_name,". He is ",f_age," years old and he is ",f_height," feet/inc tall.")

"""Chapter 3: Type Casting"""
print("3] Type Casting")

# Type casting methods 
a = "10"
b = int(a)
c = float(a)

print(b + 5)
print(c + 2.5)


"""Chapter 4: Operators"""
print("4] Operators")

# Arithmetic

a = 10
b = 3

print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Modulas: ",a%b)
print("Exponantial: ",a**b)


# Comparision 
print("a greater than b: ",a>b)
print("a less than b: ",a<b)
print("a eual b: ",a==b)
print("a not equal b:",a!=b)

# Logical
x = True 
y = False

print(x and y)
print(x or y) 
print(not x)
print(not y)


"""Chapter 5: If-Else Condition"""
print("5] If-Else Conditions")

# Applying if else conditions (that's how constraint works)
# valid_age = int(input("Enter your age: "))
# if valid_age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# Applying if else with elif condition
marks = 85
if marks >= 85:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")


"""Chapter 6: Loops"""
print("6] Loops")

# For loop
for i in range(1, 6):
    print("Number: ",i) # Print intigers 

for char in "Python":
    print("Chars: ",char) # Print strings 


# While loop
w = 1
while w<= 10:
    print("Iteration sequence: ",w)
    w += 1


"""Chapter 7:Break & Continue"""
print("7] Break & Continue")

# Using break
for g in range(1, 11):
    if g == 5:
        print("End at 5th iteration")
        break
    print(g)

# Using continue
for gg in range(1, 11):
    if gg == 5:
        print("Skip at 5th iteration")
        continue 
    print(gg) 



# All basics python concepts done... 



