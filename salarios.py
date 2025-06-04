# Arthur Ribeiro Araújo
# Emerson Sebastião dos Santos
# Matheus Latorre de Assis
# Vinícius Mlaker de Oliveira Dias

def receberSalarioBruto(): 
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

def calcularAliquotaINSS(salarioBruto): 
    if salarioBruto <= 1518:
        return 7.5
    elif salarioBruto <= 2793.88:
        return 9
    elif salarioBruto <= 4190.84:
        return 12
    elif salarioBruto <= 8157.41:
        return 14
    else:
        return "Teto"

def verificarDeducaoINSS(salarioBruto): 
    if salarioBruto <= 1518 or salarioBruto >=8157.42:
        return 0
    elif salarioBruto <= 2793.88:
        return 22.77
    elif salarioBruto <= 4190.84:
        return 106.59
    elif salarioBruto <= 8157.41:
        return 190.4

def calcularValINSS(salarioBruto, aliquotaINSS, deducaoINSS): 
    if aliquotaINSS == "Teto":
        return 951.62
    else:
        return round(salarioBruto * (aliquotaINSS / 100) - deducaoINSS, 2)

def calcularBaseIR(salarioBruto, valorINSS): 
    return round(salarioBruto - valorINSS, 2)

def calcularAliquotaIR(baseIR): 
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

def verificarDeducaoIR(baseIR): 
    if baseIR <= 2259.2:
        return 0
    elif baseIR <= 2826.65:
        return 169.44
    elif baseIR <= 3751.05:
        return 381.44
    elif baseIR <= 4664.68:
        return 662.77
    else:
        return 896

def calcularValorIR(baseIR, aliquotaIR, deducaoIR): 
    if baseIR * (aliquotaIR / 100) - deducaoIR < 10:
        return 0
    else:
        return round(baseIR * (aliquotaIR / 100) - deducaoIR, 2)

def calcularSalarioLiquido(salarioBruto, valorINSS, valorIR): 
    return round(salarioBruto - valorINSS - valorIR, 2)

def formatarSaida(salariosBrutos): 
    saida = "     Bruto   AliqINSS   Val.INSS  Base I.R.     AliqIR     Val.IR    Liquido\n"

    for salarioBruto in salariosBrutos:
        aliquotaINSS = calcularAliquotaINSS(salarioBruto)
        deducaoINSS = verificarDeducaoINSS(salarioBruto)
        valorINSS = calcularValINSS(salarioBruto, aliquotaINSS, deducaoINSS)
        baseIR = calcularBaseIR(salarioBruto, valorINSS)
        aliquotaIR = calcularAliquotaIR(baseIR)
        baseIR = verificarDeducaoIR(baseIR)
        deducaoIR = verificarDeducaoIR(baseIR)
        valorIR = calcularValorIR(baseIR, aliquotaIR, deducaoIR)
        salarioLiquido = calcularSalarioLiquido(salarioBruto, valorINSS, valorIR)

        saida += f"{salarioBruto:>10.2f} {aliquotaINSS:>10} {valorINSS:>10.2f} {baseIR:>10.2f} {aliquotaIR:>10.2f} {valorIR:>10.2f} {salarioLiquido:>10.2f}\n"
    saida += "Fim dos dados\n"
    return saida

def gravarArquivo(saida):
    arquivo = open("CALCULOS.TXT", "w")
    arquivo.write(saida)
    arquivo.close()

salariosBrutos = receberSalarioBruto()
saida = formatarSaida(salariosBrutos)
gravarArquivo(saida)

print(saida)