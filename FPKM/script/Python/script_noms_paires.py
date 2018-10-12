# KIM Yujin
# 21/07/16

# J'ai maintenant les noms des gènes pour les branches/groupes, va falloir chercher si des gènes sont exprimés différemment du coup.

#### Noms_paires ####

#### Fonction ####

# Chercher si les paires sont exprimées différemment grâce aux groupes obtenus

#### Arguments ####

# [-d]: répertoire de travail
# [-f]: nom du fichier avec les noms des paires conservées
# [-g]: liste des groupes à analyser (résultat du hclust)
# [-o]: nom du fichier de sortie

#### Imports ####

import os
import sys
import module_noms_paires

########################################################################################################################################################

names,groups,output=module_noms_paires.arguments(sys.argv)

names=module_noms_paires.read(names)

groups=module_noms_paires.read_groups(groups)

res=module_noms_paires.comp(names,groups)

module_noms_paires.save(res,output,groups)

