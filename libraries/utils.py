filters = ['t']

def filter(o):
  for f in filters:
    if f in o:
      del o[f]
  return o

def read_file(f):
  try:
    f_object = open(f, 'r')
    try:
      data = f_object.readlines()
      return data
    finally:
      f_object.close()
  except IOError:
    print '> Error opening file ' + f 
    pass

def write_file(f, data):
  try:
    f_object = open(f, 'a')
    try:
      f_object.writelines(data)
    finally:
      f_object.close()
  except IOError:
    print '> Error writing file ' + f
    pass
  