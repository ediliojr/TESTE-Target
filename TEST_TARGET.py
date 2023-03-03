# // 1) Observe o trecho de código abaixo:

# // int INDICE = 13, SOMA = 0, K = 0;

# // enquanto K < INDICE faça
# // {
# // K = K + 1;
# // SOMA = SOMA + K;
# // }

# // imprimir(SOMA);

# // Ao final do processamento, qual será o valor da variável SOMA?
print("*{:-^90}*".format("QUESTÃO 1 :"),"\n")
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

# -------------RESULTADO QUESTÃO 1 : SOMA = 91 ---------------

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)
# , escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
# pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
print("*{:-^90}*".format("QUESTÃO 2 :"),"\n")
numero = int(input("Informe um número: "))
a = 0
b = 1

while b <= numero:
    if b == numero:
        print("O número informado pertence à sequência de Fibonacci!")
        break
    c = a + b
    a = b
    b = c
else:
    print("O número informado não pertence à sequência de Fibonacci.")



# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
print("*{:-^90}*".format("QUESTÃO 3 :"),"\n")
import json

# Lendo os dados do arquivo JSON
with open('dados.json') as f:
    dados = json.load(f)

# Extraindo os valores do faturamento diário do JSON
faturamento_diario = [dia['valor'] for dia in dados]

# Calculando o menor valor de faturamento diário
menor_faturamento = min(faturamento_diario)

# Calculando o maior valor de faturamento diário
maior_faturamento = max(faturamento_diario)

# Calculando a média mensal de faturamento diário
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Calculando o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_media = sum(faturamento > media_mensal for faturamento in faturamento_diario)

# Imprimindo os resultados
print(f"Menor faturamento diário: {menor_faturamento}")
print(f"Maior faturamento diário: {maior_faturamento}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")



# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
print("*{:-^90}*".format("QUESTÃO 4 :"),"\n")
sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
out = float(19849.53)
total = float(sp + rj + mg + es + out)
print("TOTAL=",total)
psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
pout = ((out/total)*100)

print('Porcentagem de SP {}'.format(psp))
print('Porcentagem de RJ {}'.format(prj))
print('Porcentagem de MG {}'.format(pmg))
print('Porcentagem de ES {}'.format(pes))
print('Porcentagem de OUT {}'.format(pout))

# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;
print("*{:-^90}*".format("QUESTÃO 5 :"),"\n")


string = input("Digite a string a ser invertida: ")

# Convertendo a string em uma lista de caracteres
lista_caracteres = []
for caractere in string:
    lista_caracteres.append(caractere)

# Invertendo a ordem dos caracteres na lista
for i in range(len(lista_caracteres) // 2):
    lista_caracteres[i], lista_caracteres[-i-1] = lista_caracteres[-i-1], lista_caracteres[i]

# Convertendo a lista de caracteres de volta para uma string
string_invertida = ""
for caractere in lista_caracteres:
    string_invertida += caractere

# Exibindo a string invertida
print("String invertida:", string_invertida)