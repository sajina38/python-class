try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"The result is {result}")

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Number cannot be divided by 0")

finally:
    print("Thankyou for using my website")
