# # -*- coding: utf-8 -*-
# #exercicio 1
num = int(input("Digite um numero: "))
if (num == 0):
    print("O numero e zero")
elif (num > 0):
    print("O numero e positivo")
else:
    print("O numero e negativo")

# #exercicio 2
num = int(input("Digite um numero: "))
if(num % 2 == 0):
    print("O numero e par")
else:
    print("O numero e impar")

# #exercicio 3
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
if(num1 > num2):
    print(num1, "e maior")
else:
    print(num2, "e maior")

# #exercicio 4
idade = int(input("Digite sua idade: "))
if(idade >= 18):
    print("Voce e maior de idade")
else:
    print("Voce e menor de idade")

# #exercicio 5
suaIdade = int(input("Digite sua idade: "))
maeIdade = int(input("Digite a idade da sua mae: "))
nasc = maeIdade - suaIdade
print("Sua mae o teve com ",nasc,"anos de idade")

# #exercicio 6
print("-"*50)

# #exercicio 7
num = int(input("Digite um numero: "))
if(num % 2 == 0):
    print("O numero e par")
else:    print("O numero e impar")

# #exercicio 8
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

# #exercicio 9
num = 3
if(num.__class_ is int):
   print("O numero ",num,"e do tipo inteiro")
else:
   print("O numero ", num, "nao e do tipo inteiro")

# #exercicio 10
txt = "Olá"
if(txt.__class__ is str):
   print("O texto",txt,"e do tipo string")
else:
   print("O texto", txt, "nao e do tipo string#")

# #exercicio 11
num = 5.4
if(num.__class__ is float):
    print("O valor",num,"e do tipo decimal")
else:
    print("O valor", num, "nao e do tipo decimal")

# #exercicio 12
num = float(input("Digite um numero: "))
if(num.is_integer()):
    print("O numero",num,"e inteiro")
else:
    print("O numero",num,"e decimal")

#exercicio 13
num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))
num3 = int(input("Terceiro numero: "))

if(num1 > num2 and num1 > num3):
    print(num1)
elif(num2 > num3):
    print(num2)
else:
    print(num3)

#exercicio 14
num = (4, 5, 3)

print(sorted(num))

#exercicio 15
vogais = ("A","E","I","O","U","a","e","i","o","u")
letra = str(input("Digite uma letra: "))
if(letra in vogais):
    print("A letra digitada e vogal")
else:
    print("A letra digitada nao e vogal")

#exercicio 16
ip = int(input("Digite um endereco IP: "))

A = list(range(0,127))
B = list(range(128,191))
C = list(range(192,223))
D = list(range(224,240))
E = list(range(240,256))
if ip in A:
    print("IP:",ip," Classe A")
elif ip in B:
    print("IP:",ip," Classe B")
elif ip in C:
    print("IP:",ip," Classe C")
elif ip in D:
    print("IP:",ip," Classe D")
else:
    print("IP:",ip," Classe E")

#exercicio 17
mes = int(input("Digite um mes do ano: "))
if(mes < 1 or mes > 12):
    print("Esse mes nao existe")
else:
    if(mes==1): print("Janeiro")
    elif(mes==2):print("Fevereiro")
    elif(mes==3):print("Março")
    elif(mes==4):print("Abril")
    elif(mes==5):print("Maio")
    elif(mes==6):print("Junho")
    elif(mes==7):print("Julho")
    elif(mes==8):print("Agosto")
    elif(mes==9):print("Setembro")
    elif(mes==10):print("Outubro")
    elif(mes==11):print("Novembro")
    elif(mes==12):print("Dezembro")

#exercicio 18
data = input("Digite uma data no formato DD/MM/AAAA: ")

dia, mes, ano = data.split("/")
if int(dia) in list(range(1, 32)) and int(mes) in list(range(1, 13)) and int(ano) in list(range(1970, 2019)):
    print(data)
else:
    print("Digite uma data valida")
