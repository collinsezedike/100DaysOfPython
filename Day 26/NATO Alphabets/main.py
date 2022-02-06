import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
NATO_alphabets_df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_alphabets_dict = {row.letter: row.code for (index, row) in NATO_alphabets_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
user_word_NATO_list = [NATO_alphabets_dict[letter] for letter in user_word]
print(user_word_NATO_list)
