#### Modules ####

import sys, argparse
from math import log10

########################################################################################################################################################

#### arguments ####
def arguments(arg):
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--directory",dest="dir")
	parser.add_argument("-f","--file",dest="raw_data")
	parser.add_argument("-o","--output",dest="output")
	args = parser.parse_args()
	if args.dir!=None:
		os.chdir(args.dir)
	if args.raw_data == None:
		print("Le fichier entrée n'a pas été entré dans la ligne de commande")
		sys.exit(0)
	if args.output==None:
		args.output="log10("+args.raw_data+")"
	return (args.raw_data,args.output)

#### traitement ####

def traitement(raw_data,nom):
# On lit ce fichier dont on récupère tout le contenu
	f=open(raw_data,"r")								
	lines=f.readlines()
	f.close()

# Teste si le fichier existe déjà
	try:
		k=open(nom,"r")	

# S'il n'existe pas on continue le code normalement
	except FileNotFoundError:							
		u=open(nom,"w")

# Écriture de la première ligne du tableau qui ne contient pas de valeur mais qui donne les titres des colonnes
		u.write(lines[0])							

# Première boucle for: on va écrire le nom du gène au début de chaque ligne à partir de la deuxième et on transforme chaque ligne de la liste de la variable lines (string) en tableau (mise en place des indices)
		for i in range(1,len(lines)):
			u.write(lines[i][0:18])
			line=lines[i].split()

# Deuxième boucle for: 
			for j in range(1,len(line)):
			
# On passe chaque valeur du tableau (à partir de [1;1] en coordonnées) en float pour le futur calcul du log10
				line[j]=float(line[j])+1

# Appelle la fonction log10 avec arrondissement à partir des millièmes		
				valeur=round(log10(line[j]),3)

# On écrit la valeur obtenue dans le fichier de sortie			
				u.write(str(valeur)+"\t")

# Quand on atteint la fin de la ligne (détectée par le nombre de colonnes) on met un retour chariot			
				if j == (len(line)-1):						
					u.write("\n")
		print("\nLe fichier a bien été créé\n")
# Fermeture du fichier
		u.close()								
	else:

# Message qui montre que le fichier existe déjà
		print("Veuillez choisir un autre nom pour le fichier de sortie")

# Si le fichier existe, on ferme le programme	
		sys.exit(0)								

