
try:
    user_input = 100
    print(user_input / 0)

except ZeroDivisionError as e:
    print()
    print(e)
    print(e.__class__.__name__)
