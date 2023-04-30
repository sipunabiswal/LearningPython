import random
names_string=input("Give me everybody's name , separated by a comma.")
names=names_string.split(",")
range=len(names)
#1st aproach
#name_index=random.randint(0,range-1)
#print(f"{names[name_index]} is going to by the meal today.")

#2nd Aproach
who_will_pay=random.choice(names)
print(f"{who_will_pay} is going to by the meal today.")
