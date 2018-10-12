#### Fonction ####
# Calculer les Ka/Ks et récupérer les lignes avec une sélection positive (ratio>1)

###############################################################################################

setwd("/home/yujin/Documents/FPKM/analyse/Paires_de_gènes")
donnees=read.table("Minc3_kaks_formated.collinearity",sep="\t")
calcul=subset(donnees,as.numeric(donnees[,4])!=0.00000)
calcul=subset(calcul,as.numeric(calcul[,5])!=0.00000)
calcul=subset(calcul,calcul[,5]>0.01)
calcul=subset(calcul,calcul[,5]<1)
ratio=calcul[,4]/calcul[,5]
calcul[,8]=ratio
res=subset(calcul,calcul[,8]>1)
colnames(res)=c("gene1","gene2","E-value","Ka","Ks","%_id_nuc","%_id_prot","Ka/Ks")
write.table(res,"paires_gènes_KaKs",row.names = F,quote = F,sep="\t")
