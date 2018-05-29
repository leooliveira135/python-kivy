# exercicio 1
def estudo():
    print('Estamos estudando as funções')


estudo()


# exercicio 2
def estudo(x):
    print('Função invocada com sucesso. O valor passado pelo argumento x é:', x)


estudo(1)


# exercicio 3
def soma(x, y):
    somar = x + y
    print('A soma de', x, 'mais', y, 'é:', somar)


soma(1, 2)


# exercicio 4
def resultado(x, y, z):
    lista = [x, y, z]
    print('Ordenação:', sorted(lista))
    media = (x + y + z) / 3
    print('Média aritmética:', media)


resultado(2, 0, 1)


# exercicio 5
def soma(x, y=0):
    print('A soma de', x, 'mais', y, 'é:', {x + y})


soma(10, 5)


# exercicio 6
def func1():
    def func2(x, y):
        somar = x + y
        return somar

    retorno = func2(1, 2)
    print(retorno)


func1()


# exercicio 7
def variavel(*x):
    print(x)


variavel(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


# exercicio 8
def variavel_cv(**x):
    print(x)


variavel_cv(a='1', b='2', c='3', d='4', e='5', f='6', g='7')


# exercicio 9
def func(a, b, c, d):
    print(a + b + c + d)


lista = 1, 2, 3, 4
func(*lista)


# exercicio 10
def maior(a, b, c):
    if a > b and a > c:
        print("Maior número:", a)
    elif b > c:
        print("Maior número:", b)
    else:
        print("Maior número:", c)


maior(1, 7, 4)
maior(3, 2, 10)


# exercicio 11
def somar_l(*x):
    print(sum(x))


lista = 1, 2, 3, 4, 5
somar_l(*lista)

# exercicio 12
lista = [1, 2, 3, 4, 5]


def multi_l(*x):
    t = 1
    for x in lista:
        t *= x
    print(t)


multi_l(*lista)


# exercicio 13
def inverter(*txt):
    for x in range(len(txt) - 1, -1, -1):
        print(txt[x])


lista = "1234abcd"
inverter(*lista)


# exercicio 14
def fatorial(x):
    c = x
    if x <= 0:
        print("Não é possível obter fatorial deste número")
    else:
        for x in range(x - 1, 0, -1):
            c *= x
        print(int(c))


fatorial(30)
fatorial(-2)


# exercicio 15
def range_determinado(inicio, fim, num):
    if inicio <= num and fim >= num:
        print("O", num, "está no intervalo entre", inicio, "e", fim)
    else:
        print("O", num, "não está no intervalo entre", inicio, "e", fim)


range_determinado(1, 10, 5)
range_determinado(1, 10, 12)


# exercicio 16
def contarLetra(txt):
    l_min = 0
    L_max = 0
    for x in txt:
        if x == txt.upper():
            L_max += 1
        else:
            l_min += 1
    print(f'Maiúsculas:{L_max}\nMinúsculas:{l_min}')


p = str(input('Palavra:'))
contarLetra(p)


# exercicio 17
def repetido(*lista):
    l = []
    for item in lista:
        if item not in l:
            l.append(item)
    print(l)


lista = 10, 10, 23, 30, 32, 32, 40
repetido(*lista)


# exercicio 18
def num_primos(numero):
    c = 0
    for x in range(1, numero + 1):
        if numero % x == 0:
            c += 1
    if c == 2:
        print(numero, "é primo")
    else:
        print(numero, "não é primo")


num_primos(34)
num_primos(13)


# exercicio 19
def imprime_par(*lista):
    for x in lista:
        if x % 2 == 0:
            print(x)


lista = 1, 2, 3, 4, 5, 6, 7, 8, 9
imprime_par(*lista)


# exercicio 20
def palindromo(frase):
    p = frase.upper().split()
    j = ''.join(p)
    i = j[::-1]

    print('A frase', j, 'ao contrário fica', i)

    if i == j:
        print("A frase é um palíndromo")
    else:
        print("A frase não é um palíndromo")


palindromo("Roma me tem amor")
palindromo("Ás de espadas")

# exercicio 21
def mostrar_num():
    def func_anin():
        print(10)
    func_anin()
    pass

print(mostrar_num())