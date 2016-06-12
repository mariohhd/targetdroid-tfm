from emulator import start_emulator
import utils, config

options = []


def format_network(event):
  for o in event:
    if o == 'DNS':
      options.extend(['-dns-server', event[o]])

def config_ini():
  #utils.write_file(config.get('ini_path')+config.get('emulator')+'.ini', ['asdasdasd:\tasdasdasd'])
  file = utils.read_file(config.get('ini_path')+config.get('emulator')+'.ini')

def config_environment(context):
  config_ini()
  for event in context:
    if event == 'network':
      format_network(context[event])
  start_emulator(options)