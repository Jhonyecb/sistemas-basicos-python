a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

for i in range(a, b + 1):
    if i % 2 != 0:  # Verifica se i é ímpar
        print(i)