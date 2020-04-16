import sys 

def get_url_path(args):
  bed_path = args.bed
  if bed_path.endswith('.bed'):
    return bed_path[:-4] + '.url'
  else:
    print('input file must be in bed format', file=sys.stderr)
    sys.exit()

