a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >  b and a > c:
    print("O maior número é:", a)

elif b > a and b > c:
    print("O maior número é:", b)

elif b == c or a == c or a == b:
    print("Dois ou mais números são iguais.")

else:
    print("O maior número é:", c)
   