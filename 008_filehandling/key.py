import json

content = '{"name": "Sajina", "age": 20, "city": "Pokhara"}'

content_dict = json.loads(content)
content_with_key_value = content_dict.items()
print(content_with_key_value)

for key, value in content_with_key_value:
    print(key, value)
    print(type(key))

a = float(input("first num: "))
b = float(input("first num: "))

sum = a + b
print(f"Sum: {sum}")

product = a * b
print(f"Product: {product}")