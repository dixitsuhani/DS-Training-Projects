# Accept a csv file and convert it into a list of dictionaries.

import csv
with open(r"C:\Users\Student\Downloads\sample_students.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)