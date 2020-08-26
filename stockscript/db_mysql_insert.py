import mysql.connector


mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "stocks"
)

mycursor = mydb.cursor()

mydb.commit()

sql = """ INSERT INTO most_gainers (symbol, name, price, chg, chg_perc, vol, avg_vol, market_cap, pe, created_date) 
			VALUES ('PINS', 'Pinterest, Inc', 34.29, 9.10, 0.3613, 111, 15, 20, 0.0, NOW()) """


mycursor.execute(sql)
#insert_db(sql)
