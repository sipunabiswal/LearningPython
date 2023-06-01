from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=""
text=""
shift=""
print(f"{logo}")
def user_action():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift % 26
  ceasar(text=text,shift=shift,direction=direction)

def auto_cont():   
  con_activity=input("Type 'yes' if you want to go again. otherwise type 'no'.").lower()
  if con_activity=="yes":
    user_action()  
  else:
      print("Good bye !!!!")

def ceasar(text,shift, direction):
   cipher_word=""
   if direction=="decode":
         shift*= -1
   for letter in text:
      if letter in alphabet:
        curr_pos=alphabet.index(letter)      
        new_pos=curr_pos + shift
        cipher_word+=alphabet[new_pos]
      else:
         cipher_word+=letter

   print(f"The {direction}d text is {cipher_word}")
   auto_cont()


user_action()