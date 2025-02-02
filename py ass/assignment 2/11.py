def q11():
    x1=int(input("enter x1"))
    y1=int(input("enter y1"))
    x2=int(input("enter x2"))
    y2=int(input("enter y2"))
    x3=int(input("enter x3"))
    y3=int(input("enter y3"))
    if (y2-y1)/(x2-x1)==(y3-y2)/(x3-x2):
        print("collinear")
    else:
        print("not collinear")
