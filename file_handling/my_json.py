import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "stuff\\output.json") 

Employees = [
    {"name": "Alex", "position": "Software Engineer"},
    {"name": "Bob", "position": "Data Scientist"},
    {"name": "Charlie", "position": "Product Manager"}
]
with open(file_path, "w") as file:
    json.dump(Employees, file, indent=4) # indent for better readability, it adds newlines and spaces to make the JSON more human-readable
    print(f"Data written to '{file_path}' successfully.")

    