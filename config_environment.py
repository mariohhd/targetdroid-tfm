from emulator import start_emulator
import utils

options = []


def format_network(event):
  for o in event:
    if o == 'DNS':
      options.extend(['-dns-server', event[o]])

def config_environment(context):
  utils.filter(context)
  utils.get_config('emulator')
  for event in context:
    if event == 'network':
      format_network(context[event])
  start_emulator(options)