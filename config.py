#requirements: pip3 install pyunifi selenium
import os, sys, ssl
from platform import python_version
from dotenv import load_dotenv
from pyunifi.controller import Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv()

C_HOST = os.getenv('IP_Controller')
C_PORT = os.getenv('Port')
C_USER = os.getenv('Username')
C_PASS = os.getenv('Password')
C_VERS = os.getenv('Version')

def sys_specs():
   print("Current Python Version-"+ python_version())
   print("System Version"+ sys.version)

def unifi_info():
   print("Start unifi info from host "+ C_HOST +" ,checking version "+ C_VERS) 
   c = Controller(str(C_HOST), C_USER, C_PASS, port=C_PORT, ssl_verify=False, version=C_VERS)
   for ap in c.get_aps():
      print('AP named %s with MAC %s' % (ap.get('name'), ap['mac']))