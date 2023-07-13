name=input("what is your name?:")
print("\n")
age=int(input("hi,{} how old are you".format(name)))
if age<16:
    print("you cant drive",name)
    print("you cant vote",name)
    print("you cant rent",name)
elif age>16 and age<18:
    print("you cant vote",name)
    print("you cant rent",name)
elif 18<=age<=25:
    print("you cant rent",name)
else:
    print("you can do anything",name)        