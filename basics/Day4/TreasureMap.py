row1=['⬜️', '⬜️', '⬜️']
row2=['⬜️', '⬜️', '⬜️']
row3=['⬜️', '⬜️', '⬜️']

map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position= input("Where do you want to put the treasure?  ")

horizental=int(position[0])-1
vertical=int(position[1])-1

#map[vertical][horizental]="X"
#print(f"{row1}\n{row2}\n{row3}")
#2nd way 
selected_row=map[vertical]
selected_row[horizental]="X"

print(f"{row1}\n{row2}\n{row3}")
