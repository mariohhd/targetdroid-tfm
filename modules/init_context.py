import sys, os, inspect, signal, StringIO
from subprocess import Popen, PIPE, STDOUT, call
from modules.set_context import inject_events
from libraries.utils import filter

def install_app(src):
  call(['adb', 'install', src])

def init_context(context):
  #filter(context)
  for event in context:
    if event == 'install_app':
      install_app(context[event])
    else:
      a = {}
      a[event] = context[event]
      inject_events(a)
