
import psycopg2
from datetime import date

#postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
#record_to_insert = (5, 'One Plus 6', 950)
#cursor.execute(sql, record_to_insert)

def insert_db(sql, symbol):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="12345678",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="stocks")
        cursor = connection.cursor()
        m_today = date.today()
        check_sql = """ SELECT count(*) from most_gainers where (created_date = %s and symbol = %s) """
        value = (m_today, symbol)
        cursor.execute(check_sql, value)
        if (cursor.rowcount):
            print ("yes")




     		#cursor.execute(sql)  
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



sql = """ INSERT INTO most_gainers (symbol, name, price, chg, chg_perc, vol, avg_vol, market_cap, pe, created_date) 
			VALUES ('PINS', 'Pinterest, Inc', 34.29, 9.10, 0.3613, 111, 15, 20, 0.0, NOW()) """
insert_db(sql, 'PINS')