import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives=6
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

wrong_guess=False
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game and lives>0:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            wrong_guess=True
    if wrong_guess:
        lives-=1

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    if lives==0:
        print("You Loose.")
    print(stages[lives])