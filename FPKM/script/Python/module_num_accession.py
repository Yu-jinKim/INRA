## Imports ##

import os
import sys, argparse

########################################################################################################################################################

#### arguments ####
## 4 arguments: répertoire, fichier_nom, fichier_group, fichier_sortie
def arguments(arg):
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--directory",dest="dir")
	parser.add_argument("-n","--names",dest="names")
	parser.add_argument("-g","--groups", dest="groups",nargs="+")
	parser.add_argument("-o","--out",dest="out")
	args = parser.parse_args()
	if args.dir!=None:
		os.chdir(args.dir)
## Si l'un des deux arguments essentiels n'est pas entré, le programme quitte
	elif args.names == None or args.group == None:
		print("Vous n'avez pas entré le nom de l'un des fichiers requis\nFermeture du programme")
		sys.exit(0)
	return(args.names,args.groups,args.out)

#### entry_names ####
## Récupération de la première colonne du fichier (les noms des gènes)
def entry_names(arg):
	names=[]
	try:
		str(arg)
	except AttributeError:
		print("Vous n'avez pas entré de chaîne de caractère.\nFermeture du programme")
		sys.exit(0)
	else:
		try:
			f=open(arg,"r")
		except FileNotFoundError as e:
			print("Le fichier ",e.filename," n'existe pas (",e.strerror,")\nFermeture du programme")
			sys.exit(0)
		else:
			lines=f.readlines()
			for line in lines[1:len(lines)]:
				line=line.split()
				names.append(line[0])
			f.close()
	return names

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

#### dico ####
## Crée le dictionnaire à partir de la colonne de nom et les lignes correspondantes
def dico(fichier_nom):
	accession={}
## Pour la longueur de la colonne  de noms on va ajouter les clés (qui vont être les numéros des lignes) et les valeurs (les noms des gènes)
	for i in range(0,len(fichier_nom)):
		accession[i+1]=fichier_nom[i]
	return accession

#### output ####
## Crée la liste des noms correspondant aux numéros de lignes
def output(dico,numbers):
	liste=[]
	for i in range(0,len(numbers)):
		groupe=[]		
		for ele in numbers[i]:
			ele=int(ele)
			groupe.append(dico[ele])
		liste.append(groupe)
	return liste
	
#### save ####
## Sauvegarde les données
def save(groupe,out):	
	if out == None:
		out="group_"
		for i in range(0,len(groupe)):
			try:
				f=open(out+str(int(i)+1)+"_names","r")
			except FileNotFoundError:
				f=open(out+str(int(i)+1)+"_names","w")
				for ele in groupe[i]:
					f.write(ele+"\n")
				f.close()
			else:
				print("Attention, ce fichier "+out+" existe déjà\nFermeture du programme\n")
				sys.exit(0)
	else:
		for i in range(0,len(groupe)):
			try:
				f=open(out+str(int(i)+1),"r")
			except FileNotFoundError:
				f=open(out+str(int(i)+1),"w")
				for ele in groupe[i]:
					f.write(ele+"\n")
				f.close()
			else:
				print("Attention, ce fichier "+out+" existe déjà\nFermeture du programme\n")
				sys.exit(0)



 
