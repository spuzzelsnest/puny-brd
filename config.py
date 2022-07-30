#requirements: pip3 install pyunifi selenium
from platform import python_version
import sys
from pyunifi.controller import Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def clear_cache():
    print("Clear Cache/ Refresh browser")
    print("Current Python Version-", python_version())
    print("System Version", sys.version)

#    driver = webdriver.Chrome()
#    driver.get('chrome://settings/clearBrowserData')
#    driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
#    driver.refresh()

def unifi_info():
   print("start unifi info")
   c = Controller('192.168.10.6', 'ubnt', 'ipkJRVAsj2gPcfIz', port='443', ssl_verify=False, version='unifiOS')

   for ap in c.get_aps():
      print('AP named %s with MAC %s' % (ap.get('name'), ap['mac']))