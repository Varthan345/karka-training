def add_keychains():
    return "ADD KEYCCHAINS"

def remove_keychains():
    return "REMOVE KEYCHAINS"

def view_order():
    return "VIEW ORDER"
def checkout():
    return "CHECKOUT"

print("ye olde keychain shop\n 1. add keychains to order\n 2. remove keychains from order\n 3. view current order\n 4. checkout")
print("\n")
while True:
    choice=int(input("enter your option:"))
    if choice==1:
        print("\n",add_keychains())
    elif choice==2:
         print("\n",remove_keychains())
    elif choice==3:
        print("\n",view_order())
    elif choice==4:
        print("\n",checkout())
        break