from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida
frota = {}
navios = {'porta-aviões': [4, 1], 'navio-tanque': [3, 2], 'contratorpedeiro': [2, 3], 'submarino': [1, 4]}
for nome in navios:
    tamanho = navios[nome][0]
    quantidade = navios[nome][1]
    for i in range(quantidade):
        valida = False
        while not valida:
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            if nome == 'submarino':
                orientacao = 'horizontal'
            else:
                opcao = int(input('[1] Vertical [2] Horizontal >'))
                if opcao == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valida = True
            else:
                print('Esta posição não está válida!')
print(frota)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'
    for linha in range(10):
        jogador_info = ''
        oponente_info = ''
        for coluna in range(10):
            if coluna > 0:
                jogador_info += '  '
                oponente_info += '  '
            jogador_info += str(tabuleiro_jogador[linha][coluna])
            info = tabuleiro_oponente[linha][coluna]
            if info == 'X' or info == '-':
                oponente_info += info
            else:
                oponente_info += '0'
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto