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

user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_input=random.randint(0,2)


#if user_input==computer_input:
   # print(f"its a draw")
#elif user_input==0 and computer_input==1:
#    print(f"User chose {rock} and computer chose {paper} and you lose")
#elif user_input==0 and computer_input==2:
 #    print(f"User chose {rock} and computer chose {scissors} and its a win")
#elif user_input==1 and computer_input==0:
#    print(f"User chose {paper} and computer chose {rock} and you lose.")
#elif user_input==1 and computer_input==2:
#    print(f"User chose {paper} and computer chose {scissors} and you lose.")
#elif user_input==2 and computer_input==0:
#    print(f"User chose {scissors} and computer chose {rock} and you lose")
#elif user_input==2 and computer_input==1:
#    print(f"User chose {scissors} and computer chose {paper} and its a win")
#else:
#    print("Please provide a valid input as instructed.")


game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
