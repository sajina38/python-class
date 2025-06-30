#  Write a Python program to get a string made of the first 2 and last 2 characters
#  of a given string. If the string length is less than 2, return the empty string instead.


def string_both_ends(str):
    if len(str) < 2:
        return ""

    return str[0:2] + str[-2:]


# Call the string_both_ends function with different input strings and print the results.
print(string_both_ends("w3resource"))  # Output: 'w3ce'
print(string_both_ends("w3"))  # Output: 'w3w3'
print(string_both_ends("w"))
