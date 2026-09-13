print("===========number=============")
# in JAVA, variable is a name of storage location!
# in Python, variable is named reference!

count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count:{count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("===========string=============")
# METHODS: upper() lower() title() find() replace() join()

course = "Agentic AI Python FullStack"
result = type(course)
print(f"the type of text: {result}")

result = course.title()
print(f"the title of text: {result}")

result = course.upper()
print(f"the uppercase text: {result}")

result = course.lower()
print(f"the lowercase text: {result}")

result = course.replace("FullStack", "Masterclass")
print(f"the replace method text: {result}")


print("===========Boolen=============")
# functions > type() input() bool() int() str()

y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"The input value is numbers: {result}")

# TRUTHY vs FALSY value
# TRUTHY: True, 100, -100, "MIT"
# FALSY > False

test_falsy = "" or False or None or 0
print("The FALSY:", bool(test_falsy))

test_truthy = "MIT" or 1 or [1, 2, 3]
print("The TRUTHY:", bool(test_truthy))
