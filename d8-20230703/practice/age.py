 #def voting(age):
 #    eligible=age>=18
 #    return eligible

def voting(age):
    if age>=18:
        return "you are eligible for voting"
    else:
        return"you are not eligible"

age=int(input("enter your age :"))
#is_eligible=voting(age)
print(voting(age))