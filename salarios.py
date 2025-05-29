# Arthur Ribeiro Araújo
# Emerson Sebastião dos Santos
# Matheus Latorre de Assis
# Vinícius Mlaker de Oliveira Dias

def calcularAliqINSS(salarioBruto):
    if salarioBruto <= 0:
        return 0
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

def verificarDeducaoINSS(aliqINSS):
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

salarioBruto = 1815
print(f"SALARIO BRUTO {salarioBruto}")
aliqInss = calcularAliqINSS(salarioBruto)
print(f"ALIQUOTA INNS {aliqInss}")
deducaoINSS = verificarDeducaoINSS(aliqInss)
print(f"DEDUCAO INSS {deducaoINSS:.2f}")
valINSS = calcularValINSS(salarioBruto, aliqInss)
print(f"VAL INSS {valINSS:.2f}")
baseIR = calcularBaseIR(salarioBruto, valINSS)
print(f"BASE IR {baseIR:.2f}")
aliqIR = calcularAliqIR(baseIR)
print(f"ALIQ IR {aliqIR:.2f}")
deducaoIR = verificarDeducaoIR(aliqIR)
print(f"DEDUCAO IR {deducaoIR:.2f}")
valIR = calcularValIR()
print(f"VALOR IR {valIR:.2f}")
salarioLiquido = calcularSalarioLiquido()
print(f"SAL LIQUIDO {salarioLiquido:.2f}")
