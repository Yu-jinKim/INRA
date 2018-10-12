#### Imports ####

import os
import sys
import argparse

########################################################################################################################################################

#### arguments ####
## crée les options dans la ligne de commande (4 ici)
def arguments(args):
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--directory",dest="dir")
	parser.add_argument("-f","--file",dest="names")
	parser.add_argument("-g","--groups", dest="groups",nargs="+")
	parser.add_argument("-o","--output",dest="output")
	args = parser.parse_args()
	if args.dir!=None:
		os.chdir(args.dir)
	return (args.names,args.groups,args.output)

#### read ####
## Récupération du contenu pour la liste des noms
def read(fichier):
	try:
		f=open(fichier,"r")
	except FileNotFoundError as e:
		print("Le fichier '",e.filename,"' n'existe pas")
		sys.exit(0)
	else:
		lines=f.readlines()
		f.close()
	return lines

#### read_groups ####
## Récupération du contenu avec le strip() en plus pour la fonction suivante
def read_groups(groups):
	liste=[]
	for i in range(0,len(groups)):
		contenu=[]
		try:
			f=open(groups[i],"r")
		except FileNotFoundError as e:
			print("Le fichier '",e.filename,"' n'existe pas")
			sys.exit(0)
		else:
			f=open(groups[i],"r")
			lines=f.readlines()
			for line in lines:
				line=line.strip()
				contenu.append(line)
			liste.append(contenu)
			f.close()
	return liste

#### comp ####
## Comparaison des noms
def comp(names,groups):
	liste=[]

## Mise en place d'un premier indice "i" pour la colonne des noms
	for i in range(0,len(names)):
		line=names[i].split()

## Deuxième indice "j" pour parcourir la première colonne des paires
		for j in range(1,len(groups)+1):

## Si on trouve que le premier élément de la liste des noms correspond à un nom dans le groupe j-1...
			if line[0] in groups[j-1]:

## On met en place un troisième indice "k" pour parcourir la deuxième colonne des paires
				for k in range(1,len(groups)+1):

## On trouve les numéros de groupes de chaque membre de la paire et on crée une ligne avec la paire et les numéros des groupes dans les deux colonnes qui suivent		
					if line[1] in groups[k-1]:
						liste.append(line[0]+"\t"+line[1]+"\t"+str(j)+"\t"+str(k))					
	return liste

#### save ####
## Sauvegarde du fichier
def save(arg,out,groups):

## Attribution de valeur par défaut à l'output
	if out == None:
		out="analyse_paires_"+str(len(groups))+"_groups"
	try:
		f=open(out,"r")
	except FileNotFoundError:
		f=open(out,"w")
		for ele in arg:
			f.write(ele+"\n")
		f.close()
	else:
		print("Attention, ce fichier "+out+" existe déjà\nFermeture du programme\n")
		sys.exit(0)
	print("Le fichier s'appellera "+out)





