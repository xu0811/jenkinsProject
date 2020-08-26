from bs4 import BeautifulSoup
import urllib.request
from datetime import date
import requests
import re

def getChart(symbol):
    url = 'https://bigcharts.marketwatch.com/quickchart/quickchart.asp?symb=' + symbol + '&insttype=&freq=7&show=&time=3'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    gdp_table = soup.find("td", attrs={"class": "padded vatop"})
    gdp_table_data = gdp_table.find_all("img")
    url = str(gdp_table_data[0])[10:-3]
    url = url.replace('&amp;', '&')
    #print(url)
    m_today = str(date.today())

    new = m_today.replace('-', '_')

    urllib.request.urlretrieve(url, "/Users/seanxu/workspace/python_test/stockscript/stockImgs/" + symbol + "_" + m_today.replace('-', '_') + "_" + ".jpg")


getChart('IRTC')