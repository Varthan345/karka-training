height=float(input("your height in m:"))
weight=float(input("your weight in kg:"))
bmi=weight/height**height
print("your bmi is:",bmi)
if bmi<18.5:
    print('BMI category: under weight')
elif bmi>=18.5 and bmi<=24.9:
    print('BMI category: normal weight')
elif 25.0<=bmi<=29.9:
    print('BMI category: over weight')
elif bmi>30.0:
    print('obese') 
else:
    print("RE ENTER VALUE")   