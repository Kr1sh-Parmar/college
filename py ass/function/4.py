#4.	Write a program that defines a function sum_avg() to accept marks of variable subjects and calculates total and average. It should return  directly both values.

def sum_avg(*args):
    return sum(args),sum(args)/len(args)
print(sum_avg(10,20,30,40,50))
print(sum_avg(10,20,30,40,50,60,70,80,90,100))
