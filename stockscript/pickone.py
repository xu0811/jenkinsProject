from bs4 import BeautifulSoup
from datetime import date
import requests
import psycopg2
import re
from send_email import sendmail
from fetchchart import getChart
from fetchHistory import fetchHistory



def pick():
	try:
		connection = psycopg2.connect(user="postgres",
									  password="12345678",
									  host="127.0.0.1",
									  port="5432",
									  database="stocks")
		cursor = connection.cursor()
		select_sql = """ SELECT id, symbol from most_gainers where next_day_chg > 0.1 """
		cursor.execute(select_sql)
		connection.commit()
		#print(check_value)
		res = cursor.fetchall()
		print(res) #Get all the stocks that meet next_day_chg > 0.1

		final_ver = ''
		for sym in res:
			final_ver += sym[1] + ' : ' + fetchHistory(sym[1]) + '\n'
		print("final")
		#print(final_ver)
		update_sql = """ UPDATE most_gainers set mark = 'picked' WHERE id = %s """
		sendmail(final_ver)
		print(final_ver)
		for picked in res:
			id = picked[0]
			#print(picked)
			cursor.execute(update_sql, (id,))
			connection.commit()
			getChart(picked[1])

	except (Exception, psycopg2.Error) as error:
		if (connection):
			print("Failed to insert record into mobile table", error)

	finally:
		if (connection):
			cursor.close()
			connection.close()
			#print("PostgreSQL connection is closed")


pick()

