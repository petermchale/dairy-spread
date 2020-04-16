import sys

def fetch_data_core(line):  
  chromosome, start, end, annotation_ = line.strip().split('\t')[:4]
  url = 'http://localhost:5000/?locus={}:{}-{}'.format(chromosome, start, end)
  keys = []
  values = []
  for key_value in annotation_.split(';'): 
    key, value = key_value.split('=') 
    keys.append(key) 
    values.append(value) 
  return url, keys, values 

def fetch_url_annotation(line): 
  url, _, annotation = fetch_data_core(line)
  return [url] + annotation 

def fetch_header(line): 
  _, header, _ = fetch_data_core(line)
  return header 

def fetch_data(bed_filename): 
  urls_annotations = []
  header_not_fetched = True
  with open(bed_filename) as f:
    for line in f:
      if line.startswith('#gffTags'): 
        continue
      if header_not_fetched: 
        header = fetch_header(line) 
        header = [['locus'] + header]
        header_not_fetched = False 
      url_annotation = fetch_url_annotation(line) 
      urls_annotations.append(url_annotation) 

  return header, urls_annotations

if __name__ == '__main__': 
  print(fetch_data(sys.argv[1]), file=sys.stderr)
