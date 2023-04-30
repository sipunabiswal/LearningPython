print("Welcome to the rollercoaster")
height=int(input("What is your height in CM?"))

if height>120:
    print("You can ride the roller coaster!")

    age=int(input("What is your age?"))
    if(age<12):
        bill=5
        print("Child tickets are $5")
    elif(age <=18):
        bill=7
        print("Youth tickets are $7")
    elif (age >=45 and age <=55):
        bill=0
        print("Mid age tickets are free")
    else:
        bill=12
        print("Adult tickets are $12")

    want_photo=input("Do you want a photograph ? Y or N")
    if(want_photo=="Y"):
        bill+=2

        print(f"Your total bill is ${bill}")
else:
    print("Sorry, you have to grow to ride the roller coaster")

#indentetion : Indentation refers to the spaces at the beginning of a code line. 
# Where in other programming languages the indentation in code is for readability only, 
# the indentation in Python is very important. Python uses indentation to indicate a block of code.