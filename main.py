import sys

import sqlite3

from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('main.ui', self)
		self.initUI()

	def initUI(self):
		self.con = sqlite3.connect('coffee.db')
		self.cur = self.con.cursor()
		
		self.list_w.setColumnCount(7)
		self.list_w.setRowCount(0)
		self.list_w.setHorizontalHeaderLabels(['coffee_id', 'coffee_grade', 'roasting_degree',
		'ground_or_grain', 'taste', 'price', 'package_weight'])
		
		right_tables = self.cur.execute(f"""SELECT * FROM Coffee""").fetchall()
		for i, row in enumerate(right_tables):
			self.list_w.setRowCount(
				self.list_w.rowCount() + 1)
			for j, elem in enumerate(row):
				self.list_w.setItem(
					i, j, QTableWidgetItem(str(elem)))
		
		self.a = Form2()
		self.a.show()
		
		
class Form2(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('addEditCoffeeForm.ui', self)
		self.initUI()
		
	def initUI(self):
		self.con = sqlite3.connect('coffee.db')
		self.cur = self.con.cursor()
		
		self.pushButton.clicked.connect(self.update_func)
		self.pushButton_2.clicked.connect(self.new_line_func)
	
	def update_func(self):
		coffee_id = int(self.lineEdit.text())
		coffee_grade = self.lineEdit_2.text()
		roasting_degree = int(self.lineEdit_3.text())
		ground_or_grain = self.lineEdit_4.text()
		taste = self.lineEdit_5.text()
		price = float(self.lineEdit_7.text())
		package_weight = int(self.lineEdit_6.text())
		
		self.cur.execute(f"""UPDATE Coffee SET coffee_grade = '{coffee_grade}' WHERE coffee_id = {coffee_id}""")
		self.cur.execute(f"""UPDATE Coffee SET roasting_degree_id = {roasting_degree} WHERE coffee_id = {coffee_id}""")
		self.cur.execute(f"""UPDATE Coffee SET ground_or_grain = '{ground_or_grain}' WHERE coffee_id = {coffee_id}""")
		self.cur.execute(f"""UPDATE Coffee SET taste = '{taste}' WHERE coffee_id = {coffee_id}""")
		self.cur.execute(f"""UPDATE Coffee SET price = {price} WHERE coffee_id = {coffee_id}""")
		self.cur.execute(f"""UPDATE Coffee SET package_weight = {package_weight} WHERE coffee_id = {coffee_id}""")
		self.con.commit()
		
		self.b = Example()
		self.b.show()
	
	def new_line_func(self):
		coffee_id = int(self.lineEdit.text())
		coffee_grade = self.lineEdit_2.text()
		roasting_degree = int(self.lineEdit_3.text())
		ground_or_grain = self.lineEdit_4.text()
		taste = self.lineEdit_5.text()
		price = float(self.lineEdit_7.text())
		package_weight = int(self.lineEdit_6.text())
		
		self.cur.execute(f"""INSERT INTO Coffee(coffee_id, coffee_grade, roasting_degree_id,
		ground_or_grain, taste, price, package_weight) VALUES({coffee_id}, '{coffee_grade}',
		{roasting_degree}, '{ground_or_grain}', '{taste}', {price}, {package_weight})""")
		self.con.commit()
		
		self.a = Example()
		self.a.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	sys.exit(app.exec())
