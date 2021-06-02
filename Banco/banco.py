from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('----------------------------------')
    print('-------------- ATM ---------------')
    print('----------- LOOK BANK ------------')
    print('----------------------------------')

    print('Selecione uma opção do menu: ')
    print('1 - Criar conta')
    print('2 - Saques')
    print('3 - Depósitos')
    print('4 - Transferências')
    print('5 - Listar contas')
    print('6 - Sair')

    opcao: int = int(input())

    if opcao == 1:
        criarconta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Obrigado por utilizar nossos sistemas, volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção desconhecida, tente novamente.')
        sleep(1)
        menu()


def criarconta() -> None:
    print('Informe os dados do cliente: ')
    nome: str = input('Nome do cliente: ')
    email: str = input('Email do cliente: ')
    cpf: str = input('Informe o CPF do cliente: ')
    datanascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, datanascimento)
    conta: Conta = Conta(cliente)

    contas.append(conta)
    print('Conta criada com sucesso.')
    print('Dados inseridos: ')
    print('--------------------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')

    else:
        print('Não existem contas cadastradas')
        sleep(1)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))
            conta.depositar(valor)

        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Não existem contas cadastradas')
        sleep(1)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = int(input('Digite o número da conta de origem: '))
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input('Digite o número da conta de destino: '))
            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor: float = float(input('Digite o valor da transferência: '))
                conta_origem.transferir(conta_destino, valor)

                sleep(1)
                menu()

            else:
                print(f'A conta de destino de número {conta_destino} não foi encontrada.')
                sleep(1)
            menu()
        else:
            print(f'A sua conta de número {numero_origem} não foi encontrada.')
            sleep(1)
        menu()

    else:
        print('Não existem contas cadastradas')
        sleep(1)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas: ')

        for conta in contas:
            print(conta)
            print('-------------------------------')
            sleep(1)
        menu()

    else:
        print('Não existem contas cadastradas.')
    sleep(1)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()



