import json

content = '{"name": "Sajina", "age": 20, "city": "Pokhara"}'

content_dict = json.loads(content)
content_with_key_value = content_dict.items()
print(content_with_key_value)

for key, value in content_with_key_value:
    print(key, value)
    print(type(key))
