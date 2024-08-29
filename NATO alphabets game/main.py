import pandas
df=pandas.read_csv("nato_phonetic_alphabet.csv")
mydict={rows.letter:rows.code for (index,rows) in df.iterrows()}

def generate_phonetic():
    user_input = input('enter the word').upper()
    try:
        answer = [mydict[word] for word in user_input]
        print(answer)
        generate_phonetic()

    except KeyError:
        print('Sorry only alphabets are allowed')
        generate_phonetic()
generate_phonetic()