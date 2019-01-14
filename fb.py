#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as dc
import getpass

email_id=raw_input("Enter email id : ")
pswd = getpass.getpass('Password:')

caps=dc.FIREFOX.copy()
caps["marionette"]=False
driver=webdriver.Firefox(capabilities=caps)
driver.get("https://www.facebook.com")


username = driver.find_element_by_name('email')
username.send_keys(email_id)
password = driver.find_element_by_name('pass')
password.send_keys(pswd)

driver.find_element_by_id("u_0_3").submit()


