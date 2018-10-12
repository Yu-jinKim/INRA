# KIM Yujin
# 21/07/2016

# Après avoir obtenu les numéros des lignes correspondant aux gènes dans le hclust, faut retrouver les noms des gènes pour analyser les paires de gènes

#### Num_accession ####

# Dico pour associer numéro ligne et nom

## Fonction ##

# Obtention d'une liste avec les noms des gènes appartenant à chaque groupe

## Arguments ##

# [-d]: répertoire de travail
# [-n]: nom du fichier Log10... filtré (utilisé à la base du hclust)
# [-g]: nom du fichier contenant la liste des numéro de lignes (plusieurs arguments possibles)
# [-o]: nom du fichier de sortie

## Besoin ##

# Le fichier indiqué avec [-n] doit se trouver dans le repertoire de travail (amélioration à faire)

## Imports ##

import sys
import os, getopt
import module_num_accession

########################################################################################################################################################

fichier_names,fichier_numbers,nom_sortie=module_num_accession.arguments(sys.argv)

names=module_num_accession.entry_names(fichier_names)

numbers=module_num_accession.read_groups(fichier_numbers)

dico=module_num_accession.dico(names)

groupe=module_num_accession.output(dico,numbers)
 
module_num_accession.save(groupe,nom_sortie)







