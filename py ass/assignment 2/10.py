def q10():
    length=int(input("enter length"))
    breadth=int(input("enter breadth"))
    area=length*breadth
    perimeter=2*(length+breadth)
    if area>perimeter:
        print("area is greater")

    else:
        print("perimeter is greater")
