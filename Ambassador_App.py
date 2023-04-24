# Ambassador_App.py

"""This module provides views for the ambassador.db database."""

import sys

from PyQt6.QtCore import *
from PyQt6.QtSql import *
from PyQt6.QtWidgets import *

from PyQt6.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget
)


class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        """Initialize"""
        super().__init__(parent)

        # Class models
        self.db = None
        self.ambassadorModel = None

        self.get_db()
        self.get_ambassador_model()
        self.get_event_model()

        # Get GUI objects
        self.table = None
        self.addButton = None
        self.editButton = None
        self.deleteButton = None
        self.clearAllButton = None

        # Begin view
        self.setWindowTitle("Ambassador Database App")
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        """Setup the main window GUI"""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.ambassadorModel)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.resizeColumnsToContents()

        # Create buttons
        self.addButton = QPushButton("Add Ambassador")
        self.addButton.pressed.signatures.connect(self.add)
        self.editButton = QPushButton("Edit Ambassador")
        self.deleteButton = QPushButton("Delete Ambassador")
        self.clearAllButton = QPushButton("Clear All")

        # Layout the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.editButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def add(self):


    def get_db(self):
        self.db = QSqlDatabase('QSQLITE')
        self.db.setDatabaseName("ambassador.db")
        if not self.db.open():
            QMessageBox.warning(
                None,
                "Ambassador_App",
                f"Database Error: {self.db.lastError().text()}",
            )
            sys.exit(1)

    def get_ambassador_model(self):
        self.ambassadorModel = QSqlTableModel(self, self.db)
        self.ambassadorModel.setTable('ambassador_view')

        if not self.ambassadorModel.select():
            QMessageBox.warning(
                None,
                "Ambassador_App",
                f"Select Failed: {self.db.lastError().text()}",
            )
        headers = ("UIN", "First Name", "Last Name", "Major", "Ambassador (T/F)", "Graduation Year")

        for columnIndex, header in enumerate(headers):
            self.ambassadorModel.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)

    def get_event_model(self):
        self.eventModel = QSqlTableModel(self, self.db)
        self.eventModel.setTable('event_view')

        if not self.ambassadorModel.select():
            QMessageBox.warning(
                None,
                "Ambassador_App",
                f"Select Failed: {self.db.lastError().text()}",
            )
        headers = ("Event ID", "Event Name", "Date", "Semester")

        for columnIndex, header in enumerate(headers):
            self.eventModel.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)


def main():
    """Ambassador_App.py main function"""
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = Window()
    window.resize(1200, 400)
    window.show()  # Causes window to display

    # Run the event loop
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
