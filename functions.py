""" FUNCTIONS
    (1) DEFINE vs CALL
    (2) Paremetr vs Argument
    (3) Keyword & Default arguments
    (4) Scope
"""
print("============== DEFINE (parameter) vs CALL (argument) ===============")
# Function - reusable block of code!
# Instead of block {} in JAVA, JS, Python uses indentation!


# DEFINE - build
def greet(name):
    print(f"Howdo you do? {name}")


def greeting(b):
    print("Greeting is executed")
    return f"Hi {b}"


# CALL - execute
result_1 = greet("Murodil")
print("result1:", result_1)
result_2 = greeting("Justin")
print("result2:", result_2)

print("============== Keyword & Default arguments ===============")

# Define


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name} you are {age} years old!"


result3 = give_greet(name="Marcus", age=32)
print("result3:", result3)

result4 = give_greet(name="John")
print("result4:", result4)


print("============== Scope ===============")


def calculate(a, b):
    c = a * b
    print(f"The c value {c}")


calculate(5, 50)
