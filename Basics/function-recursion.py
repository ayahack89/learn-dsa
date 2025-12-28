# Function Recursion

# What is function recursion?
# -> When a function calling itself like have a dream inside a dream.

# For example:
# function dream():
#        if !wokeup:
#             dream()

# Example 1: Factorial using recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

result = factorial(5)
print(result)


# Example 2: Countdown
def countdown(n):
    if n == 0:
        return # Null value
    else:
        print(n)
        return countdown(n - 1)

count = countdown(10)
print(count)



# Function recursion done... 