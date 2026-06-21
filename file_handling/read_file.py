import os
import json
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "stuff\\test.txt") 
# file_path = os.path.join(script_dir, "stuff\\output.json") 
file_path = os.path.join(script_dir, "stuff\\output.csv") 

# for test.txt
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print(f"File '{file_path}' not found.")
# except PermissionError:
#     print(f"Permission denied for file '{file_path}'.")
# except Exception as e:
#     print(f"AN error occured: {e}")

# for reading json files
# try:
#     with open(file_path, "r") as file:
#         content = json.load(file) # for json files, we use json.load() instead of file.read() to parse the JSON content into a Python object (like a list or dict)
#         print(content)
# except FileNotFoundError:
#     print(f"File '{file_path}' not found.")
# except PermissionError:
#     print(f"Permission denied for file '{file_path}'.")
# except Exception as e:
#     print(f"AN error occured: {e}")

# for reading csv files 
try:
    with open(file_path, "r") as file:
        csv_file = csv.reader(file) #note this will just give address of the reader object
        for line in csv_file:
            # print(line)
            print(line[0])
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except PermissionError:
    print(f"Permission denied for file '{file_path}'.")
except Exception as e:
    print(f"AN error occured: {e}")
