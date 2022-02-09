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

driver.find_element(By.CSS_SELECTOR,'#truste-consent-button').click()
sleep(3)


# day_date = driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/main/div[1]/section')
# print(day_date.text)
# sleep(2)

#/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[1]/div/div[1]/h3/span  
#/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[2]/div/div[1]/h3/span
#/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[3]/div/div[1]/h3/span
#/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[4]/div/div[1]/h3/span



                        
                                 
# button =  driver.find_element(By.XPATH,f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[3]/summary')
# button.click()   

for i in range(1,11):         
    sleep(1)           
                                             #/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[4]/summary
    button =  driver.find_element(By.XPATH,f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[{i}]/summary').click()
    sleep(1)        
    day_date = driver.find_element(By.XPATH,f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[{i}]/div/div[1]/h3/span')
    print(day_date.text)
    sleep(3)

# button = driver.find_element(By.XPATH,f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[4]/summary')

# description = driver.find_element(By.XPATH,F'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[4]/div/div[1]/p')
# print(description.text)
# sleep(2)



                                       







#day_date = driver.find_element(By.XPATH,f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[2]/summary')
#day_date = driver.find_element(By.XPATH,f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[2]/div/div[1]/h3/span')
#print(day_date.text)
#sleep(2)
# for i in range(1,11):
   
#     sleep(3)
#     day_date = driver.find_element(By.XPATH,f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[{i}]/div/div[1]/h3/span')

#     print(day_date)
    # sleep(2)
    # day_temperatures = driver.find_element_by_xpath(f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[{i}]/div/div[1]/div/div[1]/span')
    
                                                        
    # sleep(2)
    # night_temperatures = driver.find_element_by_xpath(f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[{i}]/div/div[3]/div/div[1]/span')
    
    # sleep(2)
    # get_day_description = driver.find_element_by_xpath(f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[{i}]/div/div[1]/p')
    
    # sleep(2)
    
    # get_night_description = driver.find_element_by_xpath(f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[{i}]/div/div[3]/p')
    
    
    # sleep(5)

    # day, space, date = day_date.text.partition(' ')
    # print(day)
    # print(day_temperatures.text)
    # print("N Temp: ", night_temperatures.text)
    # print("DAY: ", get_day_description.text)
    # print("NIGHT: ",get_night_description.text)
    
    # sleep(5)
    # #driver.find_element_by_css_selector(f'#detailIndex{i} > summary > div > svg').click()
    # #sleep(4)

