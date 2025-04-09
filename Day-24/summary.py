#Abre o arquivo lê e fecha
# file = open("names.txt")
# content = file.read()
# print(content)
# file.close()


#Caso o arquivo não exista para escrever, ele é criado na hora, se for pra ler da erro
with open("new_file.txt",mode='w') as file:
    file.write("novo arquivo.")


#Faz o mesmo usando With e as, w quer dizer que estou abrindo para escrever,
# escreve por cima do texto contido no arquivo
with open("text.txt", mode='w') as file:
    file.write("novo texto.")


# 'a' de append adiciona o texto ao que já existe
with open("text.txt", mode='a') as file:
    file.write("\nmais novo texto.")
