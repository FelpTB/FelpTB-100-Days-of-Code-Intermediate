# try:# Algo que pode causar uma exceção
# except:# Se ocorrer uma exceção faça isso
# else:# Se não ocorrer uma exceção faça isso
# finally:# Apesar de tudo faça isso

#Palavras chave

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["cavalo"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("somethinng")
# except KeyError as error_message:
#     print(f"The Key {error_message} doesnt exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")

#Exemplo do raise

altura = float(input("Sua altura em metros é:"))
peso = int(input("Seu peso em quilos é:"))

if altura > 3:
    raise ValueError("A altura não pode ser maior que 3 metros")

bmi = peso / altura**2
print(bmi)


