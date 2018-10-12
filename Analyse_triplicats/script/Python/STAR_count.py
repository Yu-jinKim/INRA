## KIM Yujin
## 04/08/16

#### STAR_count ####

#### Fonction ####

## Calculer les reads de chaque fichier (STAR: ReadsPerGenes)
## Ecrire le fichier concaténé

#### Arguments ####

## [-d]: répertoire de travail
## [-f]: fichiers à traiter (ATTENTION L'ORDRE D'ENTRÉE DÉTERMINE L'ORDRE DE SORTIE)
## [-o]: nom du fichier de sortie

#### ATTENTION CE CODE EST FORMATÉ POUR ACCEUILLIR LES FICHIERS FINAL.LOG DE STAR ####

#### Imports ####

import sys, module_STAR_count

########################################################################################################################################################

files, output = module_STAR_count.arguments(sys.argv)

files = module_STAR_count.read(files)

sums, names = module_STAR_count.sum_col(files)

module_STAR_count.save(names,sums,output)
