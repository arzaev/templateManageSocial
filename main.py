import sys
from model import QTable_S
from gui import TableView_S
from PyQt5.QtWidgets import QApplication, QWidget
from gui import gui_template
from PyQt5.QtGui import QStandardItem


class MainForm(QWidget, gui_template.Ui_Form):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.model_table = QTable_S.ModelQTableView()
        self.QTable = TableView_S.TableView(self.model_table)
        self.verticalLayout.addWidget(self.QTable)
        self.model_table.setHorizontalHeaderLabels(['id', 'Email', 'Password', 'Proxy', 'Action', 'Info', 'Social'])
        self.add_data()
        self.btn_start.clicked.connect(self.return_select_rows)

    def add_data(self):
        with open('data/accounts.txt', 'r') as f:
            accounts = f.read().split('\n')
        for i, acc in enumerate(accounts):
            self.model_table.setItem(i, 0, QStandardItem(str(i)))
            self.model_table.setItem(i, 1, QStandardItem(acc.split(':')[0]))
            self.model_table.setItem(i, 2, QStandardItem(acc.split(':')[1]))
            self.model_table.setItem(i, 3, QStandardItem(acc.split(':')[2]))

    def return_select_rows(self):
        list_rows = []
        list_rows_id = []
        indexes = self.QTable.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = str(index.row())
            list_rows.append(row)
            list_rows_id.append(int(self.model_table.item(int(row), 0).text()))
        print(list_rows, list_rows_id)
        return (list_rows, list_rows_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainForm()
    w.setWindowTitle('Station')
    w.show()
    sys.exit(app.exec_())