name=input("whats your name?:")
age=int(input("ok,{} how old are you?:".format(name)))
if age<16:
    print("you cant drive",name)
elif age==16 and age<18:
    print("you can drive but not vote",name)
elif 18<=age<=24:
    print("you can vote ,but not rent a car",name)
elif age>25:
    print("you can do anything",name)        