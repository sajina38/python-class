
def longest_word(sentence):
    words = sentence.split()  # ['Sajina', 'Gurung', 'is', 'good']
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest  # If a word is longer, we update the longest.


print(longest_word("Sajina Gurung is good"))
