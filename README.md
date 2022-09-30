# Valuation-of-Players
This is a beginner code the analyze the market value of players in Football Manager 2012, written in Python and executed on the terminal. 
Consists in analyze the age, the actual market value, the years of contract already payedm the potencial and importance to the team. 
Its not based in any knowledge of market and negociations at the area of sports, but its based in my personal feeling about the fair price to sell the players. 
I used the Football Manager version 2012 because I play more than the other versions.
The code is all in portuguese. ;)

UPDATE: 18, june, 2021
I'll rewrite the code to calculate the valuation using multipliers that will give me the final price, based in the market value. This is more precise and works for every market value, removing the 2 milion almost arbitrary added ou subtracted in the code.

	Premissas:

  Será uma base para tomada de decisão, não o preço final a ser praticado;
  Contemplará somente informações relevantes sobre o jogador e seu futuro no clube;
  O cálculo deverá ser feito com base em mark-up de transferência;
  São multiplicadores que irão incrementar ou decrementar o passe do jogador, conforme as informações dd mesmo;
  Quanto mais fácil vender um jogador, maior será seu mark-up, pois mais concorrência terá.
  
	Funcionamento:

  Mark-up começa valendo 1.000 e haverão acréscimos e diminuições;
  Os mark-ups serão aplicados, no final do preenchimento das informações, no valor de mercado atual do jogador;
  O programa deve mostrar na tela ao final, o mark-up, a porcentagem que o valor de mercado sofrerá;
  Será um looping que o usuário digitará se irá refazer o cálculo;

  		Mark-up de Transferência:
	
	Idade
Vai corresponder a uma grande parcela do mark-up, tendo em vista que quanto mais velho o jogador, mais difícil de vendê-lo, logo, reduzindo seu valor de venda;
Até 25: + 40%
Até 30:	+ 10%
Acima de 30: -30%

	Potencial
Grau de potencial que o jogador possui. Isso quer dizer que é um jogador que pode se desenvolver bem e valer mais;
Grau de 1 até 5 de perspectiva de evolução do jogador
1: -10%
2: -5%
3: 5%
4: 30%
5: 50%

	Importância
Grau de importância no time, o quanto o jogador faz diferença para a equipe;
Perdê-lo é um golpe duro na equipe ou será bem vindo sua saída;
Grau de 1 até 5 de importância
1: -35%
2: -15%
3: 5%
4: 20%
5: 45%

	Meses restantes de contrato
Quanto mais próximo do fim do contrato, menor o valor de mercado do jogador;
Será uma queda brusca, mas com ganhos altos caso o contrato esteja no começo; 
De 36 a 47: 10%
De 24 a 35: 5%
De 12 a 23: -15%
Até 11: -30%
 
	Substituível
O quão fácil é substituir esse jogador por outro no mercado
A facilidade diz que mesmo um jogador bom não preciso pedir muito, já que sua transferência pode ser compensada
Grau de 1 até 5 de facilidade para substituir o jogador
1: 50%
2: 30%
3: 5%
4: -25%
5: -40% 
