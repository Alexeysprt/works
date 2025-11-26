import sqlite3
import pandas

cxn = sqlite3.connect('store.db')
wb = pandas.read_excel('user_import.xlsx', sheet_name='Лист1')
wb.index = wb.index + 1
wb.to_sql(name='User', con=cxn, if_exists='replace', index=True)
cxn.commit()
cxn.close()