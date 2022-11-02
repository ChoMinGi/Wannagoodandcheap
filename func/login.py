import pandas as pd
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(3)

driver.get('https://corearoadbike.com/mypage/')

driver.find_element_by_name('login_id').send_keys('whrowhrl')
driver.find_element_by_name('login_pw').send_keys('test111')
