import csv
import pandas

# Lendo arquivos em csv sem usar pandas
# temperatures = []
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
#     for n in temperatures:
#         print(n)


#Lendo arquivos Csv com pandas
data = pandas.read_csv("weather_data.csv")
# print(data)

#Mostra apenas a coluna "temp"
# print(data['temp'])

#Em pandas temos tipos de dados como por exemplo:
#series(dados unidimensionais) e dataframes(dados bidimensionais).

#transforma em dicionário
# data_dict = data.to_dict()
# print(data_dict)

#transforma em lista
temp_list = data['temp'].to_list()
print(temp_list)

#Calculo da média sem usar pandas
mean = 0
for i in temp_list:
    mean = mean + i
mean = mean/len(temp_list)
print(round(mean,2))

#Calculo da média com pandas
print(round(data['temp'].mean(),2))

#Valor máximo da série
#Panda transforma índice em atributo
print(data.temp.max())

#mostra o dia com a maior temperatura
print(data[data.temp == data.temp.max()])

#temperatura de segunda em Fahrenheit
monday = data[data.day == "Monday"]
print((monday.temp*1.8)+32)

#Criando um dataframe
dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

dataframe = pandas.DataFrame(dict)
dataframe.to_csv("new_data.csv")


