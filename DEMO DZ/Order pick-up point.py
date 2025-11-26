import sqlite3
import pandas

cxn = sqlite3.connect('store.db')
wb = pandas.read_excel('Пункты выдачи_import.xlsx', sheet_name='Лист1')

split_data = wb['Индекс, Город, Улица, Дом'].str.split(',', expand=True)
split_data.columns = ['Индекс', 'Город', 'Улица', 'Дом']
split_data.index = split_data.index + 1

split_data.to_sql(name='Order pick-up point', con=cxn, if_exists='replace', index=True)
cxn.commit()
cxn.close()