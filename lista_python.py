# -*- coding: utf-8 -*- #

# exercicio 1
print("Leonardo Oliveira Novais da Silva")

# exercicio 2
nome = input("Digite seu nome: ")
print("O seu nome é", nome)

# exercicio 3
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("O seu nome é", nome, "e a sua idade é", idade)

# exercicio 4
num = int(input("Digite um número: "))
print(num)

# exercicio 5
num = int(input("Digite um número: "))
print("O número digitado foi", num)

# exercicio 6
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
soma = (num1 + num2 + num3)
print("A soma total é:", soma)

# exercicio 7
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = (num1 + num2)
print("A soma total entre", num1, "e", num2, "é igual", soma)

# exercicio 8
n1 = float(input("Digite a nota do primeiro bimestre: "))
n2 = float(input("Digite a nota do segundo bimestre: "))
n3 = float(input("Digite a nota do terceiro bimestre: "))
n4 = float(input("Digite a nota do quarto bimestre: "))
media = (n1 + n2 + n3 + n4) / 4
print(media)

# exercicio 9
metros = float(input("Insira a medida em metros: "))
cm = metros * 100
print("Medida em centimetros:", cm, "cm")

# exercicio 10
num = int(input("Digite um numero: "))
quadrado = num ** 2
cubo = num ** 3
print("Número ao quadrado:", quadrado)
print("Número ao cubo:", cubo)

# exercicio 11
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

div1 = num1 / num2
div2 = num1 // num2

print("Total decimal da divisão:", div1)
print("Total inteiro da divisão:", div2)

# #exercicio 12
largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

metros = largura * altura
print("Você possui", metros, "metros quadrados")

# exercicio 13
dias = int(input("Insira a quantidade de dias: "))
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))

conv_m = minutos * 60
conv_h = horas * 60
conv_d = dias * 24
total = (conv_d * (conv_h * conv_m)) + segundos
print("Total em segundos:", total)

# exercicio 14
valor = float(input("Digite o valor do produto: "))

desconto = valor * (10 / 100)
valor_final = valor - desconto

print("Valor total: R$", valor_final)
print("Desconto: R$", desconto)
