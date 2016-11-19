import easygui as eg

# SETTING THINGS UP (only need this once)

eg.msgbox("Welcome to my awesome quiz!")

score = 0



# QUESTION 1

answers = ["A bird","A plane","Superman","A house","A horse"] 


choice = eg.buttonbox("What is this?","Quiz!",answers,"house.gif") 

if choice == "A house":
    eg.msgbox("Well done!","Quiz!")
    score = score + 1
else:
    eg.msgbox("No, you muppet. It was a house!","Quiz!")



# MORE QUESTIONS GO HERE

# QUESTION 2: FOOTBALL

answers = ["Football","Cricket","Rugby","Hockey","Banana racing"]


choice = eg.buttonbox("What sport is this?","Quiz!",answers,"football.gif")

if choice == "Football":
    eg.msgbox("Well done!","Quiz!")
    score = score + 1
else:
    eg.msgbox("No, you muppet. It was Football!","Quiz!")

# QUESTION 3: ICE-CREAM

answers = ["Fruit","Meat","Vegies","Cake","Ice cream cone" , "Pie"]


choice = eg.buttonbox("What dessert is this?","Quiz!",answers,"ice-cream.gif")

if choice == "Ice cream cone":
    eg.msgbox("Well done!","Quiz!")
    score = score + 1
else:
    eg.msgbox("No, you muppet. It was Ice cream cone!","Quiz!")

# QUESTION 4: KEY

answers = ["Key","Lock","USB stick","Poker","Spanner" , "Knob"]


choice = eg.buttonbox("What thing is this?","Quiz!",answers,"key.gif")

if choice == "Key":
    eg.msgbox("Well done!","Quiz!")
    score = score + 1
else:
    eg.msgbox("No, you muppet. It was a key!","Quiz!")

# QUESTION 5: ZZZZZ

answers = ["Sleep","Snooze","Doze","Nap","Rest" , "zzzzz"]


choice = eg.buttonbox("What activity is this?","Quiz!",answers,"zzzzz.gif")

if choice == "Sleep":
    eg.msgbox("Well done!","Quiz!")
    score = score + 1

if choice == "Snooze":
    eg.msgbox("Well done!","Quiz!")
    score = score + 1

if choice == "zzzzz":
    eg.msgbox("Well done! You got the lateral thinking bonus","Quiz!")
    score = score + 10

else:
    eg.msgbox("No, you muppet. Think harder!","Quiz!")

# QUESTION 6: SNAKE

answers = ["Worm","Snail","Gheko","Snake","Crocodile" , "Turtle"]


choice = eg.buttonbox("What thing is this?","Quiz!",answers,"snake.gif")

if choice == "Snake":
    eg.msgbox("Well done!","Quiz!")
    score = score + 1
else:
    eg.msgbox("No, you muppet. It was a Snake!","Quiz!")

# QUESTION 7: TOYOTA

answers = ["Nissan","Honda","Tata","Hyundai","Toyota" , "Mahindra"]


choice = eg.buttonbox("What brand is this?","Quiz!",answers,"toyota.gif")

if choice == "Toyota":
    eg.msgbox("Well done you tiger!","Quiz!")
    score = score + 1
else:
    eg.msgbox("No, you muppet. It was Toyota!","Quiz!")


# CHANGE THIS TO REFLECT DIFFERENT RESULTS

if score > 7:
    eg.msgbox("You know all","Quiz!")

if score < 1:
    eg.msgbox ("You loser!!!","Quiz!")

else:
    score == 1
    eg.msgbox("You got some right.  Better luck next time.")



# END

eg.msgbox("Well done, you scored " + str(score))
