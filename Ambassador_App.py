# Ambassador_App.py

"""This module provides an application for the ambassador.db database."""

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


class EditWindow(QMainWindow):
    """Edit Window"""
    def __init__(self):
        """Initialize"""
        super().__init__()

        # Class models
        self.db = None
        self.ambassadorModel = None

        self.get_db()

        # Create save button
        self.form = FormWindow()
        self.saveButton = QPushButton("Save")
        self.saveButton.pressed.connect(self.save_edit)

        # Create cancel button
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.pressed.connect(self.cancel_edit)

        # Begin view
        self.setWindowTitle("Edit Ambassador")
        self.resize(1200, 600)

        # Set up the model
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("Ambassador")
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "UIN")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, "First Name")
        self.model.setHeaderData(2, Qt.Orientation.Horizontal, "Last Name")
        self.model.setHeaderData(3, Qt.Orientation.Horizontal, "Major")
        self.model.setHeaderData(4, Qt.Orientation.Horizontal, "Ambassador Status (T/F)")
        self.model.setHeaderData(5, Qt.Orientation.Horizontal, "Graduation Year")

        if not self.model.select():
            QMessageBox.warning(
                None,
                "Ambassador_Edit",
                f"Select Failed: {self.db.lastError().text()}",
            )

        # Set up the view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()

        # Layout the GUI
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        button_box = QVBoxLayout()
        button_box.addWidget(self.saveButton)
        button_box.addWidget(self.cancelButton)
        button_box.addStretch()
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addStretch()
        self.layout.addLayout(layout)
        self.layout.addLayout(button_box)

    def save_edit(self):
        # Save changes and close edit window
        self.model.submitAll()
        self.main = MainWindow()
        self.main.resize(1200, 600)
        self.main.show()
        self.close()

    def cancel_edit(self):
        # Exit edit window without saving changes
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
        self.cancelButton.pressed.connect(self.cancel_add)
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

    def cancel_add(self):
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
