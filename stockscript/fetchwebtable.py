from bs4 import BeautifulSoup
from datetime import date
import requests
import psycopg2
import re


def insert_db(sql, value):
	try:
		connection = psycopg2.connect(user="postgres",
									  password="12345678",
									  host="127.0.0.1",
									  port="5432",
									  database="stocks")
		cursor = connection.cursor()

		# postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
		# record_to_insert = (5, 'One Plus 6', 950)
		# cursor.execute(sql, record_to_insert)
		m_today = date.today()
		check_sql = """ SELECT count(*) from most_gainers where (created_date = %s and symbol = %s) """
		check_value = (m_today, value[0])
		cursor.execute(check_sql, check_value)
		#print(check_value)
		res = cursor.fetchone()
		if (res[0] == 0):
			cursor.execute(sql, value)
			connection.commit()
			count = cursor.rowcount
			print(count, "Record inserted successfully into mobile table")

	except (Exception, psycopg2.Error) as error:
		if (connection):
			print("Failed to insert record into mobile table", error)

	finally:
		if (connection):
			cursor.close()
			connection.close()
			#print("PostgreSQL connection is closed")


sql = """ INSERT INTO most_gainers (symbol, name, price, chg, chg_perc, vol, avg_vol, market_cap, pe, created_date) 
			VALUES ('PINS', 'Pinterest, Inc', 34.29, 9.10, 0.3613, 111, 15, 20, 0.0, UTC_TIMESTAMP()) """


# insert_db(sql)
def convertElements(input):
	print(input)
	last_pos = len(input) - 1
	if (input[last_pos] == 'M'):
		return int(float(input[0:last_pos]) * 1000000)
	elif (input[last_pos] == 'B'):
		return int(float(input[0:last_pos]) * 1000000000)
	elif (input[last_pos] == '%'):
		return float(input[0:last_pos]) / 100
	else:
		input = str(input)
		if "N/A" in input:
			return 0
		else:
			val = input.replace(',', '')
			return float(val)


url = 'https://finance.yahoo.com/gainers'
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "W(100%)"})
gdp_table_data = gdp_table.tbody.find_all("tr")

# print (gdp_table_data[0])

td_elements = []
new_td_elements = []
ct = 0
for tr_elements in gdp_table_data:
	if ct == 15:
		break
	td_elements_data = tr_elements.find_all("td")

	pos = 0
	for td_data in td_elements_data:
		txt = td_data.get_text()
		if ((pos == 2) or (pos == 3) or (pos == 8)):
			if re.search('N/A', txt, re.IGNORECASE):
				td_elements.append(0.0)
			else:
				td_elements.append(float(txt.replace(',', '')))
		elif ((pos > 3) and (pos < 8)):  # int(a.replace(',', ''))
			td_elements.append(convertElements(txt))

		elif (pos == 9):
			break
		else:
			td_elements.append(txt)
		pos = pos + 1

	new_td_elements.append(td_elements)
	td_elements = []

	ct = ct + 1

print("\n")
print(new_td_elements)

sql = """ INSERT INTO most_gainers (symbol, name, price, chg, chg_perc, vol, avg_vol, market_cap, pe, created_date) 
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, now()) """
for value in new_td_elements:
	# print (sql)
	# print (value)
	insert_db(sql, value)
