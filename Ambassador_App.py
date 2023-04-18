# Ambassador_App.py

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

from PyQt6.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QLabel,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):
    """Main Window"""
    def __init__(self, *args, **kwargs):
        """Initialize"""
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Ambassador Database App")



app = QApplication(sys.argv)

window = MainWindow()
window.show()  # causes window to display

app.exec()
