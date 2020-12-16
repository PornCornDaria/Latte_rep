import sqlite3
import sys

from PyQt5.QtWidgets import *


class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		self.setGeometry(600, 250, 700, 500)
		self.setWindowTitle('Фильтрация по жанрам')
		
		self.list_w = QTableWidget(self)
		self.list_w.move(200, 20)
		self.list_w.resize(480, 450)
		
		self.con = sqlite3.connect('films_db.sqlite')
		self.cur = self.con.cursor()
		self.genres = self.cur.execute("""SELECT title FROM genres""")
		self.genres_list = [i for i in self.genres]
		self.genres_right = [i[0] for i in self.genres_list]
		
		self.button = QPushButton('Пуск', self)
		self.button.move(30, 70)
		self.button.resize(90, 50)
		
		self.box_list = QComboBox(self)
		self.box_list.move(5, 30)
		self.box_list.resize(140, 30)
		self.box_list.addItems(self.genres_right)
		
		self.list_w.setColumnCount(3)
		self.list_w.setRowCount(0)
		self.list_w.setHorizontalHeaderLabels(['Название', 'Жанр', 'Год'])
		
		right_tables = self.cur.execute(f"""SELECT title, genre, year FROM films""").fetchall()
		for i, row in enumerate(right_tables):
			self.list_w.setRowCount(
				self.list_w.rowCount() + 1)
			for j, elem in enumerate(row):
				self.list_w.setItem(
					i, j, QTableWidgetItem(str(elem)))
		
		self.button.clicked.connect(self.run)
	
	def run(self):
		current_genre = self.box_list.currentText()
		right_tables = self.cur.execute(f"""SELECT title, genre, year FROM films
        WHERE genre=(SELECT id FROM genres WHERE title='{current_genre}')""").fetchall()
		self.list_w.setColumnCount(3)
		self.list_w.setRowCount(0)
		
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