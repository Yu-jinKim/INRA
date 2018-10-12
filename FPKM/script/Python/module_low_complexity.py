## Imports ##

import sys, os, argparse
from Bio import SeqIO

########################################################################################################################################################

#### Arguments ####
## Extraction de chaque argument et attribution de valeurs par défaut

def arguments(arg):
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--directory",dest="dir")
	parser.add_argument("-f","--file",dest="file")
	parser.add_argument("-c","--conserved", dest="conserved")
	parser.add_argument("-r","--removed",dest="removed")
	parser.add_argument("-t","--thresh",dest="threshold")	
	args = parser.parse_args()
	if args.dir!=None:
		os.chdir(args.dir)
## Attribution des valeurs par défaut pour chaque variable si argument == None
	if args.conserved==None:
		args.conserved="seq_conservées"
	if args.removed==None:
		args.removed="seq_retirées"
	if args.threshold==None:
		args.threshold=0.3
	return (args.file,args.removed,args.conserved,args.threshold)

#### Entry ####
## Vérification de la nature du nom donné
## Vérification de l'existence du fichier (pour savoir si on peut le lire)
def entry(arg):
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
			nom=arg
	return nom

#### thresh ####
## Vérification de la nature de la variable "threshold" et attribution de la valeur de threshold
def thresh(arg):

# Si l'utilisateur n'entre pas de float dans la liste des arguments, le choix par défaut est appliqué
	threshold=arg

# On teste si l'input de l'utilisateur est bien un nombre
	try:
		float(threshold)
	except ValueError:
		print("Vous n'avez pas rentré de nombre.\nFermeture du programme")
		sys.exit(0)
	else:
		threshold=float(threshold)
	
# Si le threshold est >1, le programme assume que l'utilisateur a rentré une valeur en pourcentage
	if threshold > 1:
		threshold = threshold/100
	
# Si le threshold est <1, le programme quitte indiquant un message d'erreur
	elif threshold < 0:
		print("Vous avez rentré un threshold négatif.\nFermeture du programme")
		sys.exit(0)
	return threshold

#### extract ####
def extract(nom,threshold):
# On convertit le fichier fasta en dictionnaire
	data=SeqIO.index(nom,"fasta")

# On sauvegarde le nom des clés pour la boucle
	keys=list(data.keys())

	remove=[]
	conserve=[]

	cons_seq=[]
	rm_seq=[]
	
# Première boucle: on passe la séquence en string et on compte le nombre de X dans la séquence
	for nom_seq in keys:
		sequence=str(data[nom_seq].seq)
		nb_X=sequence.count("X")

# Calcul du ratio
		ratio=nb_X/len(sequence)

# Si le ratio est > au threshold, on ajoute le nom de la séquence à la liste retire sinon dans la liste conserve
		if ratio > threshold:
			remove.append(nom_seq)
			rm_seq.append(nom_seq+">"+sequence)
		else:
			conserve.append(nom_seq)
			cons_seq.append(nom_seq+">"+sequence)
	return (conserve,remove,cons_seq,rm_seq)


#### Output ####
## Vérification de l'existence du fichier (pour pas l'écraser au cas ou)

def output(arg):
	try:
		str(arg)
	except AttributeError:
		print("Vous n'avez pas entré de chaîne de caractère.\nFermeture du programme")
		sys.exit(0)
	else:
		try:
			f=open(arg,"r")
		except FileNotFoundError as e:
			nom_output=arg
		else:
			print("Attention, ce fichier ",e.filename," existe déjà\nFermeture du programme\n")
			sys.exit(0)
	return nom_output

#### save_txt ####
## Ecriture des données obtenues en txt
def save_txt(contenu,output):
	f=open(output+".txt","w")
	f.write("\n".join(sorted(contenu)))
	f.close()

#### save_fasta ####
## Écriture des données obtenues en fasta

def save_fasta(nom,seq):
	seq=sorted(seq)
	o=open(nom+".fasta","w")
# On ajoute un ">" au début de la ligne
	for ele in seq:
		i=0
		o.write(">")
# Tant qu'on ne rencontre pas une autre séq, on écrit tout (on écrit donc le titre)
		while ele[i] != ">":
			o.write(ele[i])
			i+=1
# On saute de ligne pour commencer à écrire la séquence
		o.write("\n")
# ele contenant le titre, un ">" et la séquence, il faut prendre en comptre le i pour bien organiser le fichier
		for j in range(i+1,len(ele)-(i+1)):
			o.write(ele[j])
			if j-i == 80:
				o.write("\n")
			elif (j-i) % 80 == 0 and (j-i) != 0:
				o.write("\n")
			if j == len(ele)-(i+2):
				o.write("\n")
	o.close()
