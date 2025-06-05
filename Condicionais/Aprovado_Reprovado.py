nota = float (input("Digite a nota do aluno: "))

if nota >= 7:
        print("O aluno está aprovado.")
    
elif nota >= 5 and nota < 7:
        print("O aluno está de recuperação.")

else:
    print("O aluno está reprovado.")