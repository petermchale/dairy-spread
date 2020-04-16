variants="/scratch/ucgd/lustre-work/quinlan/u6018199/chaisson_2019/analysis/call_visualizations/manta_0.75_svabaContigs/HG00514.DEL.gt100.lt105.minus_1bp.manta/HG00514.BIP-unified.filtered.DEL.gt100.lt105.minus_1bp.manta.graphite.bed"
credentials="/uufs/chpc.utah.edu/common/HIPAA/u6018199/dairy_spread/credentials.json"
my_email="peter.thomas.mchale@gmail.com"

python create_spreadsheet.py \
  --bed ${variants} \
  --title "my variants" \
  --column_heading "annotation" \
  --credentials ${credentials} \
  --email ${my_email} 
