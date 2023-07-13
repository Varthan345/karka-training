print("TWO QUESTIONS")
print("Think of an object,and i'll try to guess it.")

q1=input("question 1) it is a animal,vegetable,or mineral?\n>")

q2=input("question 2) it is bigger than a bread :")

if q1=="animal" and q2=="yes":
    print("my guess is that you are thinking of a moose.\ni would ask you if its right.but i dont actually care")
elif q1=="animal" and q2=="no":
    print("my guess is that you are thinking of a squirrel.\ni would ask you if its right.but i dont actually care")
elif q1=="vegetable" and q2=="yes":
    print("my guess is that you are thinking of a watermelon.\ni would ask you if its right.but i dont actually care")
elif q1=="vegetable" and q2=="no":
    print("my guess is that you are thinking of a carrot.\ni would ask you if its right.but i dont actually care")
elif q1=='mineral' and q2=="yes":
    print("my guess is that you are thinking of a camaro.\ni would ask you if its right.but i dont actually care")
elif q1=='mineral' and q2=='no':
    print("my guess is that you are thinking of a paper clip.\ni would ask you if its right.but i dont actually care")
else:
    print("you are not think of the things i have mentioned")    

