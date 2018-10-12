#### Imports ####

import sys, os, argparse

########################################################################################################################################################

#### arguments ####
def arguments(arg):
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--directory",dest="dir")
	parser.add_argument("-k","--kaks",dest="kaks_file")
	parser.add_argument("-g","--group_file", dest="group_file")
	parser.add_argument("-o","--output",dest="output")
	args = parser.parse_args()
	if args.dir!=None:
		os.chdir(args.dir)
	return (args.kaks_file,args.group_file,args.output)

#### read ####
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

#### comp ####
def comp(kaks,groups):
	res=[]
	for i in range(0,len(groups)):
		line_groups=groups[i].split()
		for j in range(0,len(kaks)):
			line_kaks=kaks[j].split()
			if line_groups[0] == line_kaks[0] and line_groups[1] == line_kaks[1]:
				res.append(groups[i].strip()+"\t"+line_kaks[7])
	return res

#### save ####
## Sauvegarde du fichier
def save(arg,out):

## Attribution de valeur par défaut à l'output
	if out == None:
		out="positive_selection_pairs_with_expression_pattern"
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


