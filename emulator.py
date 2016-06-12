import sys, os, inspect, signal, StringIO
from subprocess import Popen, PIPE, STDOUT, call
from time import sleep
import utils


def start_emulator(options):
  emulator_name = utils.get_config('emulator')
  emulator_port = utils.get_config('port')
  adb_device_name = 'emulator-' + emulator_port
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
  emulator_port = utils.get_config('port')
  adb_device_name = 'emulator-' + emulator_port
  call(['adb', '-s', adb_device_name, 'emu', 'kill'])