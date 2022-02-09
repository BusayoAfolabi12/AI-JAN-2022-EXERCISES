import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By

url = 'https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c'
pth = 'C:\\Users\\busay\\chromedriver\\chromedriver.exe'

driver = webdriver.Chrome(pth)

print(driver.get(url))

sleep(3)

day_date = driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[3]/summary/div/svg')

print(day_date)
sleep(3)