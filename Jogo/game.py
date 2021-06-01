from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int)-> None:
    dificuldade: int = int(input('Informe a dificuldade desejada (1, 2, 3 ou 4): '))

    calc: Calcular = Calcular(dificuldade)
    print(f'O resultado da operação é: ')
    calc.mostrar_operacao()

    resultado: int = int(input())
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você têm {pontos} pontos.')

    continuar: int = int(input('Deseja continuar no jogo? [1 - Sim, 0 - Não]: '))

    if continuar == 1:
        jogar(pontos)
    else:
        print(f'Você finalizou o jogo com {pontos} ponto(s)')
        print(f'Obrigado por jogar!')


if __name__ == '__main__':
    main()



