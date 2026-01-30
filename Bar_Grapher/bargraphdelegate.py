
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStyledItemDelegate, QSpinBox


class BarGraphDelegate (QStyledItemDelegate):

    def __init__(self, minimum=0, maximum=1000, parent=None):
        super().__init__(parent)
        self.minimum=minimum
        self.maximum=maximum

    def createEditor(self, parent, option, index):

        # Crear los spinbox para editar los valores
        spinbox = QSpinBox(parent)
        spinbox.setRange(self.minimum, self.maximum)
        spinbox.setMinimumWidth(60)
        spinbox.setAlignment(Qt.AlignRight)

        return spinbox

    def setEditorData(self, editor, index):
        # Obtener el valor que estaba en la celda
        value = index.model().data(index, Qt.DisplayRole)
        try:
            #convertir el valor a entero y cargarlo en el spinbox
            editor.setValue(int(value))
        except:
            #si no se puede convertir usa el valor 0
            editor.setValue(0)

    def setModelData(self, editor, model, index):
        # Guarda el valor del spinbox en el modelo
        model.setData(index, editor.value(),Qt.EditRole)















