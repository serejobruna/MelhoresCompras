rm = input("Insira seu RM")
idade = input("Insira sua idade")

if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")

#solicitando os dados do aluno
email_aluno = input("Informe o e-mail do aluno")
nota_semestral = input("Informe a nota semestral do aluno: ")
#convertendo a nota para o formato float
nota_semestral = float(nota_semestral)
#realizando o teste lógico
if nota_semestral > 8.5:
    print("ENVIANDO E-MAIL PARA {}".format(email_aluno))