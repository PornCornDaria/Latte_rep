import sqlite3

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


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	sys.exit(app.exec())
