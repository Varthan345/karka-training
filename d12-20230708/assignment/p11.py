weight=int(input("enter your current earth weight:"))
print("\n")
print("i have information for the following planets:\n\t1. venus\t\t2. mars\t\t\t3.jupiter\n\t4. saturn\t\t5. uranus\t\t\t6.neptune")
planet=int(input("which planet are you visitng?:"))
if planet==1:
    your_weight=weight*0.78
    print("your weight would be {} pounds on that planet".format(your_weight))
elif planet==2:
    your_weight=weight*0.39
    print("your weight would be {} pounds on that planet".format(your_weight))    
elif planet==3:
    your_weight=weight*2.65
    print("your weight would be {} pounds on that planet".format(your_weight)) 
elif planet==4:
    your_weight=weight*1.17
    print("your weight would be {} pounds on that planet".format(your_weight)) 
elif planet==5:
    your_weight=weight*1.05
    print("your weight would be {} pounds on that planet".format(your_weight)) 
elif planet==6:
    your_weight=weight*1.23
    print("your weight would be {} pounds on that planet".format(your_weight))
else:
    print("no planets ")     


