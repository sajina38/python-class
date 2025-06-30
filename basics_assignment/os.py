"""
Write a program that uses the os module to list all the files in the current folder 
(use os.listdir()). Print each file name on a new line.
"""
import os

files = os.listdir()
for file in files:
    print(file)

"""
Ask the user to input a file name (like "myfile.txt"). 
Use the os module (specifically os.path.exists())
to check if that file exists in the current folder. Print whether the file exists or not.
"""
user_file = input("Enter a file name: ")

if os.path.exists(user_file):
    print("The file exists!")
else:
    print("The file does not exist.")
