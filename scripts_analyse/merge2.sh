# Merger les séquences avant le SortmeRNA
# Single Thread donc à lancer séparément pour optimiser le temps

sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160720_J3/J3-1_S4_R1_001_clean.fastq asexevol_clean_fastq_20160720_J3/J3-1_S4_R2_001_clean.fastq J3_mito/J3-1_S4_R1R2_001_clean2.fastq
sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160720_J3/J3-2_S5_R1_001_clean.fastq asexevol_clean_fastq_20160720_J3/J3-2_S5_R2_001_clean.fastq J3_mito/J3-2_S5_R1R2_001_clean2.fastq
sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160720_J3/J3-3_S6_R1_001_clean.fastq asexevol_clean_fastq_20160720_J3/J3-3_S6_R2_001_clean.fastq J3_mito/J3-3_S6_R1R2_001_clean2.fastq

sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160720_Fem/Fem1_S1_R1_001_clean.fastq asexevol_clean_fastq_20160720_Fem/Fem1_S1_R2_001_clean.fastq Fem_mito/Fem1_S1_R1R2_001_clean2.fastq
sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160720_Fem/Fem2_S2_R1_001_clean.fastq asexevol_clean_fastq_20160720_Fem/Fem2_S2_R2_001_clean.fastq Fem_mito/Fem2_S2_R1R2_001_clean2.fastq
sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160720_Fem/Fem3_S3_R1_001_clean.fastq asexevol_clean_fastq_20160720_Fem/Fem3_S3_R2_001_clean.fastq Fem_mito/Fem3_S3_R1R2_001_clean2.fastq

sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160718_J2/J2-1_S1_R1_001_clean.fastq asexevol_clean_fastq_20160718_J2/J2-1_S1_R2_001_clean.fastq J2_mito/J2-1_S1_R1R2_001_clean2.fastq
sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160718_J2/J2-2_S2_R1_001_clean.fastq asexevol_clean_fastq_20160718_J2/J2-2_S2_R2_001_clean.fastq J2_mito/J2-2_S2_R1R2_001_clean2.fastq
sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160718_J2/J2-3_S3_R1_001_clean.fastq asexevol_clean_fastq_20160718_J2/J2-3_S3_R2_001_clean.fastq J2_mito/J2-3_S3_R1R2_001_clean2.fastq

sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160718_W/W1_S4_R1_001_clean.fastq asexevol_clean_fastq_20160718_W/W1_S4_R2_001_clean.fastq W_mito/W1_S4_R1R2_001_clean.fastq
sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160718_W/W2_S5_R1_001_clean.fastq asexevol_clean_fastq_20160718_W/W2_S5_R2_001_clean.fastq W_mito/W2_S5_R1R2_001_clean.fastq
sh /home/Tools/sortmerna-2.1-linux-64/scripts/merge-paired-reads.sh asexevol_clean_fastq_20160718_W/W3_S6_R1_001_clean.fastq asexevol_clean_fastq_20160718_W/W3_S6_R2_001_clean.fastq W_mito/W3_S6_R1R2_001_clean.fastq

