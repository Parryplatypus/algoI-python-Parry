print("------Calculadora de Terminal------")
calcfeitos = 0
numero1 = 0
numero2 = 0
resultado = 0
option = 0
while True:
    print("Operações disponíveis: ")
    print("1- Soma 2- Subtração 3- Multiplicação 4- Divisão 5- potencia 6- Resto 0- Sair")
    option = int(input("Digite a opção desejada: "))
    if option < 0 or option > 6:
        print("Opção inválida, tente novamente.")
    else:
        if option == 1:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            resultado = numero1 + numero2
            print(f"O resultado da soma é: {resultado:.2f}")
            calcfeitos += 1
        elif option == 2:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            resultado = numero1 - numero2
            print(f"O resultado da subtração é: {resultado:.2f}")
            calcfeitos += 1
        elif option == 3:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            resultado = numero1 * numero2
            print(f"O resultado da multiplicação é: {resultado:.2f}")
            calcfeitos += 1
        elif option == 4:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            if numero2 == 0:
                print("Não é possível dividir por zero.")
            else:
                resultado = numero1 / numero2
                print(f"O resultado da divisão é: {resultado:.2f}")
                calcfeitos += 1
        elif option == 5:
            numero1 = float(input("Digite a base: "))
            numero2 = float(input("Digite o expoente: "))
            resultado = numero1 ** numero2
            print(f"O resultado da potência é: {resultado:.2f}")
            calcfeitos += 1
        elif option == 6:
            numero1 = float(input("Digite o dividendo: "))
            numero2 = float(input("Digite o divisor: "))
            if numero2 == 0:
                print("Não é possível calcular o resto da divisão por zero.")
            else:
                resultado = numero1 % numero2
                print(f"O resultado do resto da divisão é: {resultado:.2f}")
                calcfeitos += 1
        elif option == 0:
            print(f"Você realizou {calcfeitos} cálculo(x).")
            print("Saindo da calculadora bahx")
            break
print("código resenhax slkx no clubexx")
    
            