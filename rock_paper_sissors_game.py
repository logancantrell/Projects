import random
user_chose = input("Beat the computer chose rock, paper or scissors:\nType 0 for rock, 1 for paper, 2 for scissors\n")
user_chose = int(user_chose)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# scissors > paper > rock > scissors  2 > 1 > 0 > 2
game = [rock, paper, scissors]
comp_choice = random.randint(0,2)
print("You chose: ", game[user_chose])
print("Computer chose: ", game[comp_choice])


if user_chose == comp_choice:
    print("Draw")
elif user_chose == 0 and comp_choice == 2:
    print("You win")
elif user_chose == 2 and comp_choice == 0:
    print("You lose")
elif user_chose > comp_choice:
    print("You win")
else:
    print("You lose")