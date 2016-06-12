import sys, os, inspect, signal, StringIO
from subprocess import Popen, PIPE, STDOUT, call
from json2telnet import set_context
import utils



def install_app(src):
  call(['adb', 'install', src])

def config_os(context):
  utils.filter(context)
  for event in context:
    if event == 'install_app':
      install_app(context[event])
    else:
      a = {}
      a[event] = context[event]
      set_context(a)
