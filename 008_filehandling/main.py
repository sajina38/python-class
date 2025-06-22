# file = open ("employees.txt")
# content = file.read()
# print (content)

# file.seek(0)
# another_content = file.read()
# print (another_content)
# file.close

import json

file_path = "extensions.json"
with open(file_path, "r") as file:

    text_content = file.read()
    content_dictionary = json.loads(text_content)
    print(content_dictionary["recommendations"][0])
