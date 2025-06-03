from random import randint
arq = open("testeentrada.txt", "w")

lista = []
contador = 0

while contador < 10000:
    lista.append(randint(2, 9000))
    arq.write(f"{lista[contador]}\n")
    contador += 1

arq.close()