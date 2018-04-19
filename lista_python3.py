#exercicio 1
print(list(range(1,101)))

#exercicio 2
inicio = int(input("Digite o primeiro numero: "))
fim = int(input("Digite o segundo numero: "))
intervalo = int(input("Digite o intervalo: "))

print(list(range(inicio,fim,intervalo)))

#exercicio 3
print(list(range(10,0,-1)))

#exercicio 4
print(list(range(0,101,2)))

#exercicio 5
a = int(0)
for i in range(0, 101):
    if i % 2 == 0:
        a += 1

print(a)

#exercicio 6
for i in range(0, 101):
    for j in range(i-1, 0, -1):
        if i % j == 0:#
            break
        if i % j > 0:
            if j == 2:
                print(i)
        if i == j:
            print(i)

#exercicio 7
inicio = int(input("Digite um numero: "))
fim = int(input("Digite outro numero: "))
intervalo = int(input("Digite o intervalo: "))

for i in range(inicio, fim, intervalo):
    for j in range(i-1, 0, -1):
        if i % j == 0:
            break
        if i % j > 0:
            if j == 2:
                print(i)
        if i == j:
            print(i)

#exercicio 8
inicio = int(input("Digite um numero: "))
fim = int(input("Digite outro numero: "))
intervalo = int(input("Digite o intervalo: "))

n1 = int(input("Primeiro numero a ser ignorado: "))
n2 = int(input("Segundo numero a ser ignorado: "))
n3 = int(input("Terceiro numero a ser ignorado: "))

for i in range(inicio, fim, intervalo):
    if n1 == i or n2 == i or n3 == i:
        continue
    else:
        print(i)

#exercicio 9
a=False
while(a != True):
    letra = input("estou em looping! ")
    if(letra == "q"):
        a=True