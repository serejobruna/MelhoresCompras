rm = input("Insira seu RM")
idade = input("Insira sua idade")

if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else:
    print("Sua participação não foi autorizada por causa da sua idade")

#solicitando os dados do cliente
valor_compra = input("Informe o valor da compra realizada ")
cupom = input("Digite o cupom de desconto ")
#realizando o teste lógico com o cupom em maiúsculas
if cupom.upper() == "NIVER10":
    #cálculo de 10% de desconto
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
#exibindo o valor final da compra
print("O valor final da compra é {}".format(valor_final))

minusculas = "mestre yoda"
#usamos a função upper para converter a string em letras maiúsculas
maiusculas = minusculas.upper()
print(minusculas)
print(maiusculas)