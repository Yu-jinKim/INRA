#### Imports ####

import os, argparse
import sys

########################################################################################################################################################

#### arguments ####
## 4 arguments dispo
def arguments(arg):
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--directory",dest="dir")
	parser.add_argument("-p","--paires",dest="paires")
	parser.add_argument("-g","--genes", dest="genes")
	parser.add_argument("--output_filtre",dest="output_filtre")
	parser.add_argument("--output_retires",dest="output_retires")
	parser.add_argument("--output_conserves",dest="output_conserves")
	args = parser.parse_args()
	if args.dir!=None:
		os.chdir(args.dir)
	if args.output_filtre==None:
		args.output_filtre=args.paires
	if args.output_retires==None:
		args.output_retires=args.paires+"_retirés"
	if args.output_conserves==None:
		args.output_conserves=args.paires+"_conservés"
	return (args.paires,args.genes,args.output_filtre,args.output_retires,args.output_conserves)

#### entry_paires ####
## On extrait les deux premières colonnes du fichier
def entry_paires(arg):
	pair_1=[]
	pair_2=[]
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
			for line in lines:
				line=line.split()
				pair_1.append(line[0])
				pair_2.append(line[1])
	return (pair_1, pair_2)

#### entry_names ####
## On extrait la première colonne sans le titre
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

#### comp ####
## Comparaison des 3 listes de "colonnes"
def comp(pair_1,pair_2,names):
	conserve=[]
	remove=[]
	for i in range(0,len(pair_1)):
		if not pair_1[i] in names or not pair_2[i] in names:
			remove.append(pair_1[i]+" "+pair_2[i])
		elif pair_1[i] in names and pair_2[i] in names:
			conserve.append(pair_1[i]+" "+pair_2[i])
	return (conserve,remove)

#### filtre_pair ####
## On ne va garder que les lignes contenant les lignes dans la liste conserve obtenue juste avant
def filtre_pair(names,nom_paires):
	liste1=[]
	f=open(nom_paires,"r")
	lines=f.readlines()
	for line in lines:
		line=line.split()
		for name in names:
			name=name.split()
			if line[0] == name[0] and line[1] == name[1]:
				liste1.append(line)
	f.close()
	return liste1

#### save_names ####
## Sauvegarde le fichier de liste des noms
def save_names(arg,out,entry_paires):
	try:
		f=open(out,"r")
	except FileNotFoundError:
		f=open(out,"w")
		for ele in arg:
			ele=str(ele)
			f.write(ele+"\n")
		f.close()
	else:
		print("Attention, ce fichier "+out+" existe déjà\nFermeture du programme\n")
		sys.exit(0)
	print("Le fichier s'appellera "+out)

#### save_filtre ####
## Sauvegarde le fichier de base filtré
def save_filtre(arg,out,entry_paires):
	if out == entry_paires:
		print("Le fichier filtré s'appellera "+out+"_filtré")
		out=out+"_filtré"
	try:
		f=open(out,"r")
	except FileNotFoundError:
		f=open(out,"w")
		for ele in arg:
			ele="\t".join(ele)
			f.write(ele+"\n")
		f.close()
	else:
		print("Attention, ce fichier "+out+" existe déjà\nFermeture du programme\n")
		sys.exit(0)
	print("Le fichier s'appelera "+out)

