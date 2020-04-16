bed="test.bed"
credentials="credentials.json"
my_email="peter.thomas.mchale@gmail.com"

python create_spreadsheet.py \
  --bed ${bed} \
  --title "test data" \
  --credentials ${credentials} \
  --email ${my_email} 
