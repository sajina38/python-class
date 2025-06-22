
# if operator=="+":
#     print (f"The sum of the {first_number} and {second_number} is: {first_number + second_number}" )

# elif operator=="*":
#    print (f"The multiplication of the {first_number} and {second_number} is: {first_number * second_number}" )

# elif operator=="/":
#     print (f"The division of the {first_number} and {second_number} is: {first_number / second_number}" )

# elif operator=="**":
#     print (f"The power of the {first_number} and {second_number} is: {first_number ** second_number}" )

# elif operator=="%":
#     print (f"The modulus of the {first_number} and {second_number} is: {first_number % second_number}" )

# else:
#     print ("Invalid input")


# def calculator(num1, operator, num2):

#     if operator=="+":
#         return num1+num2

#     elif operator=="-":
#         return num1-num2

#     elif operator=="*":
#         return num1*num2

#     elif operator=="/":
#         return num1/num2

#     else:
#         return None

# sum = calculator(1, "+", 2) 

# print (f"The sum is {sum} ")


# #HOMEWORK

# Q1. Age Group Checker

age = int(input("Enter your age: "))

if age < 14:
    print("You're a child")

elif age > 13 and age < 20:
    print("You're a teenager")

elif age > 19 and age < 59:
    print("You're an adult")

else:
    print("You're a senior")



# Q2. Number Operations 

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))

print(f"""The sum of {first_number} and {second_number} is {first_number + second_number},
The difference of {first_number} and {second_number} is {first_number - second_number},
The product of {first_number} and {second_number} is {first_number * second_number},
The modulus of {first_number} and {second_number} is {first_number / second_number}
       """)



# Q3. Odd or Even with a Twist

num=int(input("Enter a number: "))
 
if num%2==0:
    print(f"It is even. Its square: {num**2}")

else:
    print(f"It is odd. Its cube: {num**3}")



# Q4. Sum of N Natural Numbers

total=0
num=int(input("Enter a number: "))

for i in range(1, num + 1):
    total += i

print(f"The sum of first n natural numbers of {num}: {total}")



# Q5. Multiplication Table Generator

num=int(input("Enter a number: "))
i=1
 
while i<=10:
    print (f" {num} X {i}: {num * i}")
    i += 1





# data = [ 
#     {
#      "name" : "Ram Sharma",
#      "hobbies" : ["coding", {
#          'hi': {
#              'hello': [{
#                  'tree': ["root", {
#                      'complex': [True]
#                  }]
#              }]
#          }
#      }]
#     }
# ]



# NOTES

# number lai matra int ma parse garni 
# operator string nai ho

# indexing 0 bata suru huncha

# list ma indexing use garera access garni

# dictionary ma key use garera access garni