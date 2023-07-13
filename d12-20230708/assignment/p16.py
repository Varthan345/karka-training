firstname=input("enter your first name:")
lastname=input("enter your last name:")
name=str(firstname+lastname)
age=int(input("enter your age:"))
gender=input('what is your gender (M or F):')
if gender=="f" and age>=20:
    married=input("Are you married(Y or N)")
    if married=="y":
        print("Then i shall call you Mrs.{}".format(name))
    else:
        print("I will call you Ms.",name)
if gender=="m" and age>=20:
    print("Then i shall call you Mr.",name)
if gender=="m" and age<20:
    print("i will call you",name)    