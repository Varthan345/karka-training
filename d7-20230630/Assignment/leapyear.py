year=input("enter the year:")
year=int(year)
if(year%4==0 and year%100!=0 )or year%400==0:
    print("entered year is a leap year")
else:
    print("entered year is not a leap year")
