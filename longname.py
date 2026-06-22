print("Choose a username below 6 charaacter")
text = input("Enter a user name :")
a = len(text)
if a > 6 :
    print("the user name is long")
else:
    print(f"{text}, is your user name")
