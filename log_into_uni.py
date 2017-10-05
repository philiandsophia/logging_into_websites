# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:30:27 2017

@author: choip
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading



ID = input('ID: ')
my_password = input('Password: ')

ID_email = ID +'@uwo.ca'

fp=webdriver.FirefoxProfile('C:/Users/choip/AppData/Roaming/Mozilla/Firefox/Profiles/ymu2jqak.for_web_scraping')

def log_into_uwo_mail():
    browser = webdriver.Firefox(fp)
    browser.get('https://adfs.uwo.ca/adfs/ls/?wa=wsignin1.0&wtrealm=urn:federation:MicrosoftOnline&wctx=bk%253D1406747354%2526LoginOptions%253D3')
    id_field = browser.find_element_by_id('userNameInput')
    password = browser.find_element_by_id('passwordInput')
    id_field.send_keys(ID_email)
    password.send_keys(my_password)
    
    submit_button = browser.find_element_by_id('submitButton')
    submit_button.click()
    
    time.sleep(3)
    
    email_button = browser.find_element_by_id('ShellMail_link_text')
    email_button.click()


def log_into_owl():
    browser=webdriver.Firefox(fp)
    browser.get('https://owl.uwo.ca/portal/site/%7Eychoi327/tool/32869786-035c-491e-b701-5c3b503073a8')
    id_field = browser.find_element_by_id('eid')
    password = browser.find_element_by_id('pw')
    id_field.send_keys(ID)
    password.send_keys(my_password)
    submit_button = browser.find_element_by_id('submit')
    submit_button.click()

threadobj = threading.Thread(target = log_into_uwo_mail)
threadobj.start()
log_into_owl() 
