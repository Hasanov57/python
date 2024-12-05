while True:
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    order=input("Type 'encode' to encypt, type 'decode' to decrypt\n")
    def encrypt():
        message=input("Type your message:\n").lower()
        shift=int(input("Type the shift number\n"))
        encrypted_message=list(message)
        for i in range(len(message)):
            index=alphabet.index(message[i])
            encrypted_message[i]=alphabet[(index+shift)%len(alphabet)]
        return "".join(encrypted_message)
    def decrypt():
        message=input("Type your message:\n").lower()
        shift=int(input("Type the shift number\n"))
        decrypted_message=list(message)
        for i in range(len(message)):
            index=alphabet.index(message[i])
            decrypted_message[i]=alphabet[(index-shift)%len(alphabet)]
        return "".join(decrypted_message)
    if order=='encode':
        print(f"Here is the encoded message : {encrypt()}")
    elif order=='decode':
        print(f"here is the decoded message : {decrypt()}")
    print("Do you want to continue to code or decode message?")
    answer=input("yes or no: ")
    if answer=="yes":
        True
    else:
        print("Thanks for using our program.")
        break