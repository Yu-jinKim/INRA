#### Imports ####

import os, sys, argparse

########################################################################################################################################################

## arguments ##
## Récupérer les arguments donnés
def arguments(arg):
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--directory",dest="dir")
	parser.add_argument("-f","--file",dest="file",nargs="+")
	parser.add_argument("-o","--output",dest="output")
	parser.add_argument("-c","--column",dest="col")
	args = parser.parse_args()
	if args.dir!=None:
		os.chdir(args.dir)
	if args.output==None:
		args.output="results.out"
	if args.file==None:
		print("Vous n'avez pas entré de fichier à concaténer\n")
		sys.exit(0)
	if args.col == None:
		print("Vous n'avez pas entré le numéro de la colonne à récupérer")
		sys.exit(0)
	else:
		try:
			int(args.col)
		except TypeError:
			print("L'entrée [-c] n'est pas un entier")
			sys.exit(0)
		else:
			args.col=int(args.col)-1
	return (args.file,args.output,args.col)

## read ##
## Récupérer le contenu
def read(files):
	liste=[]
	for i in range(0,len(files)):
		contenu=[]
		try:
			f=open(files[i],"r")
		except FileNotFoundError as e:
			print("Le fichier '",e.filename,"' n'existe pas")
			sys.exit(0)
		else:
			f=open(files[i],"r")
			lines=f.readlines()
			for line in lines:
				line=line.strip()
				contenu.append(line)
			liste.append(contenu)
			f.close()
	return liste

## data ##
## Récupérer ce qui est intéressant
def data(files, col):
	names_liste=[]
	FPKM_liste=[]
	for line in files[0]:
		line=line.split()
		names_liste.append(line[0][5:len(line[0])])
	for fichier in files:
		stuff=[]
		for i in range(1,len(fichier)):
			line=fichier[i].split()
			stuff.append(line[col])
		FPKM_liste.append(stuff)
	return (names_liste,FPKM_liste)

## save ##
## Sauvegarder les résultats
def save(names,FPKM,out):
	try:
		f=open(out,"r")
	except FileNotFoundError:
		f=open(out,"w")
		f.write("tracking_id\tW1\tW2\tW3\tJ2-1\tJ2-2\tJ2-3\tJ3-1\tJ3-2\tJ3-3\tFem1\tFem2\tFem3\n")
		for i in range(1,len(FPKM[0])+1):
			f.write(names[i])
			for j in range(0,len(FPKM)):
				f.write("\t"+FPKM[j][i-1])
			f.write("\n")
		f.close()
	else:
		print('Attention, ce fichier "'+out+'" existe déjà\nFermeture du programme\n')
		sys.exit(0)
	print("Le fichier s'appellera "+out)






	
