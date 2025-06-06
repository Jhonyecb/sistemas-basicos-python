nums = [int(x) for x in input(("Digite uma sequência de números separados por espaço: ")).split()]

par = (x for x in nums if x % 2 == 0)
impar = (x for x in nums if x % 2 != 0)

print("Números pares:", list(par))
print("Números ímpares:", list(impar))