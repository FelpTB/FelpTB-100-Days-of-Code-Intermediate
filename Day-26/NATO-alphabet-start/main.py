import pandas


#TODO 1. Create a dictionary in this format:

dataFrame = pandas.read_csv("nato_phonetic_alphabet.csv")
codes = {row.letter:row.code for (index,row) in dataFrame.iterrows()}
print(codes)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Insira seu nome: ").upper()
result = [codes[letter] for letter in name]
print(result)