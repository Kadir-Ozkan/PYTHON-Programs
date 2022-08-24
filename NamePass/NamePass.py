NamePass = ("1d5q?r", "joseph")
name = input("What is your name please?:")
if name.lower() == NamePass[1]:
  print(f"Hello {NamePass[1]}, your password is: {NamePass[0]}")
else:
  print(f"Hello {name}. See you soon!")
