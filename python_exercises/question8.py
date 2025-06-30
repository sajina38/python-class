# Get a string from a given string where all occurrences of its
# first char have been changed to '$', except the first char itself

text = "Sajina"
result = ""

for i in range(len(text)):
    if i % 2 == 0:
        result += text[i]

print(result)
