# -*- coding: utf-8 -*-

#exercicio 1

num = int(input("Digite um numero: "))
if (num == 0):
    print("O numero e zero")
elif (num > 0):
    print("O numero e positivo")
else:
    print("O numero e negativo")

#exercicio 2
num = int(input("Digite um numero: "))
if(num % 2 == 0):
    print("O numero e par")
else:
    print("O numero e impar")

#exercicio 3
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
if(num1 > num2):
    print(num1, "e maior")
else:
    print(num2, "e maior")

#exercicio 4
idade = int(input("Digite sua idade: "))
if(idade >= 18):
    print("Voce e maior de idade")
else:
    print("Voce e menor de idade")

#exercicio 5
suaIdade = int(input("Digite sua idade: "))
maeIdade = int(input("Digite a idade da sua mae: "))
nasc = maeIdade - suaIdade
print("Sua mae o teve com ",nasc,"anos de idade")

#exercicio 6
print("-"*50)

#exercicio 7
num = int(input("Digite um numero: "))
if(num % 2 == 0):
    print("O numero e par")
else:    print("O numero e impar")

#exercicio 8
num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))
if(num1>num2):
   print("Imprimindo o maior valor")
   print(num1)
   print("Imrimindo o menor valor")
   print(num2)
else:
   print("Imprimindo o maior valor")
   print(num2)
   print("Imprimindo o menor valor")
   print(num1)

#exercicio 9
num = 3
if(num.__class_ is int):
   print("O numero ",num,"e do tipo inteiro")
else:
   print("O numero ", num, "nao e do tipo inteiro")

#exercicio 10
txt = "Olá"
if(txt.__class__ is str):
   print("O texto",txt,"e do tipo string")
else:
   print("O texto", txt, "nao e do tipo string#")

#exercicio 11
num = 5.4
if(num.__class__ is float):
    print("O valor",num,"e do tipo decimal")
else:
    print("O valor", num, "nao e do tipo decimal")

#exercicio 12   