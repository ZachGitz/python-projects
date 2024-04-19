

with open('Input/Names/invited_names.txt', 'r') as file:
    Names = file.readlines()
with open('Input/Letters/starting_letter.txt', 'r') as file:
    Lines = file.read()

PC="[name]"
for name in Names:
    name=name.strip()
    new_letter= Lines.replace(PC,name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt",'w') as file:
        file.write(new_letter)

