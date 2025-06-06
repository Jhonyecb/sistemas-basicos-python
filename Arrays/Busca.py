nums = [int(x) for x in input(("Digite uma sequência de números separados por espaço: ")).split()]

x = int(input(("Busque um número na lista: ")))

if x in nums:
    print("o número", x, "está na lista.")
else:
    print("O número", x, "não está na lista.")
