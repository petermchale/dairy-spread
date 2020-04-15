import random
import sys

def fetch_igv_urls(bed_filename): 
  max_number_SVs = 10
 
  with open(bed_filename) as f:
    all_lines = f.readlines()
   
  sample_size = min(len(all_lines), max_number_SVs)

  sorted_sample_of_lines = [
    all_lines[i] for i in sorted(random.sample(range(len(all_lines)), sample_size))
  ]
 
  igv_urls = []
  for line in sorted_sample_of_lines:
    print(line, end='', file=sys.stdout)
    chromosome, start, end = line.split('\t')[:3]
    igv_urls.append(['http://localhost:5000/?locus={}:{}-{}'.format(chromosome, start, end)])
   
  return igv_urls

if __name__ == '__main__': 
  print(fetch_igv_urls(sys.argv[1]), file=sys.stderr)
