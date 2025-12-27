"""Chapter 8: Functions Complete Guide"""
print("8] Functions Complete Guide")

# What is a function?
# > A function is a reusable block of code.

# Example....

def greet():
    print("Function execute")

greet()

# Function syntax (Method Structure)
# def function_name(parameters):
#     # function body
#     return value

# def -> keyword
# function_name -> method name
# parameters -> inputs
# return -> outputs (but optional)

# Function without parameters 
def show_message():
    print("Hey guys, whatsupp!")

show_message()

# Function with parameters
def your_name(name):
    print("Your name is ",name)

your_name("Ayanabha")

# Function with return value 
def add(a, b):
    return a + b 

result = add(10, 20)
print("Result: ",result)

# Multiple return values 
def calc(a, b):
    return a + b, a - b, a * b 

sum, sub, mul = calc(10, 5)
print(f"Addition: {sum}\nSubtraction: {sub}\nMultiplication: {mul}\n")


# Default parameters 
def welcome(g_name="Guest"):
    print("Welcome", g_name)

welcome()
welcome("John")

# Keywords Arguments (Name Arguments)
def student(student_name, student_age):
    print(student_name, student_age)

student(student_age=21, student_name="Ayanabha")


# Arbitrary Arguments (args)
# Used when number of arguments is unknown 
def total(*number):
    sum_=0
    for n in number:
        sum_+=n
    return sum_

r = total(1, 2, 3, 4, 5)
print("Result: ",r)

# Arbitrary keywords (kwargs)
def details(**info):
    for key, value in info.items():
        print(key, ":", value)

details(name_="Ayanabha", age_=21, course_="Python")


# Lambda function
# (Anonymous Method)
square = lambda x: x*x 
print(square(5))




# All basic functions done.... 