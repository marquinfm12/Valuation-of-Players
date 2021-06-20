import time

print('Informe os dados relativos ao jogador e a data atual do jogo\n')

while True:
    # Informações do Jogador
    ano_atual = int(input('Ano atual: '))
    mes_atual = int(input('Mês atual (número do mês): '))
    nome = input('Nome do jogador: ')
    idade = int(input('Idade: '))
    valor_mercado = float(input('Valor de mercado atual: '))
    ano_fim_contrato = int(input('Ano de fim de contrato: '))
    mes_fim_contrato = int(input('Mês de fim de contrato (número do mês): '))
    potencial = int(input('Grau de potencial de evolução do jogador (1 a 5): '))
    importancia = int(input('Grau de importância na equipe (1 a 5): '))
    substituir = int(input('Grau de dificuldade em substituí-lo (1 a 5): '))

    # Mark-ups
    if idade < 25:
        mkp_idade = 0.4
    elif idade < 30:
        mkp_idade = 0.1
    else:
        mkp_idade = -0.3

    meses_restantes = 12 * (ano_fim_contrato - ano_atual) + mes_fim_contrato - mes_atual
    if meses_restantes < 11:
        mkp_meses = -0.3
    elif meses_restantes < 23:
        mkp_meses = -0.15
    elif meses_restantes < 35:
        mkp_meses = 0.05
    elif meses_restantes < 47:
        mkp_meses = 0.1
    else:
        mkp_meses = 0.2

    mkp_potencial = ['', -0.1, -0.05, 0.05, 0.3, 0.5]
    mkp_importancia = ['', -0.35, -0.15, 0.05, 0.2, 0.45]
    mkp_substituivel = ['', -0.4, -0.25, 0.05, 0.3, 0.5]

    # Valor final de venda
    mkp_total = mkp_idade + mkp_meses + mkp_potencial[potencial] + mkp_importancia[importancia] + mkp_substituivel[substituir]
    valor_venda = valor_mercado * (1 + mkp_total)
    milhao = int(valor_venda // 1000000)
    cemmil = int((valor_venda % 1000000) // 1000)
    centena = int((valor_venda % 1000000) % 1000)
    time.sleep(2)
    print('{} milhões {} mil e {} reais'.format(milhao, cemmil, centena))

    fim = input('Deseja refazer? Sim [s] ou Não [n]\n> ')
    if fim.lower() not in ('s'):
        break
