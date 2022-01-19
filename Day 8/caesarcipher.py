def caesar(start_text, shift_amount, cipher_direction):
    end_text = []
    shift_amount %= len(alphabet)
    for letter in start_text:
        if letter not in alphabet:
            end_text.append(letter)
        else:
            for index in range(len(alphabet)):  # Angela used an index method. Had I known
                if letter == alphabet[index]:
                    if cipher_direction == 'encode':
                        encrypted_letter = alphabet[((index + shift_amount) - len(alphabet))]   
                        # I did minus len(alphabet) so that the program reads the list from behind because otherwise, it would produce a range error.
                        # Angela doubled the letters in the alphabet list, so after z is abc...z
                        end_text.append(encrypted_letter)
                    elif cipher_direction == 'decode':
                        decrypted_letter = alphabet[(index - shift_amount)]
                        end_text.append(decrypted_letter)

    print(f"The {cipher_direction}d text is {''.join(end_text)}")



run_again = True    
while run_again:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(start_text = text, shift_amount= shift, cipher_direction = direction)

    rerun = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if rerun == 'no':
        run_again = False
        print('Program closed.')