def f_criarlista()->list:
	listatotal = list()
	listagenerica = list()
	nome = input()
	with open(nome, 'r', encoding='utf-8') as arquivo:
		for linha in arquivo:
			lista = linha.split(";")
			x = float(lista[1])
			x2 = float(lista[2])
			listagenerica = [lista[0], x, x2]
			listatotal.append(listagenerica)
	return listatotal


def f_IMC(peso:float, altura: float)->float:
	IMC = float
	IMC = peso/(altura**2)
	return IMC


def f_OrdemIMC(lst_pessoas:list)->list:
	lst_pessoas.sort(key= lambda ordemIMC:f_IMC(ordemIMC[1],ordemIMC[2]))
	return lst_pessoas


def f_printformato(lst_pessoas:list)->None:
	saida = 'saída.txt'
	lst_pessoas = f_OrdemIMC(lst_pessoas)
	with open(saida, 'w', encoding='utf-8') as arquivo:
		for i in lst_pessoas:
			arquivo.write(str(i[0])+";%.2f" % f_IMC(i[1], i[2]) + "\n")


