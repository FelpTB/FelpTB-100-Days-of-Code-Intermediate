nomes = []


with open("../names.txt", mode='r') as file:
   for linha in file:
       n = linha.strip()
       nomes.append(n)

with open("../letter.txt", mode='r') as file:
        carta = file.read()

for n in nomes:
    nova_carta = carta.replace("[name]", n)

    caminho_carta_personalizada = f"./Letters/{n}.txt"

    with open(caminho_carta_personalizada, mode='w') as file:
        file.write(nova_carta)



