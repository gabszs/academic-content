from math import (sqrt, log, pow)
from random import randint



#Exercicio1
#le dois numero e descobre qual e o m

'''n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O primeiro número e o maior')
else:
    print(f'O segundo número e o maior')'''

#Exercicio2
#calcula a raiz quadrada se o número digitado for positivo senao printa erro

'''n1 = int(input('Número: '))
if n1 > 0:
    print(f'A raiz quadrada de {n1} é {sqrt(n1)}')
else:
    print('Número invalido')'''

#Exercicio3
#le um número real se for positivo ele faz a raiz quadrada, senão eleva ao quadrado

'''n1 = float(input('Número: '))
if n1 > 0:
    print(f'A raiz quadrada de {n1} é {sqrt(n1)}')
else:
    print(f'O número {n1} elavado ao quadrado é: {n1**2}')'''

#Exercicio4
#le um numero e se ele for positivo calcula a raiz e printa o numero e depois a raiz

'''n1 = int(input('Número: '))
if n1 > 0:
    print(n1)
    print(sqrt(n1))'''

#Exercicio5
#Recebe um inteiro e checa para ver se ele é par ou impar

'''n1 = int(input('Número: '))
if n1 % 2 == 0:
    print('Ele e par')
else:
    print('Ele é impar')'''

#Exercicio6
#le dois numeros, e mostra a diferença entre eles

'''n1 = int(input('1 número: '))
n2 = int(input('2 número: '))
if n1 > n2:
    print(f'O número {n1} é maior que {n2}, e a diferença é de {n1 - n2}')
else:
    print(f'O número {n2} é maior que {n1}, e a diferença é de {n2 - n1}')'''

#Exercicio7
#le dois numeros, mostra qual e o maior, e se forem iguais mostra tbm

'''n1 = int(input('1 Número: '))
n2 = int(input('2 Número: '))
if n1 > n2:
    print(f'O primeiro número e o maior')
elif n1 == n2:
    print(f'O números são iguais')
else:
    print(f'O segundo número é igual')'''

#Exercicio8
#le duas notas para calcular a média, se nao for entre 0 e 10, ele da erro

'''n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
if (n1 >= 0 and n1 <= 10) and (n2 >= 0 and n2 <= 10):
    print(f'A média do aluno é {(n1+n2)/2}')
else:
    print('ERRO')'''

#Exercicio9
#o salario e o valor da prestação, se a prestação for 20% maior que o salario ela não autoriza

'''n1 = int(input('salario: '))
n2 = int(input('Prestação: '))
if (n1 * 0.2) >= n2:
    print('Emprestimo concedido')
else:
    print('Emprestimo negado')'''

#Exercicio10
#recebe peso e altura e calcula o peso ideal

'''peso = float(input('Peso: '))
altura = float(input('Altura: '))

if ((72.7 * altura) - 58) != peso and ((62.1*altura) - 44.7) != peso:
    print(f'Você esta fora do peso ideal')
else:
    print('Voces dentro do peso ideal')'''

#Exercicio11
#le um numero, se ele for maior que zero ele vai somar todos os algarismos do numero

'''soma = 0
num = int(input('Numero: '))
if num > 0:
    for c in str(num):
        soma += int(c)
    print(soma)'''

#Exercicio12
#le um numero, se for negativo printa numero invalido, senao printa o logartimo do numero

'''num = int(input('Número: '))
if num < 0:
    print(f'Número invalido')
else:
    print(f'O logartimo de {num} é {log(num):.2f}')'''

#Exercicio13
#Le 3 notas e da a média ponderada

'''n1 = float(input('1 Nota: '))
n2 = float(input('2 Nota: '))
n3 = float(input('3 Nota: '))
media = ((n1 * 1) + (n2 * 1) + (n3 * 2))/4
print(media)
if media >= 60:
    print(f'O aluno foi aprovado')
else:
    print(f'O aluno foi reprovado')'''

#Exercicio14
#inputa as notas com pesos diferente do trabalho e avaliações e calcula e media e mostra se ele esta reprovado, recuperação ou passou

