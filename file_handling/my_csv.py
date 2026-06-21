import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "stuff\\output.csv") 

Employees = [ #2D list where each inner list represents a row in the CSV file
    ['Name', 'Age', 'Job'], # header row
    ['Alice', 30, 'Software Engineer'],
    ['Bob', 25, 'Data Scientist'],
    ['Charlie', 35, 'Product Manager']
]
with open(file_path, "w", newline='') as file: # making newline empty cuz .writerows() appends two \n by default
    writer = csv.writer(file)
    writer.writerows(Employees)
    print(f"Data written to csv file at '{file_path}' successfully.")