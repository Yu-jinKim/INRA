# Création du fichier de référence
#/home/Tools/RSEM-1.2.31/rsem-prepare-reference -p 30 --gtf /home/data/gff3/MiV3.GTF --star --star-path /home/Tools/STAR-2.5/bin/Linux_x86_64/ --star-sjdboverhang 75 /home/data/genome/Meloidogyne_incognita_V3_20131230.fna rsem_reference/Minc

# rsem
/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end W_mito/STAR/W1_Aligned.toTranscriptome.out.bam rsem_reference/ W_mito/rsem/W1
/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end W_mito/STAR/W2_Aligned.toTranscriptome.out.bam rsem_reference/ W_mito/rsem/W2
/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end W_mito/STAR/W3_Aligned.toTranscriptome.out.bam rsem_reference/ W_mito/rsem/W3

/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end J2_mito/STAR/J2-1_Aligned.toTranscriptome.out.bam rsem_reference/ J2_mito/rsem/J2-1
/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end J2_mito/STAR/J2-2_Aligned.toTranscriptome.out.bam rsem_reference/ J2_mito/rsem/J2-2
/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end J2_mito/STAR/J2-3_Aligned.toTranscriptome.out.bam rsem_reference/ J2_mito/rsem/J2-3

/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end J3_mito/STAR/J3-1_Aligned.toTranscriptome.out.bam rsem_reference/ J3_mito/rsem/J3-1
/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end J3_mito/STAR/J3-2_Aligned.toTranscriptome.out.bam rsem_reference/ J3_mito/rsem/J3-2
/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end J3_mito/STAR/J3-3_Aligned.toTranscriptome.out.bam rsem_reference/ J3_mito/rsem/J3-3

/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end Fem_mito/STAR/Fem1_Aligned.toTranscriptome.out.bam rsem_reference/ Fem_mito/rsem/Fem1
/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end Fem_mito/STAR/Fem2_Aligned.toTranscriptome.out.bam rsem_reference/ Fem_mito/rsem/Fem2
/home/Tools/RSEM-1.2.31/rsem-calculate-expression -p 30 --bam --time --alignments --paired-end Fem_mito/STAR/Fem3_Aligned.toTranscriptome.out.bam rsem_reference/ Fem_mito/rsem/Fem3
