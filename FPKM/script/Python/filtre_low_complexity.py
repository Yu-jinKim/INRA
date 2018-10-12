# Yujin KIM
# 12/07/2016

#### Filtre %low complexity ####

#### Fonction du code ####

# Lit un fichier fasta, récupère toutes les séquences pour en compter le nombre de X (résultat du BLAST)
# Calcul du ratio X/total
# Sélectionne les séquences avec un ratio supérieur à un certain threshold

#### Besoins ####

# Fichier FASTA filtré pour zone de faible complexité avec des X (amélioration possible: choix du filtre qui a été appliqué)

#### Paramètres ####

# [-d] = répertoire de travail
# [-f] = nom du fichier en entrée
# [-t] = threshold (valeur en pourcentage ou en ratio, par défaut 0.3)
# [-c] = nom du fichier de sortie pour nom des séquences et fasta des séquences conservées
# [-r] = même chose mais pour séquences retirées

#### Sortie ####

# Deux fichiers contenant le nom des séquences conservées et retirées
# Deux fichiers FASTA contenant les séquences conservées et retirées

#### Imports ####

import sys
import module_low_complexity

##################################################################################################################################################################

# Récupération des arguments
nom,nom_remove,nom_conserve,threshold=module_low_complexity.arguments(sys.argv)

# Nom du fichier
nom=module_low_complexity.entry(nom)

# Threshold
threshold=module_low_complexity.thresh(threshold)

# Extraction de données (séq conservées, retirées et liste de noms)
conserve,remove,cons_seq,rm_seq=module_low_complexity.extract(nom,threshold)

# Vérification sur les noms des fichiers
nom_conserve=module_low_complexity.output(nom_conserve)
nom_remove=module_low_complexity.output(nom_remove)

# Sauvegarde des fichiers de sortie (noms des séquences)
module_low_complexity.save_txt(conserve,nom_conserve)
module_low_complexity.save_txt(remove,nom_remove)

module_low_complexity.save_fasta(nom_remove,rm_seq)
module_low_complexity.save_fasta(nom_conserve,cons_seq)


