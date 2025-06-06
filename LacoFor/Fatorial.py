n = int(input("Digite um número: "))

fatorial = 1

for i in range(1, n+1):
    fatorial *= i  # Multiplica o valor de fatorial pelo valor de i

    print(fatorial)  # Imprime o valor do fatorial acumulado até o momento