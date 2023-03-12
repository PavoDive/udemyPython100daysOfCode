from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("\nWelcome to Giovanni's encryption utility.\n")

def encrypt(text, shift):
    shift = shift % 26
    indexes = []

    for i in text:
#        print(f"i primer for {i}")
        indexes.append(alphabet.index(i))
    new_indexes = indexes
    for i in range(0, len(indexes)):
#        print(f"i segundo for {i}")
#        print(f"indexes[i] = {indexes[i]}")
        if indexes[i] + shift >= 26:
            new_indexes[i] = indexes[i] + shift - 26
#            print("entro en este if")
        else:
            # print([i, indexes[i], shift])
            new_indexes[i] = indexes[i] + shift
    encrypted_text = []
    for i in new_indexes:
       encrypted_text.append(alphabet[i])

    print(f"Your encrypted message is: {''.join(encrypted_text)}")


def decrypt(text, shift):
    shift = shift % 26
    indexes = []

    for i in text:
        indexes.append(alphabet.index(i))
    new_indexes = indexes
    for i in range(0, len(indexes)):
        # if indexes[i] + shift < 0:
        #     new_indexes[i] = indexes[i] + shift + 26
        # else:
        #     # print([i, indexes[i], shift])
        new_indexes[i] = indexes[i] - shift
    decrypted_text = ""
    for i in new_indexes:
       decrypted_text = decrypted_text + alphabet[i]

    print(f"Your encrypted message is: {decrypted_text}")

want_to_leave = False

while not want_to_leave:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        print("You typed something else. Exiting...")
        want_to_leave = True
        break

    want_to_continue = input("\nPlease type 'yes' if you want to continue using the program, or 'no' if you want to exit.\n").lower()
    if want_to_continue == "no":
        want_to_leave = True
        print("Thank you. Exiting.")
    elif want_to_continue != "yes":
        want_to_leave = True
        print("I didn't understand that. Exiting.")
