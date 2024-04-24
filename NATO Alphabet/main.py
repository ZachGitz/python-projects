
import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

dict={row.letter:row.code for (index, row) in data.iterrows()}
while True:
    try:
        n = input("Enter the Word: ").upper()

        ans = [dict[i] for i in n]

        print(ans)
        break
    except:
        print("Enter a word!!")
        continue



