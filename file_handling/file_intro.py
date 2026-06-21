import os # helps python to interact with the operating system

# file_path = "./stuff/test.txt" #VVI NOTE: relative path is resolved from where  you're running the command from, not relative to where main.py or the script actually is.
# path can be assigned as stuff/test.txt or stuff\\test.txt (for windows) where \\ 1st \ is for escapes so 2nd \ is needed

script_dir = os.path.dirname(os.path.abspath(__file__)) # __file__ holds the current script's path
file_path = os.path.join(script_dir, "stuff\\test.txt")

# print("script dir: ", script_dir)
# print("file path: ", file_path)

if os.path.exists(file_path):
    print(f"{file_path} exists.")
    if os.path.isfile(file_path):
        print(f"{file_path} is a file.")
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory.")
else:
    print(f"{file_path} does not exist.")