import sys
import telnetlib, socket
import time
import utils

timeout = 5

def execute(events):
  ip = utils.get_config('ip')
  port = utils.get_config('port')
  try:
    telnet = telnetlib.Telnet(ip, port)
    for event in events:
      # read until it is ready to interact
      telnet.read_until('OK', timeout)
      c = event.strip()+ '\r\n'
      telnet.write(c.encode('utf-8'))
      print "Sending event to the clone cloud -> " + event
      #time.sleep(0.1)
      #time.sleep(1)
    telnet.close()
  except socket.error:
    print "Error: cannot connect to the cloud..."
  except EOFError:
    print "Error: cannot connect to the cloud..."