# KIM Yujin
# 05/07/2016

#### Log10 Tableau 2D ####

#### Fonction du code ####

# Prend en entrée un tableau de valeurs en 2D (tableau FPKM 10 colonnes)
# Applique un log10 sur les valeurs d'un tableau en 2D
# Donne en sortie le même tableau sauvegardé sous un autre nom avec les valeurs log10 dans le répertoire dans lequel se trouve le programme

#### Pré-requis ####

# A besoin du module module_python dans le même répertoire

#### Arguments ####

# [-d]: répertoire de travail
# [-f]: fichier à analyser 
# [-o]: fichier de sortie

#### Imports ####
		
import sys			
import module_log10	

########################################################################################################################################################

# On demande le nom du fichier à analyser
raw_data,output = module_log10.arguments(sys.argv)				

# On fait tout le boulot
module_log10.traitement(raw_data,output)
	


