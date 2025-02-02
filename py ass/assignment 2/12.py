def q12():
    import math
    cx = int(input("enter cx"))
    cy = int(input("enter cy"))
    r = int(input("enter r"))
    px = int(input("enter px"))
    py = int(input("enter py"))
    distance = math.sqrt((cx-px)**2 + (cy-py)**2)
    if distance < r:
        print("inside")
    elif distance == r:
        print("on the circle")
    else:
        print("outside")

