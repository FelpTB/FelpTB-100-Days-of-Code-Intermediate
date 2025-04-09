import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Pegando a quantidade de cada esquilo
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

#Criando o Dicionário
dict = {
    "Color": ["Gray", "Black", "Red"],
    "Count": [gray_count, black_count, red_count]
}

#Transformando o dicionário em dataframe
dataframe = pandas.DataFrame(dict)
dataframe.to_csv("squirrels.csv")

print(dict)
