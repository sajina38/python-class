"""
Unique Character Counter (Strings and Loops)
Create a function unique_chars(text) that takes a string and returns the count of 
unique characters (case-sensitive) using a loop. For example, unique_chars("hello")
returns 4 (h, e, l, o are unique). Avoid using sets; use a list to track characters
and string methods like in for checking.
 """


def unique_chars(text):
    unique_chars = []
    for char in text:
        if char not in unique_chars:
            unique_chars.append(char)
    return len(unique_chars)


print(unique_chars("sajina"))
