class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def __str__(self):
        return f"Employee[empcode={self.empcode}, empname={self.empname}, DOJ={self.doj}, salary={self.salary}]"

# Serialize
def serialize(employee, filename):
    with open(filename, 'w') as f:
        # Store each attribute separated by a delimiter (e.g., | )
        data = f"{employee.empcode}|{employee.empname}|{employee.doj}|{employee.salary}"
        f.write(data)

# Deserialize
def deserialize(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
        empcode, empname, doj, salary = data.split('|')
        return Employee(empcode, empname, doj, float(salary))  # Cast salary to float if needed

# Demo
if __name__ == "__main__":
    # Original employee object
    emp1 = Employee("E123", "Amit Sharma", "2021-07-01", 50000.00)
    
    # Serialize
    serialize(emp1, "employee.txt")
    print("Serialized!")

    # Deserialize
    emp2 = deserialize("employee.txt")
    print("Deserialized!\n", emp2)
