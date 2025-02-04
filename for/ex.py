"""
# Exercícios

## 1. Criando um Registro de Hóspedes

Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:
"""

# hospedes = []
# qtdhospede = int(input('Olá,quantos hospedes será hospedado? '))
# for i in range(qtdhospede):
#     nome = str(input('Nome: '))
#     cpf = str(input('CPF: '))
#     lista = [nome,cpf]
#     print('-----')
#     hospedes.append(lista)
 


# print('-----')

# for index,item in enumerate(hospedes):
#     print(f'N°{index} quarto ,esta o hospede {item[0]} com o cpf {item[1]}')






"""
    ## 2. Análise de Vendas

    Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.

    Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.
  

"""

# meta = 10000
# vendas = [
#         ['João', 15000],
#         ['Julia', 27000],
#         ['Marcus', 9900],
#         ['Maria', 3750],
#         ['Ana', 10300],
#         ['Alon', 7870],
# ]

# for item in vendas:
#     if item[1] >= meta:
#         print(f'{item[0]} bateu a meta, vendendo {item[1]}')
#     else:
#           print(f'{item[0]} Não bateu a meta, vendendo {item[1]}')




"""
    ## 3. Comparação com Ano Anterior

    Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

    Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.

    Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)

    Dica: lembre do enumerate, ele pode facilitar seu "for"
"""


# produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
# vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
# vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]


# for index,item in enumerate(produtos):
#     if  vendas2020[index] > vendas2019[index]:
#         porcentagem = vendas2020[index] / vendas2019[index] - 1
#         print(f'O ano de 2020 vendeu R${vendas2020[index]:,} teve uma porcentagem de {porcentagem:.1%} no produto {item},em relação ao ano de 2019 que vendeu {vendas2019[index]:,}')
#     else:
#         porcentagem = vendas2020[index] / vendas2019[index] - 1
#         print(f'O ano de 2020 vendeu R${vendas2020[index]:,} teve uma porcentagem de {porcentagem:.1%} no produto {item},em relação ao ano de 2019 que vendeu {vendas2019[index]:,}')
    


"""
    # Exercícios

    ## 4. Calculando % de uma lista

    Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

    Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.
"""

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]    
totalvendedores = len(vendas)
acimameta = []
for item in vendas:
    if item[1] > meta:
       acimameta.append(item)

total = len(acimameta) / totalvendedores
print(f'{total:.0%} vendedores bateram a meta , que corresponde  do total {totalvendedores}')