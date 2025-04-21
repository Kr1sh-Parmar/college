#2.	Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.

import pandas as pd

def excel_to_dict(file_path):
    df = pd.read_excel(file_path)
    student_dict = {}

    for _, row in df.iterrows():
        total = row[["Math", "Science", "English"]].sum()
        student_dict[row["RollNo"]] = {
            "Name": row["Name"],
            "Marks": row[2:5].tolist(),
            "Total": total
        }

    print(student_dict)