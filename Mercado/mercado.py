from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('====================================')
    print('============ Bem-vindo =============')
    print('========== Cantina da ECT ==========')

    print('Selecione uma das opções abaixo: ')
    print('1 - Cadastrar produto(s)')
    print('2 - Listar produto(s)')
    print('3 - Comprar produto(s)')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair')

    opcao: int = int(input('Digite o número: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Obrigado por visitar nossa cantina!')
        sleep(5)
        exit(0)
    else:
        print('Opção desconhecida, tente novamente')
        sleep(1)
        menu()

def cadastrar_produto() -> None:
    print('Cadastro do produto')
    print('---------------------')
    nome: str = input('Digite o nome do produto:')
    preco: float = float(input('Informe o preço do produto: '))
    produto: Produto = Produto(nome, preco)
    produtos.append(produto)
    print(f'O produto {produto.nome} foi cadastrado com sucesso')
    sleep(1)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:
        print('Lista de produtos')
        print('-----------------')
        for produto in produtos:
            print(produto)
            print('----------------------')
            sleep(1)
        menu()
    else:
        print('Não há produtos cadastrado')
        sleep(2)
        menu()

        print('')

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto:')
        print('----------------------------------')
        print('------ Produtos disponíveis ------')
        for produto in produtos:
            print(produto)
            print('-------------------------------')
            sleep(1)
        codigo: int = int(input())
        produto: Produto = pega_produto_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    qtd: int = item.get(produto)
                    if qtd:
                        item[produto] = qtd + 1
                        print(f'O produto {produto.nome} possui {qtd + 1} unidades no carrinho')
                        tem_no_carrinho = True
                        sleep(1)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(1)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(1)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado!')
            sleep(1)
            menu()
    else:
        print('Não há produtos cadastrados')
        sleep(1)
        menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-------------------------')
                sleep(1)
        menu()
    else:
        print('Não há produto no carrinho')
        sleep(1)
        menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos no carrinho: ')
        print('----------------------')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('--------------------------------')
                sleep(1)
        print(f'Fatura total: {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(1)
    else:
        print('Não existem produtos no carrinho')
        sleep(1)
        menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