'''trabalho = float(input('Trabalho: '))
prova = float(input('Prova: '))
exame = float(input('Exame: '))
media = ((trabalho * 2) + (prova * 3) + (exame * 5))/10
if media < 3:
    print('O aluno foi reprovado')
elif media > 3 and media < 5:
    print('O aluno esta de recuperação')
else:
    print('O aluno passou')'''

#Exercicio15
#


#Exercicio16
#


#Exercicio17
#le a vase maior e menor de um trapezio e calcula, porem as bases tem de ser maiores que 0

'''base1 = float(input('Base1: '))
base2 = float(input('Base2: '))
altura = float(input('Altura: '))
print(((base2 + base1) * altura)/2) if base1 > 0 and base2 > 0 else print('Numero da base tem de serem maiores que zero')'''

#Exercicio18
#inputa um numero, ele devera escolher uma opeação matematica

'''num = int(input('Digite um numero de 1 a 4: '))
if num == 1:
    n1 = float(input('1 numero: '))
    n2 = float(input('2 numero: '))
    print(n1 + n2)

elif num == 2:
    n1 = float(input('1 numero: '))
    n2 = float(input('2 numero: '))
    print(n1 * n2)
elif num == 3:
    n1 = float(input('1 numero: '))
    n2 = float(input('2 numero: '))
    print(n1 - n2)
elif num == 4:
    n1 = float(input('1 numero: '))
    n2 = float(input('2 numero: '))
    print(n1 / n2) if n2 != 0 else print('Base igual a zero, erro')
else:
    print('Um numero fora do range foi digitado, tente novamente')'''

#Exercicio19
#checa se um numero e divisivel por 3 ou por 5, mas nao por ambos ao mesmo tempo

'''n1 = int(input('Numero: '))


if n1 % 3 == 0:
    if n1 % 5 != 0:
        print(n1)
elif n1 % 5 == 0:
    if n1 % 3 != 0:
        print(n1)
elif n1 % 3 == 0 and n1 % 5 == 0:
    print('Valor desconsiderado')
else:
    print('Número e par')'''

#Exercicio20
#calcula o triangulo

'''Lado1 = float(input('Digite o primeiro lado: '))
Lado2 = float(input('Digite o segundo lado: '))
Lado3 = float(input('Digite o terceiro lado: '))

if (Lado1 + Lado2 > Lado3) and (Lado3 + Lado2 > Lado1) and (Lado3 + Lado1 > Lado2):
    if Lado2 == Lado1 and Lado1 == Lado3:
        print('O triangulo é Equilátero!!')
    elif (Lado1 == Lado2 and Lado1 != Lado3) or (Lado2 == Lado3 and Lado2 != Lado1) or (Lado1 == Lado3 and Lado1 != Lado2):
        print('O triangulo é isoceles')
    else:
        print('O triangulo é escaleno')
else:
    print('Os lados inseridos não formam um triangulo')'''

#Exercicio21
#mes coisa do 18 so que com upgrades

'''num = int(input('Digite um numero de 1 a 4: '))
if num == 1:
    n1 = float(input('1 numero: '))
    n2 = float(input('2 numero: '))
    print(n1 + n2) 

elif num == 2:
    n1 = float(input('1 numero: '))
    n2 = float(input('2 numero: '))
    print(n1 * n2)
elif num == 3:
    n1 = float(input('1 numero: '))
    n2 = float(input('2 numero: '))
    print(n1 - n2) if n1 > n2 else print(n2 - n1)
elif num == 4:
    n1 = float(input('1 numero: '))
    n2 = float(input('2 numero: '))
    print(n1 / n2) if n2 != 0 else print('Base igual a zero, erro')
else:
    print('Um numero fora do range foi digitado, tente novamente')'''


#Exercicio22
#calcula se pode aposentar ou nao

'''idade = int(input('Idade: '))
trab = int(input('Trablho: '))
if idade >= 65:
    print('Ja pode ser aposentar')
elif trab >= 30:
    print('Ja pode ser aposentar')
elif idade >= 60 and trab >= 25:
    print('Ja pode ser aposentar')
else:
    print('Não pode se aposentar ainda')'''

#Exercicio23

