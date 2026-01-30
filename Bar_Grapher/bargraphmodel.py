from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from PySide6.QtGui import QColor, QPixmap


class BarGraphModel (QAbstractListModel):

    def __init__(self, parent= None):
       super().__init__(parent)
       self.values=[]
       self.colors={}

    # Cantida de elemetos que hay
    def rowCount(self, parent =None):
        return len(self.values)

    # Hace que sea editable
    def flags (self, index):
        if not index.isValid():
           return Qt.ItemIsEnabled

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    # te retorna el dato segun el que pida
    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid():
            return None

        row=index.row()

        if row<0 or row>=len(self.values):
            return None

        if role== Qt.DisplayRole:
            return str(self.values[row])

        # pixmap de 20 por 20
        elif role == Qt.DecorationRole:
            pixmap=QPixmap(20, 20)
            color= self.colors.get(row, QColor(Qt.red))
            pixmap.fill(color)
            return pixmap

        # El color directamente
        elif role == Qt.UserRole:
            return self.colors.get(row, QColor(Qt.red))

        # Numeros alineados a la derecha
        elif role== Qt.TextAlignmentRole:
            return Qt.AlignRight | Qt.AlignVCenter

        return None

    # Modifica los datos
    def setData(self, index, value, role = Qt.EditRole):
        if not index.isValid():
            return False

        # Obtener la fila y comprobar límites
        row=index.row()
        if row<0 or row >= len(self.values):
            return False

        # Cambiar el valor numerico
        if role== Qt.EditRole or role==Qt.DisplayRole:
            try:
                self.values[row]=int(value)
                self.dataChanged.emit(index, index)
                return True
            except:
                return False

        # Cambiar el color de la barra
        elif role == Qt.UserRole:
            self.colors[row]=value
            self.dataChanged.emit(index, index)
            return True

        return False

    # Agrega filas nuevas
    def insertRows(self, row, count=1, parent = None):
        self.beginInsertRows(self.index(0).parent(), row, row + count-1)

        for i in range(count):
           self.values.insert(row + i,0)

        self.endInsertRows()
        return True

    # le establece un valor y color a una fila
    def setValue(self, row, value, color= None):
        if 0 <= row < len(self.values):
            self.values[row]=value
        if color:
            self.colors[row]=color
        self.dataChanged.emit(self.index(row), self.index(row))
    # Obtiene el valor de una fila
    def value(self, row):
        if 0 <=row <len(self.values):
            return self.values[row]
        return 0

    # Obtine el color de una fila color roja por defecto
    def color(self, row):
        return self.colors.get(row, QColor(Qt.red))








