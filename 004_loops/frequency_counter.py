line = "my name is sajina gurung, my  house is in pokhara"
words = line.split()

counter_dict = {}

for word in words:

    if word not in counter_dict:
        counter_dict[word] = 1   # assigning value(word) to key (counter_dict)

    else:
        frequency = counter_dict[word]
        counter_dict[word] = frequency + 1


print(counter_dict)
