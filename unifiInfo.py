import os, sys
from platform import python_version
from dotenv import load_dotenv
from pyunifi.controller import Controller

load_dotenv()

C_HOST = os.getenv('IP_Controller')
C_PORT = os.getenv('Port')
C_User = os.getenv('Username')
C_Pass = os.getenv('Password')
C_VERS = os.getenv('Version')

def main():

   print("Start unifi info from host "+ C_HOST +" With User "+ C_User+" ,checking version "+ C_VERS)
   c = Controller(str(C_HOST), C_User, C_Pass, port=C_PORT, ssl_verify=False, version=C_VERS)
   for ap in c.get_aps():
      print('Model '+ ap['model'] +' of type '+ ap['type'] )
      print('MAC: '+ ap['mac'])
      print('IP: '+ ap.get('ip'))
      print('-----------------------')
   
      #print('AP named %s with MAC %s ' % (ap.get('name'), ap['mac']))

   for u in c.get_users():
      print('User %s ' % (u.get('hostname') ))

   for conf in c.get_wlan_conf():
      print('Configuered WLANs: '+ conf.get('name'))
      print('Wlan Bands: '+ str(conf.get('wlan_bands')))
      print('Hidden: '+ str(conf.get('hide_ssid')))
main()