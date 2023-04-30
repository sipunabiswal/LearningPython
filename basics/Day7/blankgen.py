import random
word_list=["ardavark", "babbon","camel"]
#random_index=random.randint(0,2)
chossen_word=random.choice(word_list)
user_input=input("Enter a random char :")
blank_list=[]

for char in chossen_word:
    if char==user_input:
        blank_list.append(user_input)
    else:
        blank_list.append('_')

print(blank_list)