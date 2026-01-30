from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter


# Vista de la grafica de barras
class BarGraphView(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.model = None

    # Conecta el modelo y sus señales
    def setModel(self, model):
        self.model = model

        # Cuando el modelo cambie, que se repinte
        self.model.dataChanged.connect(self.update)
        self.model.modelReset.connect(self.update)
        self.model.rowsInserted.connect(self.update)
        self.model.rowsRemoved.connect(self.update)

        self.update()

    # widget tamaño 100 * 100 como minimo
    def minimumSizeHint(self):
        return QSize(100, 100)

    def sizeHint(self):
        return self.minimumSizeHint()

    # Dibuja el grafico de barras
    def paintEvent(self, event):

        #si no hay modelo o tiene 0 filas no dibuja nada
        if self.model is None:
            return
        count = self.model.rowCount()
        if count == 0:
            return

        painter=QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Calcular el valor maximo entre todas las barras
        max_value= 1
        for row in range (count):
            value = self.model.value(row)
            if value > max_value:
                max_value = value

        # Define un sistema de coordenadas lógico.
        painter.setWindow(0, 0, count * 20, max_value)

        #Recorrer las barras para pintarlas
        for row in range (count):
            value = self.model.value(row)
            color = self.model.color(row)

            #Posicion x (horizontal) dejando un margen
            x = row * 20 + 1

            #Posicion y (Verical), restamos el valor al máximo para que la barra crezca para arriba.
            y = max_value - value

            painter.setBrush(color)
            painter.setPen(color.darker(120))
            painter.drawRect(x, y, 18, value)






