import sqlite3
import sys

from PyQt5.QtWidgets import *


class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		self.setGeometry(600, 250, 700, 500)
		self.setWindowTitle('Эспрессо')
		
		self.list_w = QTableWidget(self)
		self.list_w.move(0, 0)
		self.list_w.resize(690, 500)
		
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
