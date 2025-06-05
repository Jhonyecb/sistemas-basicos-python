n = int(input("Digite um número: "))

acumulador = 0

for i in range(1, n+1):
    acumulador += i  # Acumula o valor de i

    print(acumulador)  # Imprime o valor acumulado