
import os

# current_dir = os.getcwd()
# print()
# print(f"Current directory: { current_dir}")
# print()

if not os.path.exists('test_folder'):
    os.makedirs('test_folder')
    print("Directory created!")


# if not os.path.exists('test folder'):
#     os.makedirs('test_folder')
#     print("Drirectory created!")