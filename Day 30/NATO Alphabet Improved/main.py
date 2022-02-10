import pandas

NATO_alphabets_df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_alphabets_dict = {row.letter: row.code for (index, row) in NATO_alphabets_df.iterrows()}

is_invalid = True
while is_invalid:
    user_word = input("Enter a word: ").upper()
    try:
        user_word_NATO_list = [NATO_alphabets_dict[letter] for letter in user_word]
        is_invalid = False
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        is_invalid = True
print(user_word_NATO_list)


# Angela's
# def generate_alphabets():
#     user_word = input("Enter a word: ").upper()
#     try:
#         user_word_NATO_list = [NATO_alphabets_dict[letter] for letter in user_word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_alphabets()
#     else:
#         print(user_word_NATO_list)


# generate_alphabets()
