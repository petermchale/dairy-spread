import sys

def fetch_igv_urls_annotations(bed_filename): 
  igv_urls = []
  annotations = []
  with open(bed_filename) as f:
    for line in f:
      chromosome, start, end, annotation = line.split('\t')[:4]
      igv_urls.append(['http://localhost:5000/?locus={}:{}-{}'.format(chromosome, start, end)])
      annotations.append([annotation.strip()])
  return igv_urls, annotations

if __name__ == '__main__': 
  print(fetch_igv_urls_annotations(sys.argv[1]), file=sys.stderr)
