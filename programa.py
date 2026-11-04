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
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
total_navios = 0
for nome in frota_oponente:
    total_navios += len(frota_oponente[nome])
posicoes_informadas = []
jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    ataque_valido = False
    while not ataque_valido:
        linha_ataque = int(input('Jogador, qual linha deseja atacar? '))
        while linha_ataque < 0 or linha_ataque > 9:
            print('Linha inválida!')
            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))
        coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna_ataque < 0 or coluna_ataque > 9:
            print('Coluna inválida!')
            coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))
        if [linha_ataque, coluna_ataque] in posicoes_informadas:
            print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')
        else:
            posicoes_informadas.append([linha_ataque, coluna_ataque])
            ataque_valido = True
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)
    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False