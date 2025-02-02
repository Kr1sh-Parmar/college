def q14():
    sub1=int(input("enter sub1"))
    sub2=int(input("enter sub2"))
    sub3=int(input("enter sub3"))
    total=sub1+sub2+sub3
    avg=total/3
    print("total",total)
    print ("avg",avg)
    if sub1<39 or sub2<39 or sub3<39:
        print("tum fail ho gaye")



    if sub1>=80:
        print("o")
    elif sub1>=70:
        print("a+")
    elif sub1>=60:
        print("A")
    elif sub1>=50:
        print("B+")
    elif sub1>=40:
        print("B")
    else:   
        print("F")

    if sub2>=80:
        print("o")
    elif sub2>=70:
        print("a+")
    elif sub2>=60:
        print("A")
    elif sub2>=50:
        print("B+")
    elif sub2>=40:
        print("B")
    else:
        print("F")

    if sub3>=80:
        print("o")
    elif sub3>=70:
        print("a+")
    elif sub3>=60:
        print("A")
    elif sub3>=50:
        print("B+")
    elif sub3>=40:
        print("B")
    else:  
        print("F")