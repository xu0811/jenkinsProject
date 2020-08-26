from bs4 import BeautifulSoup
from datetime import date
import requests
import psycopg2
import re


def insert_db():
	try:
		connection = psycopg2.connect(user="postgres",
									  password="12345678",
									  host="127.0.0.1",
									  port="5432",
									  database="stocks")
		cursor = connection.cursor()
		m_today = date.today()
		select_sql = """ SELECT symbol from most_gainers where mark IS NULL """
		cursor.execute(select_sql)
		connection.commit()
		#print(check_value)
		res = cursor.fetchall()
		#print(res)

		for sym in res:
			price = getSingleStockInfo(sym[0])
			delta = round((price[2] - price[0])/price[0], 2)
			update_sql = """UPDATE most_gainers SET next_day_open = %s, next_day_high = %s, next_day_chg = %s, mark = %s WHERE (mark is NULL and symbol = %s and created_date != %s ) """
			update_value = (price[0], price[2], delta, 'checked', sym[0], m_today)
			cursor.execute(update_sql, update_value)
		connection.commit()

	except (Exception, psycopg2.Error) as error:
		if (connection):
			print("Failed to insert record into mobile table", error)

	finally:
		if (connection):
			cursor.close()
			connection.close()
			#print("PostgreSQL connection is closed")

def getSingleStockInfo(symbol):
	url = 'https://finance.yahoo.com/quote/' + symbol
	html_content = requests.get(url).text
	soup = BeautifulSoup(html_content, "lxml")
	gdp_table = soup.find("table", attrs={"class": "W(100%)"})
	gdp_table_data = gdp_table.tbody.find_all("tr")
	td_elements = []
	new_td_elements = []
	ct = 0
	for tr_elements in gdp_table_data:
		td_elements_data = tr_elements.find_all("td")
		for td_data in td_elements_data:
			txt = td_data.get_text()
			td_elements.append(txt)
		if (ct == 1 or ct == 4):
			new_td_elements.append(td_elements)
		td_elements = []
		ct = ct + 1
	nextday = []
	nextday.append(float(new_td_elements[0][1])) #open
	nextday.append(float(new_td_elements[1][1].split('-')[0])) #low
	nextday.append(float(new_td_elements[1][1].split('-')[1])) #high
	return nextday

insert_db()

