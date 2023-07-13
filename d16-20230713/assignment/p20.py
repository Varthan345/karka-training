print("I will add up the numbers you give me!")
total=0
while True:
    number=int(input("number:"))
    total=number+total
    if number==0:
        break
    print("the total so far if",total)

print("total is",total)    