## KIM Yujin
## 03/08/16

#### Concaténer ####

#### Fonction ####

## Concaténer les données important des genes.results de RSEM

#### Arguments ####

## [-d][--directory] = répertoire de sortie
## [-f][--file] = noms des fichiers à concaténer (les fichiers doivent être dans le même format, même longueur et doivent avoir les mêmes noms pour les lignes)
## [-o][--output] = nom du fichier de sortie (PATH peut être intégré)
## [-c][--column] = colonne à récupérer

#### ATTENTION À L'ORDRE D'ENTRÉE DES FICHIERS ####

## Ce code est formaté pour créer un fichier du type tableau des FPKM: écriture d'une première ligne avec les stades de développement (on peut changer ça dans la fonction save)
## + récupération d'une partie de la première colonne pour la première colonne du fichier final (On peut changer cela dans la fonction data) 

#### Imports ####

import sys, module_conc

########################################################################################################################################################

# Sauvegarde des arguments d'intérêt
files, output, column = module_conc.arguments(sys.argv)

files=module_conc.read(files)

names_liste,FPKM_liste=module_conc.data(files,column)

module_conc.save(names_liste,FPKM_liste,output)


