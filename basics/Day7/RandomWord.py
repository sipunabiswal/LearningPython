import random
word_list=["ardavark", "babbon","camel"]
#random_index=random.randint(0,2)
chossen_word=random.choice(word_list)
user_input=input("Enter a random char :")

for char in chossen_word:
    if char.lower()==user_input.lower():
        print("Right")
    else:
        print("Wrong")
