# Prinseq sur les données unmergées (nettoyage poly A/T/N)
# Single Thread à lancer séparément pour optimiser

perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq J3_mito/J3-1_S4_R1_001_clean2.fastq-clean2 -fastq2 J3_mito/J3-1_S4_R2_001_clean2.fastq-clean2 -out_format 3 -log J3_mito/prinseq/J3-1_S4.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  J3_mito/prinseq/J3-1_S4_001_clean2.fastq-good -out_bad J3_mito/prinseq/J3-1_S4_001_clean2.fastq-bad
perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq J3_mito/J3-2_S5_R1_001_clean2.fastq-clean2 -fastq2 J3_mito/J3-2_S5_R2_001_clean2.fastq-clean2 -out_format 3 -log J3_mito/prinseq/J3-2_S5.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  J3_mito/prinseq/J3-2_S5_001_clean2.fastq-good -out_bad J3_mito/prinseq/J3-2_S5_001_clean2.fastq-bad
perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq J3_mito/J3-3_S6_R1_001_clean2.fastq-clean2 -fastq2 J3_mito/J3-3_S6_R2_001_clean2.fastq-clean2 -out_format 3 -log J3_mito/prinseq/J3-3_S6.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  J3_mito/prinseq/J3-3_S6_001_clean2.fastq-good -out_bad J3_mito/prinseq/J3-3_S6_001_clean2.fastq-bad

perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq Fem_mito/Fem1_S1_R1_001_clean2.fastq-clean2 -fastq2 Fem_mito/Fem1_S1_R2_001_clean2.fastq-clean2 -out_format 3 -log Fem_mito/prinseq/Fem1_S1.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  Fem_mito/prinseq/Fem1_S1_001_clean2.fastq-good -out_bad Fem_mito/prinseq/Fem1_S1_001_clean2.fastq-bad
perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq Fem_mito/Fem2_S2_R1_001_clean2.fastq-clean2 -fastq2 Fem_mito/Fem2_S2_R2_001_clean2.fastq-clean2 -out_format 3 -log Fem_mito/prinseq/Fem2_S2.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  Fem_mito/prinseq/Fem2_S2_001_clean2.fastq-good -out_bad Fem_mito/prinseq/Fem2_S2_001_clean2.fastq-bad
perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq Fem_mito/Fem3_S3_R1_001_clean2.fastq-clean2 -fastq2 Fem_mito/Fem3_S3_R2_001_clean2.fastq-clean2 -out_format 3 -log Fem_mito/prinseq/Fem3_S3.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  Fem_mito/prinseq/Fem3_S3_001_clean2.fastq-good -out_bad Fem_mito/prinseq/Fem3_S3_001_clean2.fastq-bad

perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq J2_mito/J2-1_S1_R1_001_clean2.fastq-clean2 -fastq2 J2_mito/J2-1_S1_R2_001_clean2.fastq-clean2 -out_format 3 -log J2_mito/prinseq/J2-1_S1.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  J2_mito/prinseq/J2-1_S1_001_clean2.fastq-good -out_bad J2_mito/prinseq/J2-1_S1_001_clean2.fastq-bad
perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq J2_mito/J2-2_S2_R1_001_clean2.fastq-clean2 -fastq2 J2_mito/J2-2_S2_R2_001_clean2.fastq-clean2 -out_format 3 -log J2_mito/prinseq/J2-2_S2.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  J2_mito/prinseq/J2-2_S2_001_clean2.fastq-good -out_bad J2_mito/prinseq/J2-2_S2_001_clean2.fastq-bad
perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq J2_mito/J2-3_S3_R1_001_clean2.fastq-clean2 -fastq2 J2_mito/J2-3_S3_R2_001_clean2.fastq-clean2 -out_format 3 -log J2_mito/prinseq/J2-3_S3.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  J2_mito/prinseq/J2-3_S3_001_clean2.fastq-good -out_bad J2_mito/prinseq/J2-3_S3_001_clean2.fastq-bad

perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq W_mito/W1_S4_R1_001_clean2.fastq-clean2 -fastq2 W_mito/W1_S4_R2_001_clean2.fastq-clean2 -out_format 3 -log W_mito/prinseq/W1_S4.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  W_mito/prinseq/W1_S4_001_clean2.fastq-good -out_bad W_mito/prinseq/W1_S4_001_clean2.fastq-bad
perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq W_mito/W2_S5_R1_001_clean2.fastq-clean2 -fastq2 W_mito/W2_S5_R2_001_clean2.fastq-clean2 -out_format 3 -log W_mito/prinseq/W2_S5.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  W_mito/prinseq/W2_S5_001_clean2.fastq-good -out_bad W_mito/prinseq/W2_S5_001_clean2.fastq-bad
perl /home/Tools/prinseq-lite-0.20.4/prinseq-lite.pl -fastq W_mito/W3_S6_R1_001_clean2.fastq-clean2 -fastq2 W_mito/W3_S6_R2_001_clean2.fastq-clean2 -out_format 3 -log W_mito/prinseq/W3_S6.log -ns_max_p 0 -trim_qual_type mean -trim_qual_rule lt -trim_qual_right 28 -trim_qual_window 5 -trim_qual_step 1 -trim_tail_right 5 -min_len 60 -verbose -out_good  W_mito/prinseq/W3_S6_001_clean2.fastq-good -out_bad W_mito/prinseq/W3_S6_001_clean2.fastq-bad

