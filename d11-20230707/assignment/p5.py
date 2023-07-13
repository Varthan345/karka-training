name=input("what is your name?")
print("\n")
age=input("hi,{}! how old are you?".format(name))
print("\n")
age_after=int(age)+5
age_before=int(age)-5
print("did you know that, in five years you will be {}years old ?\nand five years ago you were  {}! Imagine that".format(age_after,age_before))