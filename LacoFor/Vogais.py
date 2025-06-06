texto = (input("Digite uma palavra: "))

contadorVogais = 0

for letra in texto:
    if letra in 'aeiou': # Verifica se a letra é uma vogal
        contadorVogais += 1  # Incrementa o contador de vogais

print(contadorVogais)  # Imprime o total de vogais encontradas