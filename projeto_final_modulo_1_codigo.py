import datetime
import csv
from functools import reduce

produtos = []
vendas = [['data', 'hora', 'id', 'nome', 'marca', 'quantidade', 'preco', 'valor total']]


# Funções relacionadas à experiência do usuário
def titulo(msg): # Gera um título a partir de uma mensagem passada como parâmetro
    print('=' * 50)
    print(f'{msg:^49}')
    print('=' * 50)

def linha(): # Linha utilizada como elemento visual em alguns momentos do código
    print('-' * 50)

def menu(): # Menu principal
    titulo('MENU')
    print("""Opções disponiveis:

    1) Cadastrar novo produto no sistema
    2) Atualizar dados de um produto
    3) Excluir um produto do sistema
    4) Realizar uma venda
    5) Visualizar produtos cadastrados no sistema
    6) Sair""")

# Funções de manipulação de dados
def atributo_produto(arg): # Coleta os atributos de um produto de acordo com o parâmetro passado
    if arg == 'identificador':
        while True:
            try:
                identificador = str(input('Digite o identificador do produto (5 números inteiros): '))
                if len(identificador) != 5:
                    raise ValueError
                elif identificador.isnumeric() != True:
                    raise TypeError
            except TypeError as e:
                print('\nOps! O identificador deve ser um número inteiro de 5 dígitos... Tente novamente.')
            except ValueError as e:
                print('\nOps! O identificador deve ser um número inteiro de 5 dígitos... Tente novamente.')
            except:
                print('\nOps! Ocorreu um erro inesperado... Tente novamente.')
            else:
                break
        return identificador

    elif arg == 'nome':
        while True:
            try:
                nome = str(input('Nome do produto: ')).lower().strip()
                if nome == '':
                    raise ValueError
            except ValueError:
                print('\nOps! O campo "nome" não pode ser vazio... Tente novamente.')
            except:
                print('\nOps! Ocorreu um erro inesperado... Tente novamente.')
            else:
                break
        return nome

    elif arg == 'marca':
        while True:
            try:
                marca = str(input('Marca do produto: ')).lower().strip()
                if marca == '':
                    raise ValueError
            except ValueError:
                print('\nOps! O campo "marca" não pode ser vazio... Tente novamente.')
            except:
                print('\nOps! Ocorreu um erro inesperado... Tente novamente.')
            else:
                break
        return marca

    elif arg == 'preco':
        while True:
            try:
                preco = str(input('Preço do produto (Digite apenas o valor): R$'))
                if ',' in preco:
                    preco = preco.replace(',', '.')
                preco = float(preco)
            except ValueError as e:
                print('\nOps! O preço do produto não pode conter letras... Tente novamente.')
            except:
                print('\nOps! Ocorreu um erro inesperado... Tente novamente.')
            else:
                break
        return preco

    elif arg == 'estoque':
        while True:
            try:
                estoque = int(input('Quantidade em estoque (número inteiro): '))
            except TypeError as e:
                print('\nOps! O estoque do produto não pode conter letras... Tente novamente.')
            except ValueError as e:
                print('\nOps! O estoque do produto deve ser um valor inteiro... Tente novamente.')
            except:
                print('\nOps! Ocorreu um erro inesperado... Tente novamente.')
            else:
                break
        return estoque

    elif arg == 'descricao':
        while True:
            try:
                descricao = str(input(f'Descrição (Aperte ENTER direto para "sem descrição"): ')).lower().strip()
                if descricao == '':
                    descricao = 'sem descricao'
            except:
                print('\nOps! Ocorreu um erro inesperado... Tente novamente.')
            else:
                break
        return descricao

    elif arg == 'quantidade':
        while True:
            try:
                quantidade = int(input('\nDigite quantas unidades desse produto serão vendidas: '))
            except:
                print('\nOps! A quantidade precisa ser um número inteiro... Tente novamente.')
            else:
                break
        return quantidade

