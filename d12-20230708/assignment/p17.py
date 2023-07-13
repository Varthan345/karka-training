print("WELCOME TO THE BANK OF BRUDA")
while True:
    your_pin=int(input("\nENTER YOUR PIN:"))
    if your_pin==1234:
        print("PIN ACCEPTED.YOU HAVE ACCESS TO YOUR ACCOUNT")
        break
    else:
        print("INCORRECT PIN.try again\n")
