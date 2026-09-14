import rssi
import time
import ledshim
from configparser import ConfigParser

config = ConfigParser()
config.read('wifipi.ini')

rssi_scanner = rssi.RSSI_Scan('wlan0')
ssids = ['Avocadasteroid']
poll_interval = 5
ledshim.set_clear_on_exit(True)
ledshim.set_brightness(0.3)

while True:
  ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=False)
  qstring = ap_info[0]["quality"]
  qcomponents = qstring.split("/")
  quality = int(qcomponents[0])
  # print(quality)
  ledshim.set_all(255,0,0)
  for l in range(int(quality*0.4)):
    ledshim.set_pixel(l,0,255,0)
  ledshim.show()
  time.sleep(poll_interval)
