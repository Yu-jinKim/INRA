# KIM Yujin
# 02/08/16

#### Concaténation des ReadsPerGene ####

#### fonction ####

## Calculer la somme des reads bruts pour les différents résultats de STAR (fichiers ReadsPerGenes.out.tab)

#### Arguments ####

## [-d] = répertoire de sortie
## [-f] = noms des fichiers à concaténer (les fichiers doivent être dans le même format, même longueur et doivent avoir les mêmes noms pour les lignes)
## [-o] = nom du fichier de sortie

#### Imports ####

import sys
import module_conc_RPG

########################################################################################################################################################

# Sauvegarde des arguments d'intérêt
files, output = module_conc_RPG.arguments(sys.argv)

# Récupération du contenu du fichier
files=module_conc_RPG.read(files)

# Traitement des données
names,sums,len_line=module_conc_RPG.sum_lines(files)

# Sauvegarde des données
module_conc_RPG.save(names,sums,output,len_line)
