from subprocess import call
from adb_parser import parse_adb_command


def execute_adb(event):
  command = parse_adb_command(event)
  print '> ' + event + ': ' + command
  call(command.split())