
resultado = int(input('Bem-vindo a calculadora Python \n \n Digite a operação: \n 1)Soma \n 2)Subtração \n 3)Divisão \n 4)Multiplicação \n \n'))
#resultado = resultad


def chamarNumero1():
    return int(input("Digite o primeiro número: \n"))

def chamarNumero2():
    return int(input("Digite o segundo número: \n"))

def somar():
    num1 = chamarNumero1()
    num2 = chamarNumero2()
    result = num1 + num2
    return print("Resultado da soma: " , result)

def subtrair():
    num1 = chamarNumero1()
    num2 = chamarNumero2()
    return print("Resultado da subtração: " , (num1 - num2))


def dividir():
    num1 = chamarNumero1()
    num2 = chamarNumero2()
    return print("Resultado da divisão: " , (num1 / num2))

def multiplicar():
    num1 = chamarNumero1()
    num2 = chamarNumero2()
    return print("Resultado da multiplicação: " , (num1 * num2))


while resultado < 5:
    if resultado == 1:
        somar()
        break
    elif resultado == 2:
        subtrair()
        break
    elif resultado == 3:
        dividir()
        break
    elif resultado == 4:
        multiplicar()
        break
    else: 
        print("Valor não reconhecido!")
