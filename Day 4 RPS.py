import random

val = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors."))

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

images = [rock, paper, scissors]
choices = ["rock", "paper",  "scissors"]
comval = random.randint(0,2)
val_pick = choices[val]
com_pick = choices[comval]

print(images[val])
print(f"You chose {val_pick}")
print(images[comval])

if comval == val:
    print(f"Computer also chose {com_pick}. Draw!")
if comval == 0 and val == 1:
    print(f"Computer chose {com_pick}. You win!")
if comval == 0 and val == 2:
    print(f"Computer chose {com_pick}. You lose!")
if comval == 1 and val == 0:
     print(f"Computer chose {com_pick}. You lose!")
if comval == 1 and val == 2:
    print(f"Computer chose {com_pick}. You win!")
if comval == 2 and val == 0:
    print(f"Computer chose {com_pick}. You win!")
if comval == 2 and val == 1:
    print(f"Computer chose {com_pick}. You lose!")


