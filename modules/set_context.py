import numbers
from collections import OrderedDict
from libraries.telnet import execute
import utils

alll = ['geo fix', 'sms']

def format_values(values):
  if isinstance(values, list):
    return ' '.join(values)
  else:
    return str(values)

def event2command(event):
  commands = []
  c = ''
  format_event(event, c, commands)
  return commands


def format_event(event, c, commands):
  for o in event:
    a = c + o + ' '
    if type(event[o]) is OrderedDict:
      if(a.strip() in alll):
        for o2 in event[o]:
          a = a + format_values(event[o][o2]) + ' '
        commands.append(a)
        continue
      else:
        format_event(event[o], a, commands)
    else:
      a = a + format_values(event[o]) + ' '
      commands.append(a)

def inject_events(context):
  for event in context:
    telnet = event2command(context)
    execute(telnet)