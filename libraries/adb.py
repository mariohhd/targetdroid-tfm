from subprocess import call
from adb_parser import parse_adb_command

intent_start = ['adb', 'shell', 'am', 'start']
intent_startservice = ['adb', 'shell', 'am', 'startservice']
intent_broadcast = ['adb', 'shell', 'am', 'broadcast']
 

def execute_adb(event):
  commands = parse_adb_command(event['action'])
  print '> ' + str(event['action'])
  for cmd in commands:
    print '> ' + cmd
    call(cmd.split())

def execute_intent(event):
  params = event['params'].split()
  if event['type'] == 'start':
    print '> ' + ' '.join(intent_start) + ' '.join(params)
    call(intent_start + params)
  if event['type'] == 'start_service':
    print '> ' + ' '.join(intent_startservice) + ' '.join(params)
    call(intent_startservice + params)
  if event['type'] == 'broadcast':
    print '> ' + ' '.join(intent_broadcast) + ' '.join(params)
    call(intent_broadcast + params) 
