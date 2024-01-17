def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print("********************* Calculadora em Python *********************\n")
print('Selecione o número da operação desejada: \n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão \n')

opcao = int(input("Digite sua opção (1/2/3/4):"))

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if opcao == 1:
    print(num1, "+", num2, "=", soma(num1, num2))
if opcao == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
if opcao == 3:
    print(num1, "*", num2, "=", mult(num1, num2))
if opcao == 4:
    print(num1, "/", num2, "=", div(num1, num2))
