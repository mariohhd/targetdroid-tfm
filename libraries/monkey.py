from subprocess import call
import config
 
def cp_script(path):
  emulator = 'emulator-' + config.get('port')
  command = 'adb -s ' + emulator + ' push ' + path + ' /sdcard/script.txt'
  call(command.split())

def run_script(package):
  emulator = 'emulator-' + config.get('port')
  command = 'adb -s ' + emulator + ' shell monkey -p ' + package + ' -f /sdcard/script.txt 1 > /dev/null'
  call(command)

def execute_monkey(event):
  cp_script(event['path'])
  run_script(event['package'])
