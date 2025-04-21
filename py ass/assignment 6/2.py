students = [
    (1, "krish", 20),
    (2, "ronit", 22),
    (3, "tanmay", 21),
    (4, "yug", 23)
]

roll_nos = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)