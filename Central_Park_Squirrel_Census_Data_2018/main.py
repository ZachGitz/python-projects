import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240420.csv")

grey=0
black=0
red=0
for i in data["Primary Fur Color"]:
    if(i=="Gray"):grey+=1
    if (i == "Cinnamon"): red += 1
    if (i == "Black"): black += 1

dict= {"Colour":["Grey","Red","Black"],"No of Squirrel":[grey,red,black]}

new_data=pandas.DataFrame(dict)

new_data.to_csv("Squirrel Colour Data.csv")