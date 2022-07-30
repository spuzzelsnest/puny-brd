#requirements: pip3 install pyunifi selenium
import os, sys
from platform import python_version
from dotenv import load_dotenv
from pyunifi.controller import Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv()

C_HOST = os.getenv('IP_Controller')
C_PORT = os.getenv('Port')
C_User = os.getenv('Username')
C_Pass = os.getenv('Password')

def clear_cache():
    print("Current Python Version-"+ python_version())
    print("System Version"+ sys.version)

#    driver = webdriver.Chrome()
#    driver.get('chrome://settings/clearBrowserData')
#    driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
#    driver.refresh()

def unifi_info():
   print("start unifi info from host "+ C_HOST)
   c = Controller(str(C_HOST), C_User, C_Pass, port=C_PORT, ssl_verify=False, version='UDMP-unifiOS')
   
   #for ap in c.get_aps():
   #   print('AP named %s with MAC %s' % (ap.get('name'), ap['mac']))