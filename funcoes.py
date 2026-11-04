def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else: 
            posicoes.append([linha, coluna + i])
    return posicoes
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(frota):
    
    grid = []
    for i in range(10):
        grid.append([0] * 10)

    
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                grid[linha][coluna] = 1
    return grid
def afundados(frota, tabuleiro):
    total = 0
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            afundou = True
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
            if afundou:
                total += 1
    return total
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in novas_posicoes:
        l = posicao[0]
        c = posicao[1]
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False
        for lista_navios in frota.values():
            for navio in lista_navios:
                if posicao in navio:
                    return False
    return True

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