def verificador(identificador): # Verifica se o identificador passado pelo usuário está cadastrado no sistema
    lista_indexador = list(map(lambda produto: identificador in produto.keys(), produtos))
    return lista_indexador

def viz_dados_produto(identificador): # Visualiza os dados de um produto específico, de acordo com o seu identificador
    linha()
    for produto in produtos:
        for key, value in produto.items():
            if identificador == key:
                for key2, value2 in value.items():
                    print(f'{key2}: {value2}')
                linha()

def viz_dados_produtos(): # Visualiza os dados de todos os produtos que estão cadastrados no sistema
    if not produtos:
        print("\nNão há produtos cadastrados.")
        return
    titulo("PRODUTOS CADASTRADOS")
    linha()
    for produto in produtos:
        for key, value in produto.items():
            print(f'id : {key}')
            for key2, value2 in value.items():
                print(f'{key2}: {value2}')
            linha()

# Funções relacionadas ao funcionamento do sistema
def cadastrar(): # Cadastra um produto no sistema
    titulo('CADASTRAR PRODUTO')
    dicionario_principal = {}
    identificador = atributo_produto('identificador')
    verificacao = verificador(identificador)
    if True in verificacao:
        print('\nOps! Esse identificador já foi cadastrado para outro produto... Tente novamente.')
    else:
        produto = {'nome': atributo_produto('nome'),
                   'marca': atributo_produto('marca'),
                   'preco': atributo_produto('preco'),
                   'estoque': atributo_produto('estoque'),
                   'descricao': atributo_produto('descricao')}

        dicionario_principal = {identificador: produto}
        linha()
        print('Dados do produto adicionado:')
        print()
        for k in dicionario_principal.keys():
            print(f'id: {k}')
            for i, j in dicionario_principal[k].items():
                print(f'{i}: {j}')
        linha()
        produtos.append(dicionario_principal)
        print((f'O produto {produto["nome"]} foi cadastrado com sucesso!'))

def atualizar(): # Atualiza os dados de um produto já cadastrado
    titulo('ATUALIZAR PRODUTO')
    identificador = atributo_produto('identificador')
    verificacao = verificador(identificador)
    if True in verificacao:
        for produto in produtos:
            for chave, valor in produto.items():
                if identificador == chave:
                    print(f'id: {chave}')
                    for chave2, valor2 in valor.items():
                        print(f'{chave2}: {valor2}')
                    
                    while True:
                        linha()
                        print('''O que deseja fazer?

1) Atualizar todos os dados do produto
2) Atualizar um campo específico
3) Cancelar atualização''')
                        linha()
                        opcao = str(input('\nDigite a sua opção: '))
                        print()
                        if opcao == '1':
                        
                            valor['nome'] = atributo_produto('nome')
                            valor['marca'] = atributo_produto('marca')
                            valor['preco'] = atributo_produto('preco')
                            valor['estoque'] = atributo_produto('estoque')
                            valor['descricao'] = atributo_produto('descricao')
                            linha()
                            print('\nProduto atualizado com sucesso!')
                            print()
                        elif opcao == '2':
                            print('''\nQual elemento deseja atualizar?
                            

1) Nome
2) Marca
3) Preço
4) Estoque
5) Descrição''')
                            linha()
                            while True:
                                dado = str(input('\nDigite o número do dado que quer atualizar: '))
                                print()                         
                                if dado == '1':
                                    valor['nome'] = atributo_produto('nome')
                                    break
                                elif dado == '2':
                                    valor['marca'] = atributo_produto('marca')
                                    break
                                elif dado == '3':
                                    valor['preco'] = atributo_produto('preco')
                                    break
                                elif dado == '4':
                                    valor['estoque'] = atributo_produto('estoque')
                                    break
                                elif dado == '5':
                                    valor['descricao'] = atributo_produto('descricao')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                            print('\nProduto atualizado com sucesso!')
                            break
                        elif opcao == '3':
                            print('Ação cancelada.')
                            break
                        else:
                            print('\nOpção inválida. Digite um dos números do menu.')
        viz_dados_produto(identificador)
    else:
        print('\nOps! Não existe nenhum produto cadastrado com esse identificador. Tente realizar um novo cadastro.')

