from datetime import date

date1 = (17, 2, 2025) 
date2 = (25, 12, 2025)


d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])


difference = abs((d2 - d1).days)

print(f"The number of days between {d1} and {d2} is {difference} days.")
