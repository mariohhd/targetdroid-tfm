config = {
  'ini_path': '/home/mariohhd/.android/avd/',
  'telnet_timeout': 5,
  'emulator': 'android23',
  'sdk_version': 'android-10',
  'port': 5554,
  'ip': '127.0.0.1'
}

def set(k, v):
  config[k] = v

def get(k):
  return config[k]