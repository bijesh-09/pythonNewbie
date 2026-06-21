import os

txt_data = "My fav dish: I like momo and jhol"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "stuff\\output.txt") 

# with open(file=file_path, mode ="w") as myfile: # we can give keyword args as well
# with wraps around the code block and auto closes the file after the code block is executed, even if an exception occurs. This is a good practice to avoid resource leaks.
# but explicitly writing close() is a good practice

# with open(file_path,"w") as myfile:
#     myfile.write(txt_data)
#     print(f"Data written to {file_path} successfully.")

try:
    with open(file_path,"x") as myfile:
        myfile.write(txt_data)
        print(f"File at '{file_path}' created successfully via 'x' mode.")
except FileExistsError:
    print(f"File at '{file_path}' already exists. Cannot create a new file with 'x' mode.")
except Exception as e:
    print(f"An error occurred: {e}")

Employees = [
    {"name": "Alice", "position": "Software Engineer"},
    {"name": "Bob", "position": "Data Scientist"},
    {"name": "Charlie", "position": "Product Manager"}
]

with open(file_path,"a") as myfile:
        for emp in Employees:
            emp_info = f"{emp['name']}, position: {emp['position']}"
            myfile.write('\n' + emp_info)
        print(f"Data appended to '{file_path}' successfully.")