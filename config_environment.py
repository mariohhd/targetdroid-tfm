from emulator import start_emulator
from ini_parser import parse_ini_property
import utils, config

options = []


def format_network(event):
  for o in event:
    if o == 'DNS':
      options.extend(['-dns-server', event[o]])

def set_ini_properties(properties):
  aux = []
  for p in properties:
    line = parse_ini_property(p) + '=' + str(properties[p]) + '\r\n'
    aux.append(line)
  if len(aux) > 0:
    utils.write_file(config.get('ini_path')+config.get('emulator')+'.ini', aux)

def config_environment(context):
  for event in context:
    if event == 'network':
      format_network(context[event])
    if event == 'ini_properties':
      set_ini_properties(context[event])
  start_emulator(options)