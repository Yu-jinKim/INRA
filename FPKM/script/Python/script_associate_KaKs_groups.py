# KIM Yujin
# 25/07/16

#### associate_KaKs_groups ####

#### Fonction ####

## Croise les paires dans le fichier KaKs filtré et le fichier paires+groupes pour en tirer les gènes avec patrons d'expressions différents et avec sélection positive

#### Arguments ####

# [-d]: nom du répertoire de travail
# [-k]: nom du fichier kaks (avec colonne du ratio Ka/Ks)
# [-g]: nom du fichier avec les paires et les groupes associés
# [-o]: nom du fichier de sortie

#### Imports ####

import sys
import module_associate_KaKs_groups

########################################################################################################################################################

kaks_file,group_file,output=module_associate_KaKs_groups.arguments(sys.argv)

kaks=module_associate_KaKs_groups.read(kaks_file)

groups=module_associate_KaKs_groups.read(group_file)

res=module_associate_KaKs_groups.comp(kaks,groups)

module_associate_KaKs_groups.save(res,output)
