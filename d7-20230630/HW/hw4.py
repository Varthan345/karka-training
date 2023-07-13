product1=input("enter the amount of item1=")
product2=input("enter the amount of item2=")
product3=input("enter the amount of item3=")
product4=input("enter the amount of item4=")
product1=int(product1)
product2=int(product2)
product3=int(product3)
product4=int(product4)
total=product1+product2+product3+product4
if(500<=total<=1000):
    print("you have owned a silver token")
elif(total>1000):
    print("you have owned a golden token")    
else:
    print("thank you for coming")
