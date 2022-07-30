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

print("Start unifi info from host "+ C_HOST +" With User "+ C_User+" ,checking version "+ C_VERS)
c = Controller(str(C_HOST), C_User, C_Pass, port=C_PORT, ssl_verify=False, version=C_VERS)
for ap in c.get_aps():
   print('AP named %s with MAC %s' % (ap.get('name'), ap['mac']))
