#1.	Write a program to create a csv file that we can directly open in MS-Excel.simply

def create_csv_file(filename):
    import csv

    # Sample data to write to the CSV file
    data = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"]
    ]

    # Create and write to the CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

create_csv_file('sample_data.csv')