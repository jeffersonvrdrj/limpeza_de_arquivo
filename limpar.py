#!C:\Program Files\Python310\python.exe

# coding: utf-8

import cgi, os, re
import cgitb; cgitb.enable()
import pandas as pd


#inicio locais de gravação 

pasta = 'C:\\xampp\\cgi-bin\\limpeza\\' # local da carga do arquivo 
gravar = 'C:\\xampp\\htdocs\\limpeza\\' # local da salvar arquivo 
resultados='C:\\xampp\\cgi-bin\\arquivos\\resultados\\'# local da gravacao do resultado  

#fim  locais de gravação 


print ("Content-type: text/html\n\n")
print ("<!DOCTYPE html> <html lang=pt-BR> <head><meta http-equiv=content-type content=text/html><meta charset=utf-8/>")
 
print (" <script src=https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js> </script>")

print ("<title>Resposta </title>")
print ("</head><body>")

#####Inicio rotina de parse#####

form = cgi.FieldStorage()
nome_arquivo = form.getvalue('nome_arquivo')
escolhas = form.getlist("acao")
linhas_total= int(form.getvalue('linhas_total'))
#####fim da rotina de parse######



## inicio coletando a planilha e gerando dataframe e outras informações ###

arquivo= pasta + nome_arquivo
tbl=pd.read_excel(arquivo)
tamanho_lista = len(escolhas)

## fim coletando a planilha e gerando dataframe e outras informações ###

# incio da rotinas de tratamento do arquivo

def cep():
	inter2=0

	# coluna que sera tratada
	coluna_end = tbl['Endereco']


	print("estou dentro  da rotina cep<br>")
	

	while inter2 < linhas_total-1:
		
		linhas = coluna_end.loc[inter2]	
		print(inter2)

		palavra1 = "cep"
		palavra2 = "CEP"

		if palavra1  in linhas :

			print(linhas + ' - tem palavra cep minuscula')

			tbl['Endereco'].replace('cep','', inplace = True)
			#nova_linha= linhas.replace('cep','')
			print ("<br>")
			print (nova_linha + ' - linha corrigida')
			print ("<br>")

		elif palavra2  in linhas :

			print(linhas + ' - tem palavra cep Maiscula')
			nova_linha= linhas.replace('CEP','')
			print ("<br>")
			print (nova_linha + ' - linha corrigida')
			print ("<br>")

		else:

			print (linhas +" - nao tem a palavra cep")
			print ("<br>")

		print(linhas)
		print ("<br>")
		inter2+= 1




def numero():

	print("estou dentro  da rotina numero<br>")


def sem_numero():

	print("estou dentro  da rotina sem numero<br>")

def tirar_ponto():

	print ("estou dentro  da rotina tirar ponto <br>")

	inter2=0

	# coluna que sera tratada
	coluna_end = tbl['Endereco']
		

	while inter2 < linhas_total-1:

		linhas = coluna_end.loc[inter2]	

		#s = 'Hello, World!!'

    	#caracteres = '.,!'
    	#caracteres = linhas.maketrans(' ', ' ', '-')
 
    	#linhas = linhas.translate(caracteres)
    
 
    


		print(linhas)
		print ("<br>")
		inter2+= 1








def avenida():

	print ("estou dentro da rotina avenida<br>")

def rua():

	print ("estou dentro  da rotina rua<br>")

## Fim da rotina de tratamento do arquivo##



# inicio da iteração na lista de escolha 

for itens in escolhas:

	if itens == "cep":

		#print ("escolhi cep<br>")
		cep()

	if itens == "numero":

		#print ("escolhi numero<br> ")
		numero()

	if itens == "sem_numero":

		#print("escolhi sem numero <br>")
		sem_numero()

	if itens == "tirar_ponto" :

		#print ("escolhi tirar_ponto<br>")
		tirar_ponto()

	if itens == "avenida" :

		#print("escolhi avenida<br>")
		avenida()
	
	if itens == "rua":

		#print("escolhi rua<br> ")
		rua()

# fim  da iteração na lista de escolha 




## fim coletando a planilha e gerando dataframe ###
print ("nome do arquivo: " + str(nome_arquivo) + "<br>")
print ("Qtd linhas : " + str(linhas_total) + "<br>")
print ("</body></html>")
