month_name=int(input("enter the month number:"))
def month(month_name):
    if month_name==1:
        return "january"
    elif month_name==2:
        return "february"
    elif month_name==3:
        return "march"
    elif month_name==4:
        return "april"
    elif month_name==5:
        return "may"
    elif month_name==6:
        return "june"
    elif month_name==7:
        return "july"
    elif month_name==8:
        return "august"
    elif month_name==9:
        return "september"
    elif month_name==10:
        return "october"            
    elif month_name==11:
        return "november"
    elif month_name==12:
        return "december"  

print(month(month_name))