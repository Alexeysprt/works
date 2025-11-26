import sqlite3
import pandas

cxn = sqlite3.connect('store.db')
wb = pandas.read_excel('Заказ_Import.xlsx', sheet_name='Лист1')
wb.to_sql(name='Order', con=cxn, if_exists='replace', index=False)
cxn.commit()
cxn.close()