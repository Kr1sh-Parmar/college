

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return (self.day == other.day and
                self.month == other.month and
                self.year == other.year)
    

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"
    

# Example usage
date1 = Date(15, 8, 2023)
date2 = Date(15, 8, 2023)
date3 = Date(16, 8, 2023)

print(date1)  
print(date2)  
print(date3)  


print(date1 == date2) 
print(date1 == date3) 
print(date2 == date3) 
print(date1 == date1)  






