def main():
	nome = 'atv7_20251.txt'
	idade = int()

	with open(nome, 'r', encoding='utf-8') as arq_entrada:
		conteudo = arq_entrada.read()

	idades_lst = conteudo.split()
	soma = 0
	for i in idades_lst:
		soma = soma + float(i)
	media = soma / len(idades_lst)

	print("MEDIA IDADES=%.2f" % media)


if __name__ == '__main__':
	main()