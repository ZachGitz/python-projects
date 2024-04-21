import pandas
student_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

dict={row.letter:row.code for (index, row) in student_data_frame.iterrows()}

n = input("Enter the Word: ").upper(H)

ans = [dict[i] for i in n]

print(ans)



