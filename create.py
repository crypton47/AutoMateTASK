#! -*- coding:utf-8 -*-

import os
import sys
from selenium import webdriver
path = '/home/crypt0n47/Desktop/Projects/'
browser = webdriver.Chrome()
browser.get("https://github.com/login")
username = os.environ.get('DB_USERNAME')
passwd = os.environ.get('DB_PASSWD')




def create():
    foldername = str(sys.argv[1])
    os.makedirs(path + foldername)
    python_button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    python_button.send_keys(username)
    python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
    python_button.send_keys(passwd)
    python_button = browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[4]")[0]
    python_button.click()
    task = browser.find_elements_by_xpath("/html/body/div[1]/header/div[7]/details/summary")[0]
    task.click()
    task = browser.find_elements_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/a[1]")[0]
    task.click()
    task = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    task.send_keys(foldername)
    task = browser.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
    task.submit()


  



if __name__ == "__main__":
    create()










