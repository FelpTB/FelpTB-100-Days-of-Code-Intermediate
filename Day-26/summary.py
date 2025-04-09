import random
import pandas

#lista de números
# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

#lista de caracteres
# nome = "Felipe"
# letras = [n for n in nome]
# print(letras)

#Lista usando Range
# double = [n*2 for n in range(1,5)]
# print(double)

#Lista condicional
# nomes = ["Amanda", "Bianca", "Carlos", "Diogo", "Eduardo", "Felipe"]
# nomes6 = [n for n in nomes if len(n) == 6]
#print(nomes6)
# nomes_maiusculo = [n.upper() for n in nomes if len(n) > 6]
#print(nomes_maiusculo)

#dicionários
# notas = {n: random.randint(1,100) for n in nomes}
# print(notas)

#percorrer dicionários, duas maneiras
# aprovados1 = {n:notas[n] for n in notas if notas[n] >= 60}
# aprovados2 = {nome:nota for (nota,nome) in notas.items() if nota >= 60}
# print(aprovados1)

aprovados = {
    "nome": ["Felipe", "Diogo", "Eduardo"],
    "nota": [65, 70, 87]
}

aprovados_dataframe = pandas.DataFrame(aprovados)

for (index,row) in aprovados_dataframe.iterrows():
    print(row.nome)
    print(row.nota)
