def function(first,second,third):
    if second=="+":
        return first+third
    elif second=="-":  
        return first-third
    elif second=="*":
        return first*third
    elif second=="/":
        return first/second    
    else:
        return "not assigned"        

first=int(input("enter the first number="))
second=input("enter the operator=")
third=int(input("enter the third number"))
print(function(first,second,third))