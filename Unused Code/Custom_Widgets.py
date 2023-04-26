# Custom_Widgets.py
# Started making a custom widget to edit grad year
# https://www.pythonguis.com/tutorials/pyqt6-widget-search-bar/

# Edit Class
# class EditWindow(QDialog):
#     """Edit Window"""
#     def __init__(self):
#         """Initialize"""
#         super(EditWindow, self).__init__(parent=None)
#
#         # Class models
#         self.db = None
#         self.ambassadorModel = None
#
#         self.get_db()
#
#         # Begin view
#         self.setWindowTitle("Edit Ambassador")
#         self.setGeometry(100, 100, 300, 400)
#
#         # Form creation
#         self.formGroupBox = QGroupBox("Edit Ambassador")
#         self.gradYearEntry = QSpinBox(self)
#         self.gradYearEntry.setRange(2000, 2030)
#         self.create_form()
#
#         # Create button for submission
#         self.acceptButton = QPushButton("Submit")
#         self.acceptButton.pressed.connect(self.edit_ambassador)
#         self.cancelButton = QPushButton("Cancel")
#         self.cancelButton.pressed.connect(self.hide)
#         self.buttonBox = QDialogButtonBox(self.acceptButton or self.cancelButton)
#
#         # Create search container
#         self.container = QWidget()
#         self.containerLayout = QVBoxLayout()
#         self.containerLayout.addWidget(self.formGroupBox)
#         self.containerLayout.addWidget(self.acceptButton)
#         self.containerLayout.addWidget(self.cancelButton)
#         self.containerLayout.addWidget(self.buttonBox)
#         self.container.setLayout(self.containerLayout)
#
#         # Using custom widget
#         ambassador_list = []
#         for self.QListView
#
#         self.onoff = ChangeKeepWidget('Testing')
#         self.containerLayout.addWidget(self.onoff)
#
#         self.setLayout(self.containerLayout)
#
#     # create form method
#     def create_form(self):
#         # creating a form layout
#         layout = QFormLayout()
#
#         # adding rows
#         layout.addRow(QLabel("Graduation Year:"), self.gradYearEntry)
#
#         # setting layout
#         self.formGroupBox.setLayout(layout)
#
#     def edit_ambassador(self):
#         # Edit an ambassador grad year
#         # Create a query for later execution
#         update_data_query = QSqlQuery(self.db)
#         update_data_query.prepare(
#             """
#             UPDATE Ambassador
#             SET grad_year = ?
#             WHERE UIN = ?;
#             """
#         )
#
#         new_grad_year = self.gradYearEntry.text()
#         update_data_query.addBindValue(new_grad_year)
#
#         update_data_query.exec()
#         self.main = MainWindow()
#         self.main.resize(1200, 600)
#         self.main.show()
#         self.close()
#
#     def get_db(self):
#         self.db = QSqlDatabase('QSQLITE')
#         self.db.setDatabaseName("ambassador.db")
#         if not self.db.open():
#             QMessageBox.warning(
#                 None,
#                 "Ambassador_App",
#                 f"Database Error: {self.db.lastError().text()}",
#             )
#             sys.exit(1)

"""This module provides custom widgets for the Ambassador_App.py file."""

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout
)


class ChangeKeepWidget(QWidget):
    """Keep or Change Widget"""
    def __init__(self, name):
        super(ChangeKeepWidget, self).__init__()

        self.name = name  # Name of Search Widget
        self.is_on = False  # Current State

        self.label = QLabel(self.name)
        self.btn_change = QPushButton("Change")
        self.btn_keep = QPushButton("Keep")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.btn_change)
        self.hbox.addWidget(self.btn_keep)
        self.setLayout(self.hbox)

        self.btn_change.pressed.connect(self.change)
        self.btn_keep.pressed.connect(self.keep)

    def change(self):
        self.editTrue = True
        self.update_button_state()

    def keep(self):
        self.editTrue = False
        self.update_button_state()

    def update_button_state(self):
        """
        Update the appearance of the control buttons
        depending on the current state (change/keep).
        """
        if not self.editTrue:
            self.btn_keep.setStyleSheet("background-color: #4CAF50; color: #fff;")
            self.btn_change.setStyleSheet("background-color: none; color: none;")
        else:
            self.btn_keep.setStyleSheet("background-color: none; color: none;")
            self.btn_change.setStyleSheet("background-color: #D32F2F; color: #fff;")

