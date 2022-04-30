morse_alphabet = {
    
    # LETTERS
    "A": ".-",
    "B": "–···",
    "C": "–·–·",
    "D": "–··",
    "E": "·",
    "F": "··–·",
    "G": "––·",
    "H": "····",
    "I": "··",
    "J": "·---",
    "K": "-·-",
    "L": "·-··",
    "M": "--",
    "N": "-·",
    "O": "---",
    "P": "·--·",
    "Q": "--·-",
    "R": "·-·",
    "S": "···",
    "T": "-",
    "U": "··-",
    "V": "···-",
    "W": "·--",
    "X": "-··-",
    "Y": "-·--",
    "Z": "--··",

    # NUMBERS
    "0": "-----",
    "1": "·----",
    "2": "··---",
    "3": "···--",
    "4": "····-",
    "5": "·····",
    "6": "-····",
    "7": "--···",
    "8": "---··",
    "9": "----·",
}

print("\nMORSE CODE TRANSLATOR")
print("Enter 'quit' to close the application.")
while True:
    text = input("\nEnter text: \n").upper()
    if text.strip() == "QUIT":
        break
    else:
        morse_code = str()
        for letter in text.strip():
            morse_code += f"{morse_alphabet.get(letter, letter)}   "
        print(f"\nMorse code Translation: \n{morse_code.strip()}")
print("\nTo see the other amazing things I am building,\nFollow me on Twitter @collinsezedike\n")


# LITTLE DOCUMENTATION

# In morse code, a space is 7 units.
# I did not add a space to the morse alphabets dictionary because  
# during translation, three spaces separates each letter (Line 47). 
#
# So, when there is a space in the text, the program evaluates like this:
# the letter before the space appends three spaces,
# the space remains a space since it is not in the dictionary; 3+1=4
# finally, the space adds it's own space; 4+3=7
# seven spaces to separate words
#
# Follow me on Twitter: @collinsezedike"
