from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' , 'z']



def ceaser(start_text, shift_amount, cypher_direction):
    end_text = ""
    if cypher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    if cypher_direction == "encode":
        print(f"The encoded text is {end_text}")
    elif cypher_direction == "decode":
        print(f"The decoded text is {end_text}")
    else:
        print("Invalid Input")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
    shift = shift % 26
    ceaser(text, shift, direction)
    cont = input("Type 'Yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if cont == "no":
        should_continue = False
        print("Goodbye")