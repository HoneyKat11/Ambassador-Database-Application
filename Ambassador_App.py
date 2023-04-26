# Ambassador_App.py

"""This module provides views for the ambassador.db database."""

import sys

from PyQt6.QtCore import *
from PyQt6.QtSql import *
from PyQt6.QtWidgets import *

from PyQt6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget
)


class EditWindow(QDialog):
    """Edit Window"""
    def __init__(self):
        """Initialize"""
        super(EditWindow, self).__init__(parent=None)

        # Class models
        self.db = None
        self.ambassadorModel = None

        self.get_db()

        # Begin view
        self.setWindowTitle("Edit Ambassador")
        self.setGeometry(100, 100, 300, 400)

        # Form creation
        self.formGroupBox = QGroupBox("Edit Ambassador")
        self.gradYearEntry = QSpinBox(self)
        self.gradYearEntry.setRange(2000, 2030)
        self.create_form()

        # Create button for submission
        self.acceptButton = QPushButton("Submit")
        self.acceptButton.pressed.connect(self.edit_ambassador)
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.pressed.connect(self.hide)
        self.buttonBox = QDialogButtonBox(self.acceptButton or self.cancelButton)

        # Creating layout
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.formGroupBox)
        form_layout.addWidget(self.acceptButton)
        form_layout.addWidget(self.cancelButton)
        form_layout.addWidget(self.buttonBox)
        self.setLayout(form_layout)

    # create form method
    def create_form(self):
        # creating a form layout
        layout = QFormLayout()

        # adding rows
        layout.addRow(QLabel("UIN:"), self.uinEntry)
        layout.addRow(QLabel("First Name:"), self.firstNameEntry)
        layout.addRow(QLabel("Last Name:"), self.lastNameEntry)
        layout.addRow(QLabel("Major:"), self.majorEntry)
        layout.addRow(QLabel("Ambassador Status:"), self.ambassadorEntry)
        layout.addRow(QLabel("Graduation Year:"), self.gradYearEntry)

        # setting layout
        self.formGroupBox.setLayout(layout)

    def edit_ambassador(self):
        # Edit an ambassador grad year
        # Create a query for later execution
        update_data_query = QSqlQuery(self.db)
        update_data_query.prepare(
            """
            UPDATE Ambassador
            SET grad_year = ?
            WHERE UIN = ?;
            """
        )

        new_grad_year = self.gradYearEntry.text()
        update_data_query.addBindValue(new_grad_year)

        update_data_query.exec()
        self.main = MainWindow()
        self.main.resize(1200, 600)
        self.main.show()
        self.close()

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

class FormWindow(QDialog):
    """Form Window"""
    def __init__(self):
        """Initialize"""
        super(FormWindow, self).__init__(parent=None)

        # Class models
        self.db = None
        self.ambassadorModel = None

        self.get_db()

        # Begin view
        self.setWindowTitle("Insert Form")
        self.setGeometry(100, 100, 300, 400)

        # Form creation
        self.formGroupBox = QGroupBox("Add Ambassador")
        self.uinEntry = QSpinBox(self)
        self.uinEntry.setRange(0, 999999999)
        self.firstNameEntry = QLineEdit()
        self.lastNameEntry = QLineEdit()
        self.majorEntry = QComboBox(self)
        self.majorEntry.addItems(["Software", "Civil", "Environmental", "Bioengineering", "Construction Management"])
        self.ambassadorEntry = QComboBox(self)
        self.ambassadorEntry.addItems(["Yes", "No (Honorary)"])
        self.gradYearEntry = QSpinBox(self)
        self.gradYearEntry.setRange(2000, 2030)
        self.create_form()

        # Create button for submission
        self.acceptButton = QPushButton("Submit")
        self.acceptButton.pressed.connect(self.add_ambassador)
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.pressed.connect(self.hide)
        self.buttonBox = QDialogButtonBox(self.acceptButton or self.cancelButton)

        # Creating layout
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.formGroupBox)
        form_layout.addWidget(self.acceptButton)
        form_layout.addWidget(self.cancelButton)
        form_layout.addWidget(self.buttonBox)
        self.setLayout(form_layout)

    # create form method
    def create_form(self):
        # creating a form layout
        layout = QFormLayout()

        # adding rows
        layout.addRow(QLabel("UIN:"), self.uinEntry)
        layout.addRow(QLabel("First Name:"), self.firstNameEntry)
        layout.addRow(QLabel("Last Name:"), self.lastNameEntry)
        layout.addRow(QLabel("Major:"), self.majorEntry)
        layout.addRow(QLabel("Ambassador Status:"), self.ambassadorEntry)
        layout.addRow(QLabel("Graduation Year:"), self.gradYearEntry)

        # setting layout
        self.formGroupBox.setLayout(layout)

    def add_ambassador(self):
        # Add to table
        # Create a query for later execution
        insert_data_query = QSqlQuery(self.db)
        insert_data_query.prepare(
            """
            INSERT INTO Ambassador (
                UIN, 
                first_name, 
                last_name, 
                major, 
                is_ambassador, 
                grad_year
            ) 
            VALUES (?, ?, ?, ?, ?, ?)
            """
        )

        uin = self.uinEntry.text()
        insert_data_query.addBindValue(uin)

        first_name = self.firstNameEntry.text()
        insert_data_query.addBindValue(first_name)

        last_name = self.lastNameEntry.text()
        insert_data_query.addBindValue(last_name)

        major = self.majorEntry.currentText()
        insert_data_query.addBindValue(major)

        input_check = self.ambassadorEntry.currentText()
        if input_check == "Yes":
            is_ambassador = 1
        else:
            is_ambassador = 0
        insert_data_query.addBindValue(is_ambassador)

        grad_year = self.gradYearEntry.text()
        insert_data_query.addBindValue(grad_year)

        insert_data_query.exec()
        self.main = MainWindow()
        self.main.resize(1200, 600)
        self.main.show()
        self.close()

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


class MainWindow(QMainWindow):
    """Main Window"""
    def __init__(self):
        """Initialize"""
        super().__init__()

        # Class models
        self.db = None
        self.ambassadorModel = None

        self.get_db()
        self.get_ambassador_model()
        #self.get_event_model()

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

        # Create add button
        self.form = FormWindow()
        self.addButton = QPushButton("Add Ambassador")
        self.addButton.pressed.connect(self.add)

        # Create edit button
        self.editForm = EditWindow()
        self.editButton = QPushButton("Edit Ambassador")
        self.editButton.pressed.connect(self.edit)

        # Create delete button
        self.deleteButton = QPushButton("Delete Ambassador")

        # Create clear all button
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
        self.form.resize(400, 200)
        if self.form.isVisible():
            self.form.hide()
        else:
            self.form.show()
            self.hide()

    def edit(self):
        self.form.resize(400, 200)
        if self.editForm.isVisible():
            self.editForm.hide()
        else:
            self.editForm.show()
            self.hide()

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

    # def get_event_model(self):
    #     self.eventModel = QSqlTableModel(self, self.db)
    #     self.eventModel.setTable('event_view')
    #
    #     if not self.ambassadorModel.select():
    #         QMessageBox.warning(
    #             None,
    #             "Ambassador_App",
    #             f"Select Failed: {self.db.lastError().text()}",
    #         )
    #     headers = ("Event ID", "Event Name", "Date", "Semester")
    #
    #     for columnIndex, header in enumerate(headers):
    #         self.eventModel.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)


def main():
    """Ambassador_App.py main function"""
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.resize(1200, 600)
    window.show()  # Causes window to display

    # Run the event loop
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
