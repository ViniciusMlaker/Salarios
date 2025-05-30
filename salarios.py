# Arthur Ribeiro Araújo
# Emerson Sebastião dos Santos
# Matheus Latorre de Assis
# Vinícius Mlaker de Oliveira Dias

def verificarSalarioBruto(): # Função que recebe os salários brutos e os guarda ignorando o 0 e os colocando em ordem com InsertionSort (vale nota)
    salarioBruto = None
    listaSalariosBrutos = []
    while salarioBruto != 0:
        salarioBruto = float(input())
        index = 0
        while index < len(listaSalariosBrutos) and salarioBruto > listaSalariosBrutos[index]:
            index += 1
        if salarioBruto > 0:
            listaSalariosBrutos.insert(index, salarioBruto)
    return listaSalariosBrutos

def calcularAliquotaINSS(listaSalariosBrutos): # Função que retorna as aliquotas para cada salário bruto inserido
    listaAliquotaINSS = []
    for salarioBruto in listaSalariosBrutos:
        if salarioBruto <= 0:
            listaAliquotaINSS.append(0)
        if salarioBruto <= 1518:
            listaAliquotaINSS.append(7.5)
        elif salarioBruto <= 2793.88:
            listaAliquotaINSS.append(9)
        elif salarioBruto <= 4190.84:
            listaAliquotaINSS.append(12)
        elif salarioBruto <= 8157.41:
            listaAliquotaINSS.append(14)
        else:
            listaAliquotaINSS.append("Teto")
    return listaAliquotaINSS

def verificarDeducaoINSS(listaSalariosBrutos):
    listaDeducaoINSS = []
    for salarioBruto in listaSalariosBrutos:
        if salarioBruto <= 2793.88:
            listaDeducaoINSS.append(22.77)
        elif salarioBruto <= 4190.84:
            listaDeducaoINSS.append(106.59)
        elif salarioBruto <= 8157.41:
            listaDeducaoINSS.append(190.4)
        else:
            listaDeducaoINSS.append(0)
    return listaDeducaoINSS
    if aliqINSS == 9:
        return 22.77
    elif aliqINSS == 12:
        return 106.59
    elif aliqINSS == 14:
        return 190.4
    else:
        return 0

def calcularValINSS(salarioBruto, aliqINSS):
    if aliqINSS == "Teto":
        return 951.62
    else:
        return salarioBruto * (aliqINSS / 100) - deducaoINSS

def calcularBaseIR(salarioBruto, valorINSS):
    return salarioBruto - valorINSS

def calcularAliqIR(baseIR):
    if baseIR <= 2259.2:
        return 0
    elif baseIR <= 2826.65:
        return 7.5
    elif baseIR <= 3751.05:
        return 15
    elif baseIR <= 4664.68:
        return 22.5
    else:
        return 27.5

def verificarDeducaoIR(aliqIR):
    if aliqIR == 7.5:
        return 169.44
    elif aliqIR == 15:
        return 381.44
    elif aliqIR == 22.5:
        return 662.77
    elif aliqIR == 27.5:
        return 896
    else:
        return 0

def calcularValIR():
    if ((salarioBruto - valINSS) * (aliqIR / 100) - deducaoIR) < 10:
        return 0
    else:
        return (salarioBruto - valINSS) * (aliqIR / 100) - deducaoIR

def calcularSalarioLiquido():
    return salarioBruto - valINSS - valIR

# def formatarSaida():

iniciar = verificarSalarioBruto()
print(iniciar)
print(calcularAliquotaINSS(iniciar))
print(verificarDeducaoINSS(iniciar))