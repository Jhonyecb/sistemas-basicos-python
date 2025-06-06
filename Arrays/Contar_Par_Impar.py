nums = [int(x) for x in input(("Digite uma sequência de números separados por espaço: ")).split()]

par = 0
impar = 0

for x in nums:
    if x % 2 == 0:
        par += 1
    else:
        impar += 1

print("Quantidade de números pares:", par)
print("Quantidade de números ímpares:", impar)