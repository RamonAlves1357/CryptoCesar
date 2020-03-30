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
		CryptoCesar.py
			Aonde todo processo será realizado.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

#Função de criptografia
def encripitar(texto, chave):
	TextoEncrypt = ""
	for caracter in texto:
		Alfabeto = string.ascii_letters
		if (caracter in Alfabeto):
			if (caracter.islower()): 
				Alfabeto = Alfabeto[0:26]
				index = Alfabeto.index(caracter) + chave
				TextoEncrypt += Alfabeto[index % len(Alfabeto)]
			else:
				if (caracter.isupper()): 
					Alfabeto = Alfabeto[26:52]	
					index = Alfabeto.index(caracter) + chave
					TextoEncrypt += Alfabeto[index % len(Alfabeto)]
		if (caracter not in Alfabeto):
			TextoEncrypt += caracter
	return TextoEncrypt 

#Função de decriptografia
def decripitar(cifra, chave):
	TextoDecrypt = ''
	for caracter in cifra:
		Alfabeto = string.ascii_letters
		if (caracter in Alfabeto):
			if (caracter.islower()):
				Alfabeto = Alfabeto[0:26]
				index = Alfabeto.index(caracter) - chave
				TextoDecrypt += Alfabeto[index % len(Alfabeto)]
			else:
				if (caracter.isupper()):
					Alfabeto = Alfabeto[26:52]
					index = Alfabeto.index(caracter) - chave
					TextoDecrypt += Alfabeto[index % len(Alfabeto)]
		if (caracter not in Alfabeto):
			TextoDecrypt += caracter
	return TextoDecrypt 
