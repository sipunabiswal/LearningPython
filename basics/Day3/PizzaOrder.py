print("Welcome to Python pizza deliveries!")
size=input("What size pizza do you want? S, M or L  ")
add_pepperoni=input("Do you want pepperoni? Y or N  ")
extra_cheese=input("Do you want extraa cheese? Y or N  ")

print("Small pizza: $15")
print("Medium pizz: $20")
print("Large pizz: $25")

print("Pepporoni for small pizza : + $2")
print("Pepporoni for Medium pizza or Large pizza : + $3")

print("Extra Cheese for any size pizza : +$1")

print(f"Pizza size {size}")
print(f"Add pepperoni {add_pepperoni}")
print(f"Extra cheese {extra_cheese}")

#base price for pizza
if size=="S":
    base_price=15
elif size =="M":
    base_price=20
elif size =="L":
    base_price=25
#if add pepperoni

if add_pepperoni=="Y" and size=="S":
    base_price+=2
else:
    base_price+=3

#Eztra Cheese
if extra_cheese=="Y":
    total_price=base_price+1
else:
    total_price=base_price

print(F"Your final bill is ${total_price}")