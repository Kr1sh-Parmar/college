#3.	Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.

d1={
    "dept1":{1:1000,2:2000,3:3000},
    "dept2":{4:4000,5:5000,6:6000},
    "dept3":{7:7000,8:8000,9:9000}
}
for i in d1:
    print("Department:",i)
    print("Minimum salary:",min(d1[i].values()))
    print("Maximum salary:",max(d1[i].values()))
    print()

    