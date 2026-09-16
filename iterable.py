print('============= Iterable objects & Range ============')
# Iterable objects > string, dict, tuple, list, range, map, filter

text = "MIT"
for letter in text:
    print(f'the letter:{letter}')

range_obj = range(3)
print('range_obj:', range_obj)

for el in range_obj:
    print(f'the element:{el}')


print('============= DICTIONARY ============')
# Dictionary is JSON object!

# 1-method of creating dict
person = {'name': "Justin", "age": 25, "single": True}
# 2-method of creating dict
person_obj = dict(name="Justin", age=25, single=True)
print(f"the person object: {person}")
print(f"the person object: {person_obj}")

# method: get()
# name = person_obj['name']
name = person_obj.get('name')
hobby = person_obj.get('hobby')
print("Hobby:", hobby)  # Key mavjud bolmasa None qaytaradi
balance = person_obj.get("balance", 0)  # Key mavjud bolmasa default qaytarsin
print(f"the name:{name}, hobby: {hobby} and balance:{balance}")

del person_obj['single']
for key, val in person_obj.items():
    print(f"the key:{key, val}")
