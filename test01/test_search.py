# coding=utf-8
from config import readconf
from selenium import webdriver
from common.base import Base
import time


driver = webdriver.Firefox()
base_driver = Base(driver)

base_driver.open_url(readconf.index_url)

a = '#kw'
b = 'selenium'
c = '#kw'
d = ''

input_button = "$('"+a+"').val('"+b+"');"
driver.execute_script(input_button)
time.sleep(2)

ss = "$('"+c+"').val('"+d+"');"
driver.execute_script(ss)