'''n1 = int(input('Digite o ano: '))

if (n1 % 4) == 0 and (n1 % 400) == 0:
    print(f'O ano é bissexto')
elif (n1 % 4) == 0 and (n1 % 100) == 0 and (n1 % 400) == 0:
    print(f'O ano {n1} é bissexto')
else:
    print(f'O ano não é bissexto')'''


#Exercicio24
#Calcula o valor do produto com imposto de acordo com o estado (SP, MG, RJ, MS)

'''valor = float(input('Valor: '))
estado = input('Digite o estado: ').upper()

if estado == 'MG':
    print(f'O valor total do produto com o acrescimo de 7% de imposto é R$: {valor * 1.07}')
elif estado == 'SP':
    print(f'O valor total do produto com o acrescimo de 12% de imposto é R$: {valor * 1.12}')
elif estado == 'RJ':
    print(f'O valor total do produto com o acrescimo de 15% de imposto é R$: {valor * 1.15}')
elif estado == 'MS':
    print(f'O valor total do produto com o acrescimo de 8% de imposto é R$: {valor * 1.08}')
else:
    print('Sigla do estado não reconhecida')'''

#Exercicio25
#Calcula a raiz de de uma equação de segundo grau

'''a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
x = (-b - (sqrt((b**2)- 4 * a * c))) / 2 * a
x1 = (-b + (sqrt((b**2)- 4 * a * c))) / 2 * a
print(x)
print(x1)'''

#Exercicio26
#calcula o gasto de gasolina e indica o potencial do carro

'''gasolina = float(input('Gasolina: '))
km = int(input('Kilometros: '))
km_litro = km / gasolina

if km_litro >= 0:
    if km_litro < 8:
        print('Venda o carro')
    elif km_litro >= 8 and km_litro <= 14:
        if km_litro > 12:
            print('Super economico')
        else:
            print('Economico')'''

#Exercicio27
#classifica o nadador de acordo com a idade

'''idade = int(input('Idade: '))

if idade >= 5 and idade <= 7:
    print('Infantil A')
elif idade >= 8 and idade <= 10:
    print('Infantil B')
elif idade >= 11 and idade <= 13:
    print('Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Juvenil B')
elif idade < 5:
    print('Ilegivel')
else:
    print('Senior')'''

#Exercicio28
#calcula diferentes tipos de media de acordo com com a que o usuario preferir

'''choice = input('Qual média quer: ').upper()

if choice == 'A':
    x = int(input('X: '))
    y = int(input('Y: '))
    z = int(input('Z: '))
    media_geo = (x * y * z)**(1/3)
    print(media_geo)
elif choice == 'B':
    x = int(input('X: '))
    y = int(input('Y: '))
    z = int(input('Z: '))
    media_pond = (x + (2 * y) + (2 * z))/6
    print(media_pond)
elif choice == 'C':
    x = int(input('X: '))
    y = int(input('Y: '))
    z = int(input('Z: '))
    media_harmonica = 1 / ((1/x) + (1/y) + (1/z))
    print(media_harmonica)
elif choice == 'D':
    x = int(input('X: '))
    y = int(input('Y: '))
    z = int(input('Z: '))
    media_arit = (x + y + z) / 3
    print(media_arit)
else:
    print('O valor informado não esta de acordo com as opções')'''

#Exercicio29
#Vai gerar perguntas com dois numeros inteiros abaixo de 100 para soma, se crianca acerta conta ponto, e mostra a reposta

'''cont = 0
print('Prova escolar')
for c in range(1,6):
    n1 = randint(0,100)
    n2 = randint(0,100)
    gab = n1 + n2
    result = int(input(f'Qual o resultado da soma de {n1} + {n2}? '))
    if (n1 + n2) == result:
        cont += 1
    print(gab)
print(cont)'''

#Exercicio30
#le 3 numeros e imprime eles em ordem crescente

'''n1 = int(input('1 numero: '))
n2 = int(input('2 numero: '))
n3 = int(input('3 numero: '))
lst = [n1, n2, n3]
lst = sorted(lst)
for c in lst:
    print(c, end=' ')'''

#Exercicio31
#recebe a altura e peso e descobre a classificação de acordo com a tabela informada no pdf

