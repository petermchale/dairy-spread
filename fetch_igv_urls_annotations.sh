missed_SVs="/scratch/ucgd/lustre-work/quinlan/u6018199/chaisson_2019/analysis/call_visualizations/manta_0.75_svabaContigs/HG00514.DEL.gt100.lt105.minus_1bp.manta/HG00514.BIP-unified.filtered.DEL.gt100.lt105.minus_1bp.manta.graphite" 
sort --version-sort -k1,1 -k2,2 "${missed_SVs}.bed" > "${missed_SVs}.sorted.bed" 
python fetch_igv_urls_annotations.py "${missed_SVs}.sorted.bed" 
