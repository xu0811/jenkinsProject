from bs4 import BeautifulSoup
from datetime import date
import requests
import psycopg2
import re


def fetchHistory(symbol):
    url = "https://finance.yahoo.com/quote/" + symbol + "/history?p=" + symbol
    html_content = requests.get(url).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    gdp_table = soup.find("table", attrs={"class": "W(100%) M(0)"})
    gdp_table_data = gdp_table.tbody.find_all("tr")

    td_elements = []
    new_td_elements = []
    high_price = []
    close_price = []
    for tr_elements in gdp_table_data:
        td_elements_data = tr_elements.find_all("td")
        #print(td_elements_data[0])
        ct = 0
        for td_data in td_elements_data:
            if ct == 0:
                td_elements.append(td_data.get_text())
            elif ct == 6:
                td_elements.append(int((td_data.get_text()).replace(',', '')))
            else:
                td_elements.append(float(td_data.get_text()))
            ct += 1
        new_td_elements.append(td_elements)
        high_price.append(td_elements[2])
        close_price.append(td_elements[4])
        td_elements = []
    #new_close_price = close_price.reverse()

    rev_close_price = list(reversed(close_price))
    rev_high_price = list(reversed(high_price))
    #print(new_td_elements[0])
    print(close_price)
    #print(rev_close_price)

    flag = 0
    total = len(rev_close_price)
    for i in range(total):
        if i < (total - 2):
            diff1 = (rev_close_price[i+1] - rev_close_price[i])/rev_close_price[i]
            diff2 = (rev_high_price[i+2] - rev_close_price[i+1])/rev_close_price[i+1]
            if (diff1 > 0.1 and diff2 > 0.1):
                print(symbol)
                print (rev_close_price[i], rev_close_price[i+1], rev_close_price[i+2])
                print(i)
                flag += 1

    result = str(flag) + " out of " + str(total) + " = " + str(flag/total)
    #print(result)
    return result
    #print(len(new_td_elements))

print(fetchHistory('TRUP'))