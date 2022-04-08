import random

def gameWin(comp, you):
    if(you == comp):
        return "Game is tie"
    elif(comp == 's'):
        if(you == 'w'):
            return "Sorry, You Lose"
        else:
            return "Congratulation, You Win!"
    elif(comp == 'w'):
        return "Congratulation, You Win!"
    elif(comp == 'g'):
        return "Sorry, You Lose!"

randNo = random.randint(1, 3)
you = input("Please choose any One: \n1. Sanke(s) \n2. Water(w) \n3. Gun(g)\n")

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'
print("Computer Choose: ",comp)
print("You Choose: ",you)
f = gameWin(comp, you)
print(f)