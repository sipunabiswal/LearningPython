print("Welcome to the love calculator!")
name1=input("What is your name?\n")
name2=input("What is their name? \n")
name1.lower()
name2.lower()

t_t=0
t_t+=(name1+name2).count("t")
t_t+=(name1+name2).count("r")
t_t+=(name1+name2).count("u")
t_t+=(name1+name2).count("e")

l_t=0
l_t+=(name1+name2).count("l")
l_t+=(name1+name2).count("o")
l_t+=(name1+name2).count("v")
l_t+=(name1+name2).count("e")

love_percent=int(str(t_t)+str(l_t))

if (love_percent < 10) or (love_percent>90):
    print(f"Your score is {love_percent}%. you go togather like coke and mentos.")
elif (love_percent>40 and love_percent<50):
    print(f"Your score is {love_percent}%. you are alright togather.")
else:
    print(f"Your score is {love_percent}%.")