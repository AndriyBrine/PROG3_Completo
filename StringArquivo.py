def main(): 
// ATV 7

	nome = input("Digite o nome do arquivo: ")    # poderia ser um nome = "StringArquivo.txt" apenas
	# ^ para colocar em outro local que não a mesma pasta do programa principal, precisa especificar isso colocando o caminho.
	with open(nome, 'a', encoding='utf-8') as arq: # Ou arq = open("StringArquivo.txt", "w"). No caso, o with open serve para 'r'(read), para quando o arquivo digitado não existe.
		# CORPO DO WITH
	    arq.write("    O poeta é um fingidor.      \n")
	    arq.write("    Finge tão completamente     \n")
	    arq.write("    Que chega a fingir que é dor\n")
	    arq.write("    A dor que deveras sente.    \n")
	    arq.write("                Fernando Pessoa.\n")

	conteudo = str

	with open(nome, 'r', encoding='utf-8') as arq_entrada:
		# CORPO DO WITH
		conteudo = arq_entrada.read()

		# continue o programa usando conteudo
		print(conteudo)
if __name__ == '__main__':
	main()