def excluir(): # Exclui um produto que foi cadastrado previamente no sistema
    titulo('EXCLUIR PRODUTO')
    identificador = atributo_produto('identificador')
    verificacao = verificador(identificador)
    if True in verificacao:
        viz_dados_produto(identificador)
        print('''Tem certeza que deseja excluir este produto?

1) Excluir produto
2) Cancelar exclusão''')

        while True:
            escolha = str(input('\nDigite o número da sua escolha de acordo com o menu: '))
            if escolha == '1':
                lista_indexador = list(map(lambda produto: identificador in produto.keys(), produtos))
                for i in range(len(lista_indexador)):
                    if lista_indexador[i] == True:
                        indexador = i
                produtos.pop(indexador)
                print('\nProduto excluído com sucesso!')
                break
            elif escolha == '2':
                print('\nExclusão cancelada.')
                break
            else:
                print('\nOps! Parece que você digitou um valor inválido... Tente novamente.')

def cadastrar_venda(): # Faz o cadastro de um item para que posteriormente seja vendido
    venda = []
    identificador = atributo_produto('identificador')
    verificacao = verificador(identificador)
    if True in verificacao:
        quantidade = atributo_produto('quantidade')
        for produto in produtos:
            for k, v in produto.items():
                if k == identificador and v['estoque'] >= quantidade:
                    nome = v.get('nome')
                    marca = v.get('marca')
                    preco = v.get('preco')
                    total = preco * quantidade
                    venda.append(identificador)
                    venda.append(nome)
                    venda.append(marca)
                    venda.append(quantidade)
                    venda.append(preco)
                    venda.append(total)
                    v['estoque'] -= quantidade
                    return venda
                elif k == identificador and v['estoque'] < quantidade:
                    print('\nOps! Parece que o estoque não é suficiente para essa venda...')

def executar_venda(): # Executa a ordem de venda e retorna o valor total da compra
    carrinho = []
    while True:
        titulo('EXECUTAR VENDA')
        print('''Escolha uma opção:
1) Acrescentar item ao carrinho
2) Remover item do carrinho
3) Visualizar carrinho
4) Encerrar venda (Cancelar se o carrinho estiver vazio)
''')
        escolha = str(input('\nDigite sua escolha: '))
        if escolha == '1':
            print('Produtos disponíveis:')
            viz_dados_produtos()
            venda = cadastrar_venda()
            if venda is not None:
                carrinho.append(venda)
        elif escolha == '2':
            if len(carrinho) < 1:
                print('\nOps! Parece que o carrinho está vazio...')
            else:
                for v in carrinho:
                    linha()
                    print(f'''id: {v[0]}
produto: {v[1]}
quantidade: {v[3]}
total: R${v[5]}''')
                identificador = atributo_produto('identificador')
                for indice, produto in enumerate(carrinho):
                    if produto[0] == identificador:
                        for i in produtos:
                            for k, v in i.items():
                                if k == identificador:
                                    print(produto[3])
                                    v['estoque'] += produto[3]
                        carrinho.pop(indice)
                        print('Produto removido do carrinho!')
        elif escolha == '3':
            if len(carrinho) == 0:
                print('Carrinho vazio...')
            else:
                linha()
                print('Produtos no carrinho:')
                for v in carrinho:
                    print(f'''id: {v[0]}
produto: {v[1]}
quantidade: {v[3]}
total: R${v[5]}''')
                    linha()
        elif escolha == '4':
            if len(carrinho) < 1:
                print('Carrinho vazio! A compra foi cancelada.')
                break
            else:
                lista_totais = []
                data = datetime.date.today().strftime('%d/%m/%y')
                hora = datetime.datetime.now().time().strftime('%H:%M:%S')
                for v in carrinho:
                    v.insert(0, data)
                    v.insert(1, hora)
                    lista_totais.append(v[7])
                    vendas.append(v)
                total_venda = reduce(lambda x, y: x+y, lista_totais)
                if total_venda is not None:
                  print(f'O valor total da venda foi de R${total_venda:.2f}')
                  break
                else:
                  print('\nOps! Parece que não foi possível realizar a venda!')
                  break
        else:
            print('\nOps! Parece que você digitou um valor inválido... Tente novamente.')

