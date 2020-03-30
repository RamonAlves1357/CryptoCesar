"""
	Instituição:
        INSTITUTO FEDERAL DA PARAÍBA - Campus Sousa
    @utor: 
        Ramon Alves
    Data de inicio: 
        03/06/2019
    Professor: 
        Victor
    Disciplina:
		Tópicos Especiais & Segurança da Informação
    Objetivo: 
        Implementar o Criptograma de Cesar tanto para encriptar qunato para decriptar um texto qualquer.
    Arquivo:
		main.py
			Aonde ira chamar o arquivo "CryptoCesar.py" para criptografar ou descriptografar o arquivo
			Alem de ter a interação com o user
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import CryptoCesar as Cesar

def  getTextFromFile(fileName): 
	with open(fileName, 'r') as archive:
		return archive.read()
def saveTextFrominFile(fileName, EXIT):
	with open(fileName, 'w') as archive: 
		archive.write(EXIT)

texto = getTextFromFile('documento.txt')

while True:
	print('''
		## ## ### #### ### ## ##
		#      Criptologia     #
		## ## ### #### ### ## ##
	''')

	print('Oq vc deseja?\n')

	print("(1) - Encriptar documento.txt e salvar em saida.txt?")
	print("(2) - Decriptar documento.txt e salvar em saida.txt?")
	print("(0) - Sair")

	op = int(input('>>>'))
	
	if (op != 0) and (op != 1) and (op != 2):
		print("ERROR!!!")
		print("Por favor reinicie o programa e informe uma opção valida!")
		break
	
	elif (op == 0):
		print("Obg por usar nossa aplicação! ;)")
		break

	elif (op == 1):
		chave = int(input('\nEntre com a chave criptográfica: '))
		crypt = Cesar.encripitar(texto, chave)

	elif (op == 2):
		chave = int(input('\nEntre com a chave criptográfica: '))
		cifra = getTextFromFile('saida.txt')
		crypt = Cesar.decripitar(cifra, chave)
		
	saveTextFrominFile('saida.txt', crypt)
