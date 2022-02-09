alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  shift_amount%=26
  if cipher_direction == "decode":
    shift_amount *= -1
  start_text=start_text.split(" ")
  for word in start_text:
    for char in word:
      if char in alphabet:
      #end_text = "•••• •• •• 3"
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text+=char
    end_text+=" "
  print(f"Here's the {cipher_direction}d result: {end_text}")

def initiate():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if((direction=="encode" or direction=="decode")):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  else:
    print("Please enter correct input")

    
import art
ask_flag=True
print(art.logo)
repeat="yes"
while(repeat=="yes"):
  initiate()
  repeat=input("Do you want to continue?").lower()
  if(repeat=="no"):
    print("Goodbye!!")
  elif(repeat != "yes"):
    print ("Please enter right input")
    repeat="yes"
