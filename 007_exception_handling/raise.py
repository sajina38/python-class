divisor = int(input("Enter a number:"))

divident = 20

if divisor == 0:
    msg = "yesto jpt number nahana na"
    raise Exception(msg)

result = divident / divisor
print("The result is", result)
