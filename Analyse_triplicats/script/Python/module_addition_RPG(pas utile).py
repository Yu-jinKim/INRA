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
	args = parser.parse_args()
	if args.dir!=None:
		os.chdir(args.dir)
	if args.output==None:
		args.output="results.out"
	if args.file==None:
		print("Vous n'avez pas entré de fichier à concaténer\n")
		sys.exit(0)
	return (args.file,args.output)

## read ##
## Récupérer le contenu des fichiers dans une liste
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

## sum_lines ##
## Récupération des noms et des sommes
def sum_lines(files):
	name_liste=[]
	sum_liste=[]
	stuff=[]
## Récupération des noms des lignes
	for line in files[0]:
		line=line.split()
		name_liste.append(line[0])
## Récupération des nombres en une seule liste ...
	for fichier in files:
		nb_liste=[]
		for i in range(0,len(fichier)):
			line=fichier[i].split()
			len_line=len(line)
			for j in range(1,len(line)):
				nb_liste.append(line[j])
## ... dans laquelle chaque indice représente son fichier d'origine
		stuff.append(nb_liste)
## Somme des lignes
	for i in range(0,len(stuff[0])):
		nb=0
		for j in range(0,len(stuff)):
			nb=nb+int(stuff[j][i])
		sum_liste.append(nb)
	return (name_liste,sum_liste,len_line)

## save ##
## Donner un output
def save(names,sums,out,len_line):
	flag=0
	try:
		f=open(out,"r")
	except FileNotFoundError:
		f=open(out,"w")
		for ele in names:
			f.write(ele)
## Astuce pour écrire 3 nombres à chaque fois mais pas 3 fois les mêmes
			for i in range(0,len_line-1):
				f.write("\t"+str(sums[flag]))
				flag+=1
			f.write("\n")
		f.close()
	else:
		print("Attention, ce fichier "+out+" existe déjà\nFermeture du programme\n")
		sys.exit(0)
	print("Le fichier s'appellera "+out)






