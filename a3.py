print("Enter the Rounded Marks in 5 subjects")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

total = markOne + markTwo + markThree + markFour + markFive
avg = int(total / 5)

validRange = range(0,101)

if avg not in validRange:
    print("This is invalid.")
elif avg in range(91, 101):
    print("That's amazing! You will get far my friend")
elif avg in range(81, 91):
    print("That's still really good! So proud of you and just try a little harder and you'll get through it")
elif avg in range(71, 81):
    print("A bit rough but it's still good! Keep trying")
elif avg in range(61, 71):
    print("Okay... That's alirhgt you cacn do it")
elif avg in range(51, 61):
    print("That's not...You can still improve though and I believe you can")
elif avg in range(41, 51):
    print("Ummm. I have no words but as long as you're happy")
elif avg in range(33, 41):
    print("THAT'S CRAZY! You can still pick it up, I think")
elif avg in range(21, 33):
    print("OMG, how are you that low?!")
elif avg in range(0, 21):
    print("Yeah you're cooked, I can't really help now.")