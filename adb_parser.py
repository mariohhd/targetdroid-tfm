adb_commands = {
  'connect_wifi':['adb shell setprop service.adb.tcp.port 5555 && stop adbd && start adbd',
                  'adb connect'
                 ],
  'lock_screen': ['adb shell input keyevent 6',
                  'adb shell input keyevent 26'
                 ],
  'unlock_screen' : ['adb shell input keyevent 82'],
  'volume_up': ['adb shell input keyevent 25'],
  'go_home': ['adb shell input keyevent 3'],
  'take_screenshot': ['adb shell screenshot /sdcard/screenshot.png'],
  'start_clock_app': ['adb shell am start com.google.android.deskclock'],
  'stop_clock_app': ['adb shell am force-stop com.google.android.desclock'],
  'start_wifi': ['adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings'],
  'wifi_status': ['adb shell am start -n com.android.settings/.wifi.WifiStatusTest'],
  'enable_wifi': ['adb shell svc wifi enable'],
  'disable_wifi': ['adb shell svc wifi disable'],
  'enable_mobile_data': ['adb shell svc data enable'],
  'disable_mobile_data': ['adb shell svc data disable']
}

def parse_adb_command(name):
  return adb_commands[name]