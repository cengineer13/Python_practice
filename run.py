# Dunder (magic) methodlar __builtins__, __init__ - system variablelar hisoblanadi,

message = "PYTHON: Erverything is object!"
print(message)

result = type(message)
print("result:", result)

''' In Python, there are builtins tools:
    (1) TYPES > int, float, str, list, dict
    (2) FUNCTION > print(), len(), type()
    (3) CONSTANTS > True, False, None
'''

print(dir(__builtins__))
