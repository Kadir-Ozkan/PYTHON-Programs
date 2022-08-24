age = input('Are you a cigarette addict older than 75 years old? \n(Please use only "Yes" or "No" as answer)')
chronic = input('Do you have a severe chronic disease? \(Please use only "Yes" or "No" as answer)')
immune = input('Is your immune system too weak?\(Please use only "Yes" or "No" as answer)')
Bool_Dict = {"yes": True, "no": False}
age, chronic, immune = Bool_Dict[age.lower()], Bool_Dict[chronic.lower()], Bool_Dict[immune.lower()]
risk = age and chronic and immune
if risk:
    print("You are in risky group")
else:
    print("You are not in risky group")