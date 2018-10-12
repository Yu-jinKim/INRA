# KIM Yujin
# 19/07/16

#### Filtre paires de gènes ####

#### Fonction ####

# Trouver les gènes éliminés dans les différents filtres et éliminer les paires qui contiennent un des deux membres filtré

#### Besoins ####

# Fichier avec les paires de gènes en 2 colonnes
# Fichier avec noms des gènes filtré (tableau FPKM filtré complet)

#### Arguments ####

# [-d]: répertoire de travail
# [-p]: adresse du fichier avec les deux colonnes
# [-g]: adresse du fichier avec la liste des gènes "survivants"
# [--output_filtre]: nom du fichier de base sans les gènes filtrés
# [--output_retires]: nom du fichier contenant la liste des gènes retirés
# [--output_conserves]: nom du fichier contenant la liste des gènes conservés

#### Imports ####

import module_paires
import sys

########################################################################################################################################################

# On récupère les arguments et on les attribue à des variables
fichier_paires, fichier_genes, output_filtre, output_retires, output_conserves=module_paires.arguments(sys.argv)

# On récupère les colonnes 1, 2 du fichier "paires"
pair_1,pair_2=module_paires.entry_paires(fichier_paires)

# On récupère la première colonne sans le titre
names_genes=module_paires.entry_names(fichier_genes)

# On compare les colonnes entre elles
conserve,remove=module_paires.comp(pair_1,pair_2,names_genes)

# On prépare le fichier filtré
liste_conserve=module_paires.filtre_pair(conserve,fichier_paires)

# On sauvegarde les fichiers à enregistrer
module_paires.save_names(remove,output_retires,fichier_paires)
module_paires.save_names(conserve,output_conserves,fichier_paires)
module_paires.save_filtre(liste_conserve,output_filtre,fichier_paires)


