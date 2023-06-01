def exibir_tabuleiro(tabuleiro):
    for i in range(3):
        print(" | ".join(tabuleiro[(i, j)] for j in range(3)))
        if i < 2:
            print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    combinacoes_vitoria = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combinacao in combinacoes_vitoria:
        if all(tabuleiro[posicao] == jogador for posicao in combinacao):
            return True

    return False

def verificar_empate(tabuleiro):
    return all(tabuleiro[posicao] != " " for posicao in tabuleiro)


def jogar_jogo_da_velha():
    tabuleiro = {(i, j): " " for i in range(3) for j in range(3)}
    jogador_atual = "X"
    posicoes = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2)}

    while True:
        exibir_tabuleiro(tabuleiro)
        posicao = int(input("Digite o número da posição (1 a 9): "))

        if posicao in posicoes:
            linha, coluna = posicoes[posicao]

            if tabuleiro[(linha, coluna)] == " ":
                tabuleiro[(linha, coluna)] = jogador_atual

                if verificar_vitoria(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print("O jogador {} venceu!".format(jogador_atual))
                    break

                if verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break

                if jogador_atual == "X":
                    jogador_atual = "O"
                else:
                    jogador_atual = "X"
            else:
                print("Posição ocupada. Tente novamente.")
        else:
            print("Posição inválida. Tente novamente.")

jogar_jogo_da_velha()