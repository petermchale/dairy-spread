import sys
import os

def get_url(chromosome, start, end): 
  return 'http://localhost:5000/?locus={}:{}-{}'.format(chromosome, start, end)

def fetch_data_core(line):  
  try: 
    chromosome, start, end, annotation_ = line.strip().split('\t')[:4]
    keys = []
    values = []
    for key_value in annotation_.split(';'): 
      key, value = key_value.split('=') 
      keys.append(key) 
      values.append(value) 
    return get_url(chromosome, start, end), keys, values 
  except ValueError: 
    chromosome, start, end = line.strip().split('\t')[:3]
    return get_url(chromosome, start, end), [], []

def fetch_url_annotation(line): 
  url, _, annotation = fetch_data_core(line)
  return [url] + annotation 

def fetch_header(line): 
  _, header, _ = fetch_data_core(line)
  return header 

def fetch_data(bed_filename): 
  if os.stat(bed_filename).st_size == 0: 
    return [[]], [[]]
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