'''altura = int(input('Altura: '))
peso = int(input('Peso: '))

if peso < 60:
    if altura < 1.2:
        print('A')
    elif altura >= 1.2 and altura <= 1.7:
        print('B')
    else:
        print('c')
if peso >= 60 and altura <= 90:
    if altura < 1.2:
        print('A')
    elif altura >= 1.2 and altura <= 1.7:
        print('B')
    else:
        print('c')
if peso > 90:
    if altura < 1.2:
        print('A')
    elif altura >= 1.2 and altura <= 1.7:
        print('B')
    else:
        print('c')'''

#Exercicio32
#de acordo com o codigo informado ele puxa o valor e calcula o pedido

'''dct = {100: 1.2, 101: 1.3, 102: 1.5, 103: 1.2, 104: 1.7, 105: 2.2, 106: 1}
prod = int(input('Produto: '))
qtd = int(input('Quantidade: '))

if prod == 100:
    print(qtd * 1.2)
elif prod == 101:
    print(qtd * 1.3)
elif prod == 102:
    print(qtd * 1.5)
elif prod == 103:
    print(qtd * 1.3)
elif prod == 104:
    print(qtd * 1.7)
elif prod == 105:
    print(qtd * 2.2)
elif prod == 106:
    print(qtd * 1)
else:
    print('Numero digitado, esta fora do range')'''

#Exercicio33
#aumenta o vlaor do produto de acordo com a tabela, e de acordo com o preõ da um preço

'''valor = float(input('Valor: '))
if valor < 50:
    valor *= 1.05
elif valor >= 50 and valor <= 100:
    valor *= 1.1
elif valor > 100:
    valor *= 1.15
elif valor < 0:
    print('Número imcopativel')

if valor <= 80:
    print('Barato')
elif valor >= 80 and valor < 120:
    print('Normal')
elif valor >= 120 and valor <= 200:
    print('Caro')
else:
    print('Muito caro')'''

#Exercicio34
#le a nota e de acordo com o as faltas da uma classificação ao aluno

'''nota = int(input('Nota: '))
faltas = int(input('Faltas: '))

if nota < 4:
    if faltas < 20:
        print('E')
    else:
        print('E')
elif nota >= 4 and nota < 5:
    if faltas < 20:
        print('D')
    else:
        print('E')
elif nota >= 5 and nota < 7.5:
    if faltas < 20:
        print('C')
    else:
        print('D')
elif nota >= 7.5 and nota < 9:
    if faltas < 20:
        print('B')
    else:
        print('C')
elif nota >= 9 and nota <= 10 :
    if faltas < 20:
        print('A')
    else:
        print('B')
else:
    print('Numero invalido digitado')'''

#Exercicio35
#le uma data e checa se ela esta e valida dentro dos ranges de data

'''mes = int(input('Mês: '))

if mes >= 1 and mes <= 12:
    dia = int(input('Idade: '))
    if mes == 2:
        if dia >= 1 and dia <= 29:
            print('Data validada')
        else:
            print(f'Dia em fevereiro invalido')
    elif dia <= 31 and dia >= 1:
        print('Data validada')
    else:
        print('Dia invalido')'''


#Exercicio36
# quanto maior a venda  maior a comição

'''venda = int(input('Venda: '))

if venda >= 100000:
    print(f'Comição: R${700 + venda * 1.16}')

elif venda < 100000 and venda >= 80000:
    print(f'Comição: R${650 + venda * 1.14}')

elif venda < 80000 and venda >= 60000:
    print(f'Comição: R${600 + venda * 1.14}')

elif venda < 60000 and venda >= 40000:
    print(f'Comição: R${550 + venda * 1.14}')

elif venda < 40000 and venda >= 20000:
    print(f'Comição: R${500 + venda * 1.14}')

elif venda < 20000:
    print(f'Comição: R${400 + venda * 1.14}')'''


#Exercicio37
#
'''lst = [c for c in range(0,7)]

st = {c: c for c in range(0,7)}
print(st)
print(type(st))'''

#Exercicio38
#


#Exercicio39
#


#Exercicio40
#


#Exercicio41
#

