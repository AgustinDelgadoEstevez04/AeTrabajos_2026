from PySide6.QtWidgets import QDialog, QListView, QHBoxLayout

from bargraphdelegate import BarGraphDelegate
from bargraphmodel import BarGraphModel
from bargraphview import BarGraphView
from utils import create_items

class MainForm(QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.model = BarGraphModel()
        self.barGraphView = BarGraphView()
        self.barGraphView.setModel(self.model)
        self.listView = QListView()
        self.listView.setModel(self.model)
        self.listView.setItemDelegate(BarGraphDelegate(0, 1000, self))
        self.listView.setMaximumWidth(120)
        self.listView.setEditTriggers(QListView.DoubleClicked |
                                  QListView.EditKeyPressed)
        layout = QHBoxLayout()
        layout.addWidget(self.listView)
        layout.addWidget(self.barGraphView, 1)
        self.setLayout(layout)
        self.setWindowTitle("Bar Grapher")
        create_items(self.model)
        self.resize(600, 600)

