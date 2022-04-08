# Rock Paper Scissor Game

import random
random_number  = random.randint(1, 3)

def computerChoice():
    if random_number == 1:
        computer_choice = 'r'
    elif random_number == 2:
        computer_choice = 'p'
    else:
        computer_choice = 's'
    return computer_choice

def win(your_choice):
    if computerChoice() == your_choice:
        print("OOP'S\nGame is Tie..!")
    else:
        if computerChoice() == 'r':
            print(f"Computer's Choice: r")
            if your_choice == 'p':
                print("\nCongratulations, You Win..")
            else:
                print("\nSorry, You Lose.!")
        if computerChoice() == 'p':
            print(f"Computer's Choice: p")
            if your_choice == 'r':
                print("\nSorry, You Lose.!")
            else:
                print("\nCongratulations, You Win..")
        if computerChoice() == 's':
            print(f"Computer's Choice: s")
            if your_choice == 'r':
                print("\nCongratulations, You Win..")
            else:
                print("\nSorry, You Lose.!")


your_choice = input("1. Type r for Rock \n2. type p for Paper \n3. Type s for Scissor \nEnter your Choice: ")
print(f"\nYour Choice: {your_choice}")
if your_choice == 'r' or your_choice == 'p' or your_choice == 's':
    win(your_choice)
else:
    print('Please Enter correct choice..!')