# Funções de consistência de dados
def arquivo_existe(arquivo): # Verifica a existência de um arquivo no computador do usuário
    try:
        arquivo = open(arquivo, 'r')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(arquivo): # Cria um arquivo 
    with open(arquivo, 'w+'):
        print(f'Arquivo {arquivo} não existia e foi criado com sucesso.')

def ler_arquivo(nome_arquivo, tabela): # Faz a leitura de um arquivo csv
    tabela.clear()
    with open(nome_arquivo, 'r') as arquivo:
        planilha = csv.reader(arquivo, delimiter = ';', lineterminator='\n')
        for linha in planilha:
            tabela.append(linha)
        print(f'Arquivo {arquivo} encontrado e lido com sucesso.')

def exportar_arquivo(nome_do_arquivo, tabela): # Exporta um arquivo csv
    with open(nome_do_arquivo, 'w') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
        escritor.writerows(tabela)

def conversao_dicionario_csv(): # Prepara os produtos para serem exportados como csv
    dicionario_desmantelado = []
    lista_estoque = [['id', 'nome', 'marca', 'preco', 'estoque', 'descricao']]
    for a in range(len(produtos)):
        dicionario_desmantelado.append(list(produtos[a].keys())[0])
        dicionario_desmantelado.append(list(produtos[a].values())[0].get("nome"))
        dicionario_desmantelado.append(list(produtos[a].values())[0].get("marca"))
        dicionario_desmantelado.append(list(produtos[a].values())[0].get("preco"))
        dicionario_desmantelado.append(list(produtos[a].values())[0].get("estoque"))
        dicionario_desmantelado.append(list(produtos[a].values())[0].get("descricao"))
        lista_estoque.append(dicionario_desmantelado[:])
        dicionario_desmantelado.clear()
    return lista_estoque

def conversao_csv_dicionario(): # Lê o csv e monta a lista de produtos
    for i, v in enumerate(lista_estoque):
        dicionario = {}
        if i > 0:
            dicionario = {v[0]: {'nome': v[1],
                                'marca': v[2],
                                'preco': float(v[3]),
                                'estoque': int(v[4]),
                                'descricao': v[5]}}
            produtos.append(dicionario)

# PROGRAMA PRINCIPAL
if not arquivo_existe('estoque_produtos.csv'):
    criar_arquivo('estoque_produtos.csv')
else:
    lista_estoque = []
    ler_arquivo('estoque_produtos.csv', lista_estoque)
    conversao_csv_dicionario()
            

if not arquivo_existe('relatorio_de_vendas.csv'):
    criar_arquivo('relatorio_de_vendas.csv')
else:
    ler_arquivo('relatorio_de_vendas.csv', vendas)

contador_cadastro = 0
opcao = 0
while True:
    menu()
    opcao = input('\nDigite a opção desejada: ')
    if opcao == '6':
        print('Programa encerrado')
        break
    elif opcao == '1':
        cadastrar()
    elif opcao == '2':
        atualizar()
    elif opcao == '3':
        excluir()
    elif opcao == '4':
        executar_venda()
    elif opcao == '5':
        viz_dados_produtos()
    else:
        print('\nOps! Opção inválida... Tente novamente.')

lista_estoque = conversao_dicionario_csv()
exportar_arquivo('relatorio_de_vendas.csv', vendas)
exportar_arquivo('estoque_produtos.csv', lista_estoque)