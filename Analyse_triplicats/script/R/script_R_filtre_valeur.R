setwd("/home/yujin/Documents/Analyse_triplicats/results")
donnees=read.table("log10_FPKM.txt",h=T)

#Récupération des valeurs dont le log10(FPKM) > 2.5 à tous les stades
data<-donnees[,2:ncol(donnees)]
rownames(data)<-donnees[,1]		# La colonne des noms de gènes passe dans les rownames (elle n'est plus prise en compte dans le comptage des col)

res1=rowSums(data>2.5)			# On récupère les sommes des TRUE pour cette condition
result1=which(res1==12)			# On récupère les noms des gènes pour lesquels la somme est égale à 9

# Récupération des valeurs dont le log10(FPKM) < 0.3 à tous les stades
res2=rowSums(data<0.3)
result2=which(res2==12)

f_result=result1
f_result=append(f_result,result2)
f_result=as.data.frame(f_result)
result=donnees[-c(f_result[,1]),]
colnames(result)=colnames(donnees)
write.table(result,"log10_FPKM_filtered",quote=F,row.names = F,col.names = T,sep="\t")
