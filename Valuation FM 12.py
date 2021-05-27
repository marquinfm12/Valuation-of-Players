import time
inicio = ''
while inicio.lower() not in ('n','sair'):
    
    #Informações do jogador
    nome = input('Nome do Jogador: ')
    idade = int(input('Idade: '))
    valor_mercado = int(input('Valor de mercado: '))
    anos_cumpridos = int(input('Anos de contrato já cumpridos: '))
    potencial = input('Potencial? "s" ou "n": ')
    importante = int(input('De 0 a 5 nível de importância na equipe, tática, etc: '))
    vender = input('Precisa vender rápido? "s" ou "n": ')

    #Venda sem pressa com valorização
    if vender.lower() in ('n'):
        #Multiplicativo de Valor
        importante = importante / 20
        if potencial.lower() in ('s'):
            multiplicativo = 0.6 + importante
        else:
            multiplicativo = 0.25 + importante

        valor_primario = valor_mercado * (1 + multiplicativo)

        #Análise de idade
        if idade < 28 and potencial.lower() in ('s'):
            valor_secundario = valor_primario + 2500000 * (28 - idade)
        elif idade > 28:
            valor_secundario = valor_primario - 2000000 * (idade - 28)
        else:
            valor_secundario = valor_primario

        #Análise de contrato
        valor_final = valor_secundario * (1 - 0.04 * anos_cumpridos)

    #Venda rápida sem valorização
    else:
        if idade < 28 and potencial.lower() in ('s'):
            valor_secundario = valor_mercado + 2000000 * (28 - idade)
        elif idade > 28:
            valor_secundario = valor_mercado - 2000000 * (idade - 28)
        else:
            valor_secundario = valor_mercado

        #Análise de contrato
        valor_final = valor_secundario * (1 - 0.08 * anos_cumpridos)

    #Fim ou recomeço
    print('\n{} vale cerca de: R${} de reais'.format(nome, valor_final))
    inicio = input('Refazer? Se deseja sair do Valuation FM 12, digite "n".')
    print('Volte sempre!!')
    time.sleep(1)
