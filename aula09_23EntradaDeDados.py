nome = input("Qual o seu nome?")
idade = input("Qual a sua idade?")
ano_nasc = 2022 - int(idade)

print(f'O usuario digitou o seu nome: {nome} e a sua idade: {idade} e o tipo da variavel é: {type(nome)} {type(idade)}')
print(f'o {nome} nasceu em: {ano_nasc}')

# posso fazer um  casting:
# se houver uma variavel instring int(input('digite o numero:'))