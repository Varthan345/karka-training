print("WELCOME TO METHOHELL'S TINY ADVENTURES")

house=input("you are in a creepy house! would you like to go'upstaris'or 'kitchen'?:\n>")
print("\n")
if house=="kitchen":
    kitchen=input("you may open the 'refregerator' or look in 'cabinet'.\n>")
    if kitchen=="refregerator":
        eat=input("so you want to list out any food to eat :YES or NO\n>")
        if eat=="yes":
            print(" you alive of starvation....")
        elif eat=="no":
            print("you die of starvation.....eventually")
    elif kitchen=="cabinet":
        take=input("would you like to look at a dressse (YES OR NO)\n>")
        if take=="yes":
            print(" you alive of starvation....")
        elif take=="no":
            print("you die of starvation.....eventually")
elif house=="upstair":
    upstair=input("so you want to get into a 'hall' or 'room':\n> ")
    if upstair=="hall":
        tv=input("so, you want to watch tv?(YES OR NO):\n>")
        if tv=="yes":
            print(" you alive of starvation....")
        elif tv=="no":
            print("you die of starvation.....eventually")
    elif upstair=="room":
        study=input("you want to open your book? (YES OR NO):\n>")
        if study=="yes":
            print(" you alive of starvation....")
        elif study=="no":
            print("you die of starvation.....eventually")