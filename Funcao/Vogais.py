texto = input("Digite um texto: ")

def contar(texto):
    vogal = 'aeiou'
    contador = 0

    for letra in texto: 
        if letra in vogal:  # Verifica se a letra é uma vogal
            contador += 1
    return contador  # Retorna o total de vogais encontradas

print(contar(texto))