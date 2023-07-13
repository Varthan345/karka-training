def triangle():
    l1=int(input("enter the length1 of triangle:"))
    l2=int(input("enter the length2 of triangle:"))
    l3=int(input("enter the length3 of triangle:"))
    s=l1+l2+l3/2
    area=(s*(s-l1)*(s-l2)*(s-l3)**0.5)
    return "area of triangle is.",area

def square():
    a=int(input("enter the side of a square in meter:"))
    return "area of square is:",a**2

def rectangle():
    l=int(input("enter the length of a rectangle:"))
    b=int(input("enter the length  of a rectangle:"))
    area=l*b
    return 'area of a rectangle=',area


def circle():
    radius=int(input("enter the radiys of circle:"))
    return "Area of circle is",3.14*radius**2

def trapezium():
    b1=int(input("enter the base one of a trapezium:"))
    b2=int(input("enter the second base of trapezium:"))
    h=int(input("enter the height of trapezium:"))
    area=b1+b2/2*h
    return area    


a=int(input("enter a function number:"))
if a==1:
    print(triangle())
elif a==2:
    print(rectangle())
elif a==3:
    print(circle())
elif a==4:
    print(trapezium())