# Arthur Ribeiro Araújo
# Emerson Sebastião dos Santos
# Matheus Latorre de Assis
# Vinícius Mlaker de Oliveira Dias

def verificarSalarioBruto(): # Função que recebe os salários brutos, os ordena em uma lista usando o InsertionSort (vale nota) e os retorna para atribuição em uma variável
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

def calcularAliquotaINSS(listaSalariosBrutos): # Função que retorna as aliquotas do INSS para cada salário bruto inserido
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

def verificarDeducaoINSS(listaSalariosBrutos): # Função que retorna as deduções do INSS para cada salário bruto inserido
    listaDeducaoINSS = []
    for salarioBruto in listaSalariosBrutos:
        if salarioBruto <= 1518 or salarioBruto >=8157.42:
            listaDeducaoINSS.append(0)
        elif salarioBruto <= 2793.88:
            listaDeducaoINSS.append(22.77)
        elif salarioBruto <= 4190.84:
            listaDeducaoINSS.append(106.59)
        elif salarioBruto <= 8157.41:
            listaDeducaoINSS.append(190.4)
    return listaDeducaoINSS

def calcularValINSS(iniciar, listaAliquotaINSS, listaDeducaoINSS): # Função que calcula o valor do INSS considerando a aliquota e a deduçãoe retorna em uma lista ordenada
    contador = 0
    listaValoresINSS = []
    for aliquota in listaAliquotaINSS:
        if aliquota == "Teto":
            listaValoresINSS.append(951.62)
        else:
            listaValoresINSS.append(round(iniciar[contador] * (aliquota / 100) - listaDeducaoINSS[contador], 2))
        contador += 1
    return listaValoresINSS

def calcularBaseIR(iniciar, listaValoresINSS): # Função para calcular a base do IR para usar nos cálculos futuros, retorna uma lista
    listaBaseIR = []
    contador = 0
    for salarioBruto in iniciar:
        listaBaseIR.append(round(salarioBruto - listaValoresINSS[contador], 2))
        contador += 1
    return listaBaseIR

def calcularAliquotaIR(listaBaseIR): # Função que retorna a lista de aliquotas para cálculo do Imposto de Renda
    listaAliquotaIR = []
    for baseIR in listaBaseIR:
        if baseIR <= 2259.2:
            listaAliquotaIR.append(0)
        elif baseIR <= 2826.65:
            listaAliquotaIR.append(7.5)
        elif baseIR <= 3751.05:
            listaAliquotaIR.append(15)
        elif baseIR <= 4664.68:
            listaAliquotaIR.append(22.5)
        else:
            listaAliquotaIR.append(27.5)
    return listaAliquotaIR

def verificarDeducaoIR(listaBaseIR):
    listaDeducaoIR = []
    for baseIR in listaBaseIR:
        if baseIR <= 2259.2:
            listaDeducaoIR.append(0)
        elif baseIR <= 2826.65:
            listaDeducaoIR.append(169.44)
        elif baseIR <= 3751.05:
            listaDeducaoIR.append(381.44)
        elif baseIR <= 4664.68:
            listaDeducaoIR.append(662.77)
        else:
            listaDeducaoIR.append(896)
    return listaDeducaoIR

def calcularValorIR(listaBaseIR, listaAliquotaIR, listaDeducaoIR):
    listaValoresIR = []
    contador = 0
    for baseIR in listaBaseIR:
        if baseIR * (listaAliquotaIR[contador] / 100) - listaDeducaoIR[contador] < 10:
            listaValoresIR.append(0)
        else:
            listaValoresIR.append(round(baseIR * (listaAliquotaIR[contador] / 100) - listaDeducaoIR[contador], 2))
        contador += 1
    return listaValoresIR

def calcularSalarioLiquido(iniciar, listaValoresINSS, listaValoresIR):
    listaSalarioLiquido = []
    contador = 0
    for salarioBruto in iniciar:
        listaSalarioLiquido.append(round(salarioBruto - listaValoresINSS[contador] - listaValoresIR[contador], 2))
        contador += 1
    return listaSalarioLiquido

def formatarSaida(iniciar, listaAliquotaINSS, listaValoresINSS, listaBaseIR, listaAliquotaIR, listaValoresIR, listaSalarioLiquido):
    print("     Bruto   AliqINSS   Val.INSS  Base I.R.     AliqIR     Val.IR    Liquido")
    contador = 0
    for salarioBruto in iniciar:
        print(f"{salarioBruto:>10} {listaAliquotaINSS[contador]:>10} {listaValoresINSS[contador]:>10} {listaBaseIR[contador]:>10} {listaAliquotaIR[contador]:>10} {listaValoresIR[contador]:>10} {listaSalarioLiquido[contador]:>10}")
        contador += 1


iniciar = verificarSalarioBruto()
listaAliquotaINSS = calcularAliquotaINSS(iniciar)
listaDeducaoINSS = verificarDeducaoINSS(iniciar)
listaValoresINSS = calcularValINSS(iniciar, listaAliquotaINSS, listaDeducaoINSS)
listaBaseIR = calcularBaseIR(iniciar, listaValoresINSS)
listaAliquotaIR = calcularAliquotaIR(listaBaseIR)
listaDeducaoIR = verificarDeducaoIR(listaBaseIR)
listaValoresIR = calcularValorIR(listaBaseIR, listaAliquotaIR, listaDeducaoIR)
listaSalarioLiquido = calcularSalarioLiquido(iniciar, listaValoresINSS, listaValoresIR)
formatarSaida(iniciar, listaAliquotaINSS, listaValoresINSS, listaBaseIR, listaAliquotaIR, listaValoresIR, listaSalarioLiquido)