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