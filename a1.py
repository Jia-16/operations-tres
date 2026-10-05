x = 5
if (type(x) is int):
    print("That is very true")
else:
    print("That's false labelling")

x = 5.5
if (type(x) is not float):
    print("As this is a whole number, it is true")
else:
    print("That is a very obviously not a whole number")

x = 20
y = 20

if (x is y):
    print("x and y are the same and have the same identity")

y = 30
if (x is not y):
    print("They do NOT relate to eachother whatsoever")