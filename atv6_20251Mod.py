import random
def f_preencheListaRand(n:int)->list: # Função cria/preenche lista randomicamente
	lista = list()
	for i in range(n):
		x = random.randint(1, 50000000000000000000000000000000000000000000000000) # Põe um valor aleatório para x
		lista.append(x/100) # Transformando em float o x
	return lista
		
def f_ordenaCrescente(lista:list)->list:
	listaord = sorted(lista)
	return listaord

def f_buscaSequencialAlterada(dados:list, elemento:float)->tuple:
	posicao = int()
	i = int()
	posicao = -1
	i = 0
	achou = False
	quantiC = 0

	while i < len(dados) and achou == False:
		if elemento == dados[i]:
			posicao = i
			achou = True
		i = i + 1
		if posicao < 0:
			quantiC = len(dados)
		else:	
			quantiC = posicao
	return posicao, quantiC

def f_buscaBinariaAlterada(dados:list, elemento:float)->int:
	ini = int(); meio = int(); fim = int(); posicao = int()
	ini = 0
	fim = len(dados) - 1
	posicao = -1
	quantiC = 0
	while ini <= fim and posicao == -1:
		meio = (ini + fim) // 2
		if elemento == dados[meio]:
			posicao = meio
			quantiC = quantiC + 1
		else:
			if elemento > dados[meio]:
				ini = meio + 1
				quantiC = quantiC + 1
			else:
				fim = meio - 1
				quantiC = quantiC + 1
	return posicao, quantiC
