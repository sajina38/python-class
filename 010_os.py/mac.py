import platform
import os

print(os.getcwd())

system = platform.system()

if system == "Linux":
    print("linux user")

elif system == "Darwin":
    print("mac user")

elif system == "Windows":
    print("windows user")
