#5.	Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.

d1={
    "apple":100,
    "banana":50,
    "mango":150,
    "orange":80
}
d2={
    "apple":2,
    "banana":3,
    "mango":1,
    "orange":4
}
total=0
for i in d1:
    total+=d1[i]*d2[i]

print("Total bill:",total)