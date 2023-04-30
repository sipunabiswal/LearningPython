import random
word_list=["ardavark", "babbon","camel"]
#random_index=random.randint(0,2)
chossen_word=random.choice(word_list)
word_len=len(chossen_word)

display=[]
for _ in range(word_len):
    display+="_"

end_of_game=False

while not end_of_game:
    guess=input("Guess a letter: ").lower()
    for potion in range(word_len):
        letter=chossen_word[potion]
        if letter==guess:
            display[potion]=letter

    print(display)

    if "_" not in display:
        end_of_game=True
        
        
print("you win")