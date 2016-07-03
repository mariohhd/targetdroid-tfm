import numbers
from collections import OrderedDict
from libraries.telnet import execute
from libraries.adb import execute_adb, execute_intent
from libraries.monkey import execute_monkey
import utils

multiple_parameters = ['geo fix', 'sms']

def event2adb_command(events):
  for event in events:
    execute_adb(event)

def event2intent(events):
  for event in events:
    execute_intent(event)

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
      if(a.strip() in multiple_parameters):
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
    if event == 'adb':
      event2adb_command(context[event])
    elif event == 'intents':
      event2intent(context[event])
    elif event == 'monkey':
      execute_monkey(context[event])  
    elif event == 'telnet':
      telnet = event2command(context[event])
      execute(telnet)