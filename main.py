alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' , 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))


def ceaser(start_text, shift_amount, cypher_direction):
    end_text = ""
    new_position = 0
    for letter in start_text:
        position = alphabet.index(letter)
        if cypher_direction == "encode":
            new_position = position + shift_amount
        elif cypher_direction == "decode":
            new_position = position - shift_amount
        end_text += alphabet[new_position]
    if cypher_direction == "encode":
        print(f"The encoded text is {end_text}")
    elif cypher_direction == "decode":
        print(f"The decoded text is {end_text}")
    else:
        print("Invalid Input")


ceaser(text, shift, direction)