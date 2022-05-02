from ast import keyword
import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário 
    representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_de_categorias_construcao = []
    for produto in dados:
        categoria = produto["categoria"]
        lista_de_categorias_construcao.append(categoria)
    
    lista_de_categorias = []           
    for categorias in lista_de_categorias_construcao:
        if categorias not in lista_de_categorias:
            lista_de_categorias.append(categorias)
    
    return lista_de_categorias


def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista_produtos_por_categoria = []
    
    for produto in dados:
        if categoria == produto['categoria']:
            lista_produtos_por_categoria.append(produto['id'])
    return lista_produtos_por_categoria  
        

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_caros = []
    lista_precos = []
    for produto in dados:
        if categoria == produto['categoria']:
            lista_caros.append(produto['preco'])
            lista_caros.append(produto['id'])
            lista_precos.append(float(produto['preco']))
    mais_caro = max(lista_precos)
                
    return mais_caro


def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_caros = []
    lista_precos = []
    for produto in dados:
        if categoria == produto['categoria']:
            lista_caros.append(produto['preco'])
            lista_caros.append(produto['id'])
            lista_precos.append(float(produto['preco']))
    mais_barato = min(lista_precos)
                
    return mais_barato

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista_geral_precos = []
    lista_precos = []
    
    for produto in dados:
        lista_geral_precos.append(float(produto['preco']))
    lista_geral_precos.sort()
    lista_geral_precos.reverse()
    for produto in range(10):
        lista_precos.append(str(lista_geral_precos[produto]))
        
    return lista_precos


def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    
    lista_geral_precos = []
    lista_precos = []
    
    for produto in dados:
        lista_geral_precos.append(float(produto['preco']))
    lista_geral_precos.sort()
    
    for produto in range(10):
        lista_precos.append(str(lista_geral_precos[produto]))
        
    return lista_precos

def menu(dados):

    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    mensagem = '\n1. Listar Categorias \n2. Listar produtos de uma categoria \n3. Produto mais caro por categoria \n4. Produto mais barato por categoria \n5. Top 10 produtos mais caros \n6. Top 10 produtos mais baratos \n0. Sair \n'
    opcao = int(input(mensagem))
    while opcao != 0:
        if opcao == 1:
            print(listar_categorias(dados))
        elif opcao == 2:
            categoria = input('Informe a categoria desejada: ')
            print(listar_por_categoria(dados, categoria))
        elif opcao == 3:
            categoria = input('Informe a categoria desejada: ')
            print(produto_mais_caro(dados, categoria))
        elif opcao == 4:
            categoria = input('Informe a categoria desejada: ')
            print(produto_mais_barato(dados, categoria))
        elif opcao == 5:
            print(top_10_caros(dados))
        elif opcao == 6:
            print(top_10_baratos(dados))
        elif opcao == 0:
            print('fim do programa')
        else:
            print('Opção errada, por favor, escolha uma das opções a seguir:')

        opcao = int(input(mensagem))
        
    print('Fim do programa')
        
            

# Programa Principal - não modificar!
d = obter_dados()
menu(d)
