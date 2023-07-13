current=0
def add_keychains():
    add=int(input(f"now you have {current} keychains,how many keychains you want to add:"))
    total=current+add
    print(f"now you have {total} keychains")
    return total
def remove_keychains():
    remove=int(input(f"now you have {current} keychains ,how many keychains you want to remove:"))
    total=current-remove
    print(f"now you have {total} keychains.")
    return total
def view_order():
    cost=10
    total=current*cost
    print(f"you have {current} keychains,\n keychains cost $10 each,\ntotal cost is ${total}")
    return total
def checkout():
    name=input("enter your name:")
    cost=10
    total=int(current*cost)
    print(f"you have {current} keychains.\n keychains cost $10 each,\ntotal cost is ${total}.\n thanks for your order,{name}")
    return total
while True:
    choice=int(input("enter your option:"))
    if choice==1:
        current=add_keychains()
    elif choice==2:
         current=remove_keychains()
    elif choice==3:
         current=view_order()
    elif choice==4:
         current=checkout()
         break
