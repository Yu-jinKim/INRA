#### Fonction ####
# Retire les valeurs du filtre low_complexity du tableau de base et sauvegarde le nouveau fichier

setwd(dir = "/home/yujin/Documents/FPKM/analyse/")
data=read.table("log10_FPKM_filtered",h=T)
remove=read.table("seq_retirées.txt")

# On retire les lignes du fichier remove du le fichier data
res=subset(data,is.element(data[,1],remove$V1)==F)

write.table(res,"Log10_FPKM_filtre_complet",quote=F,row.names = F,sep="\t")
