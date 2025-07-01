
def is_palindrome():
    sentence = input("Enter a sentence: ")
    reversed_sentence = sentence[::-1]
    if sentence == (reversed_sentence):
        print("The sentence is a palindrome.")
    else:
        print("The sentence is not a palindrome.")


is_palindrome()
