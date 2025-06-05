lado1 = int(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = int(input("Digite o comprimento do segundo lado do triângulo: "))  
lado3 = int(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 == lado2 and lado2 == lado3:
    print("O triângulo é equilátero.")

elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("O triângulo é isósceles.")

else:
    print("O triângulo é escaleno.")