
line = "my name is sajina gurung, my pet name is suman"

words = line.split()

key_value = {}

for word in words:
    if word not in key_value:
        key_value[word] = 1

    else:
        frequency = key_value[word]
        key_value[word] = frequency + 1

repeated_words = {}

for word, freq in key_value.items():
    if freq > 2:
        repeated_words[word] = freq

print(repeated_words)