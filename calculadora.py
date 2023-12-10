
# Calculadora simples em Python

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: divisão por zero"

while True:
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite a opção (1/2/3/4/5): ")

    if escolha == '5':
        print("Encerrando a calculadora.")
        break

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(num1, "+", num2, "=", adicao(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicacao(num1, num2))

        elif escolha == '4':
            resultado_divisao = divisao(num1, num2)
            if isinstance(resultado_divisao, str):
                print(resultado_divisao)
            else:
                print(num1, "/", num2, "=", resultado_divisao)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
