from subprocess import call
from adb_parser import parse_adb_command

intent_start = ['adb', 'shell', 'am', 'start']
intent_startservice = ['adb', 'shell', 'am', 'startservice']
intent_broadcast = ['adb', 'shell', 'am', 'broadcast']
 

def execute_adb(event):
  command = parse_adb_command(event['action'])
  print '> ' + event + ': ' + command
  call(command.split())

def execute_intent(event):
  params = event['params'].split()
  if event['type'] == 'start':
   call(intent_start + params)
  if event['type'] == 'start_service':
   call(intent_startservice + params)
  if event['type'] == 'broadcast':
   call(intent_broadcast + params) 
