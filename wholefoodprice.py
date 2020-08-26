#!/usr/bin/env python3
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from datetime import date
import requests
import psycopg2
import re
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#display = Display(visible=0, size=(800, 600))
#display.start()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
print ("Run ...  ")
url = 'https://products.wholefoodsmarket.com/product/the-mountain-valley-sparkling-spring-water-9f625a'
# Make a GET request to fetch the raw HTML content
driver = webdriver.Chrome('/Users/seanxu/workspace/SeleniumProject/chromedriver', chrome_options=chrome_options)
driver.get(url)
inputElement = driver.find_element_by_class_name("Input-InputField--KUzM1")
inputElement.send_keys('94127')
#inputElement.send_keys(Keys.ENTER)
time.sleep(2)
select = driver.find_elements_by_class_name("StoreSelector-Option--mQyct")
for option in select:
    if '1150 Ocean Ave' in option.text:
        #print ("here")
        option.click()
        break
time.sleep(2)
price = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/span[2]')
print (price.text)

driver.quit()


gmail_user = 'ready6302016@gmail.com'
gmail_password = '06302016'

sent_from = gmail_user
to = ['sean0811@gmail.com', 'bill@gmail.com']
subject = 'OMG Super Important Message' + price.text
body = 'Hey, what\'s up?\n\n- You'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print 'Email sent!'
except:
    print 'Something went wrong...'


#html_content = requests.get(url).text
# Parse the html content
#soup = BeautifulSoup(html_content, "lxml")
#gdp_data = soup.find("div", attrs={"class": "ProductHeader-Available--1hp_M"})

#print(gdp_data.get_text())
