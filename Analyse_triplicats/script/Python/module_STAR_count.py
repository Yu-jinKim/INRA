#### Imports ####

import sys, os, argparse

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

## sum_col ##
## Faire la somme des colonnes 3, 4
def sum_col(files):
	sum_col_liste=[]
	names_liste=[]
	stuff=[]
	for line in files[0]:
		line=line.split()
		names_liste.append(line[0][5:len(line[0])])
	names_liste=names_liste[4:len(names_liste)]
	for fichier in files:
		nb_liste=[]
		for i in range(4,len(fichier)):
			line=fichier[i].split()
			for j in range(2,len(line)):
				nb_liste.append(line[j])
		stuff.append(nb_liste)
	for i in range(0,len(stuff)):
		numbers=[]
		for j in range(0,len(stuff[i]),2):
			nb=int(stuff[i][j])
			nb=nb+int(stuff[i][j+1])
			numbers.append(nb)
		sum_col_liste.append(numbers)
	return (sum_col_liste,names_liste)

## save ##
## Sauvegarder les résultats
def save(names,sums,out):
	try:
		f=open(out,"r")
	except FileNotFoundError:
		f=open(out,"w")
		f.write("tracking_id\tW1\tW2\tW3\tJ2-1\tJ2-2\tJ2-3\tJ3-1\tJ3-2\tJ3-3\tFem1\tFem2\tFem3\n")
		for i in range(0,len(sums[0])):
			f.write(names[i])
			for j in range(0,len(sums)):
				f.write("\t"+str(sums[j][i]))
			f.write("\n")
		f.close()
	else:
		print('Attention, ce fichier "'+out+'" existe déjà\nFermeture du programme\n')
		sys.exit(0)
	print("Le fichier s'appellera "+out)

		
