import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  message=""
  for letter in text:
    if letter in alphabet:
      j = alphabet.index(letter)
      if direction.lower() == "encode":
        k = j+shift
        if k > len(alphabet)-1:
          k=k%len(alphabet)
      elif direction.lower() == "decode":
        k = j-shift
        while k < 0:
          k = k+len(alphabet)
      message = message + (alphabet[k])
    else:
      message+=letter

  print(f"Your {direction}d message is {message}")

should_continue = True
while should_continue == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)

  restart = input("go again: \n")
  restart = restart.lower()
  if restart =="n" or restart=="no":
    should_continue = False
    print("Goodbye")
    break
  else:
    continue
