config = {}
filters = ['t']

def set_config(k, v):
  config[k] = v

def get_config(k):
  return config[k]

def filter(o):
  print o
  for f in filters:
    print str(hasattr(o, f)) + '---f='+f
    if hasattr(o, f):
      print 'removing --- t=' + o[f]
      del o[f]