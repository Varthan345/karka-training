input("are you ready for the quiz? ")
print("okay,here it comes!")

print("q1) what is the capital of alaska?\n\t 1)melbourne\n\t 2)anchorage\n\t 3)juneou")
print("\n")
num=0
ans=int(input(">"))
if ans==3:
    num=num+1
    print("That's right")
else:
    print("that's wrong")

print("q2) can you store the value 'cat' in a variable of type 1\n\t 1)yes\n\t 2)no ")
ans=int(input(">"))
if ans==2:
    num=num+1
    print("That's right")
else:
    print("sorry 'cat' is a string")

print("q3)what is the result of 9+6/3?\n\t 1)5\n\t 2)11\n\t 3)15/3")
ans=int(input(">"))
if ans==1:
    num=num+1
    print("That's right")
else:
    print("that's wrong")

print("overall,you get {} out of 3 correct".format(num))