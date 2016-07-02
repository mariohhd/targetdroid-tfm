import sys, os, inspect, signal, StringIO
from subprocess import Popen, PIPE, STDOUT, call
from time import sleep
import config

def create_emulator(options):
  name = options['name']
  target = options['sdk_version']
  config.set('emulator', name)
  p = Popen(['android', '-s', 'create', 'avd', '-n', name, '-f', '-t',  target], stdin=PIPE)
  print p.communicate(input='no\n')[0]
  print '> Created new emulator: -name ' + name + ' -sdk-version: ' + target  



def start_emulator(options):
  emulator_name = config.get('emulator')
  emulator_port = config.get('port')
  adb_device_name = 'emulator-' + str(emulator_port)
  emulator = ['emulator', '-avd', emulator_name]

  print "> Created new execution evironment. Wating for emulator..."  
  # Wait for emulator and clean logcat
  emulator.extend(options)
  print "> " + ' '.join(emulator)
  Popen(emulator)

  bootcomplete = None
  count = 0
  while bootcomplete is not 1:
    p = Popen(['adb', '-s', adb_device_name, 'wait-for-device', 'shell', 'getprop', 'sys.boot_completed'], stdout=PIPE)
    out=p.communicate()
    print out
    try:
      bootcomplete = int(str(out[0]).strip())
    except:
      pass
    sleep(2)
    count+=1
    if count % 10 is 0:
      print "Waiting boot completed... ", bootcomplete

def stop_emulator():
  emulator_port = config.get('port')
  adb_device_name = 'emulator-' + str(emulator_port)
  call(['adb', '-s', adb_device_name, 'emu', 'kill'])

def delete_emulator():
  emulator = config.get('emulator')
  call(['android', '-s', 'delete', 'avd', '-n', emulator])

def stop_and_delete_emulator():
  stop_emulator()
  delete_emulator()