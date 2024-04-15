weight = float(input("Enter your body weight:"))
unit = input("Is it (L)bs or (K)gs:")
if (unit.upper() == "K"):
    new_weight = weight * 2.2
    print(f"You are {new_weight} pounds")
else:
    new_weight = weight/2.2
    print(f"You are {new_weight} kilos")
