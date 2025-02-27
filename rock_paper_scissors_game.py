import random
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
game = [rock, paper, scissors]
computer = game[random.randint(0,len(game) - 1)]
user = input("welcome to rock paper scissors\npress 0 for rock, 1 for paper,2 for scissors\n")
if user not in ["0", "1", "2"]:
    print("PLEASE CHOSE A NUMBER FROM 0, 1 OR 2")
    exit()
if user == "0":
    print(rock)
elif user == "1":
    print(paper)
elif user == "2":
    print(scissors)
print(computer)
if user == "0" and computer == rock or user == "1" and computer == paper or user == "2" and computer == scissors:
    print("draw")
elif user == "0" and computer == scissors or user == "1" and computer == rock or user == "2" and computer == paper:
    print("You WIN!")
else:
    print("YOU LOSE :(")