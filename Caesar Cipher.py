#function to encrypt the message
def caesar_encrypt(msg, shift):
    cipher= ""
    for c in msg:
        if c.isalpha():
          if c.isupper():
            cipher += chr((ord(c)-65 + shift)% 26+65)
          else: #if lowercase letter
            cipher += chr((ord(c)-97 + shift)%26+97)
        else:
          cipher+= c
    return cipher   




#function to decrypt the message  
  
def caesar_decrypt(msg, shift):
    return caesar_encrypt(msg, -shift) #  decrypt by shifting in reverse

#main function to run the program

def main():
    print("Caesar cipher Program")

    while True:
        option=input("Choose (E)encrypt, (D)decrypt, (Q)quit : ").upper()

        if option =='Q':
            print("Exiting program.")
            break
        
        if option not in ['E','D']:
            print ("Wrong Option. please try again.")
            continue
        message = input("Enter the text :")
        try:
            s=int(input("enter shift number:"))
        except:
            print("shift must be a number. try again")
            continue

        if option=='E':
            encrypted = caesar_encrypt(message, s)
            print("Encrypted Text:", encrypted)
        else:
            decrypted = caesar_decrypt(message, s)
            print("Decrypted Text:", decrypted)

# run the program

if __name__ == "__main__":
    main()

