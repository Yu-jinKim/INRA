#### Fonction ####
# Retire les valeurs du filtre low_complexity du tableau de base et sauvegarde le nouveau fichier

setwd("/home/yujin/Documents/FPKM/analyse/filtre_low_complexity/")
remove=read.table("seq_retirées.txt")

setwd(dir = "/home/yujin/Documents/Analyse_triplicats/results/")
data=read.table("log10_FPKM_filtered",h=T)

# On retire les lignes du fichier remove du le fichier data
res=subset(data,is.element(data[,1],remove$V1)==F)

write.table(res,"Log10_FPKM_filtre_complet",quote=F,row.names = F,sep="\t")
