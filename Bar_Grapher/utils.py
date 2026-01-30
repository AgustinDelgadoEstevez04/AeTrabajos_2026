from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
import random

def create_items(model):
    Colors = [
        QColor(Qt.red),
        QColor(Qt.green),
        QColor(Qt.yellow),
        QColor(Qt.cyan),
        QColor(Qt.magenta),
        QColor(Qt.black),
        QColor("#568259"),  # fern
        QColor("#536558"),  # granite
        QColor("#ff006e"),  # pink
        QColor("#3A86FF"),  # azure blue
        QColor("#001524"),

        QColor("#9D8189"),  # Dusty Mauve
        QColor("#BC6C25"),  # Copperwood
        QColor("#03045e"),  # Ocean blue
        QColor("#432818"),  # Coffee
        QColor("#CCFF33"),  # Chartreuse(verde lima)
        QColor("#640D14"),  # Black Cherry
        QColor("#FB5607"),  # Blaze Orange
    ]

    for i in range(18):
        model.insertRows(model.rowCount())
        row = model.rowCount() - 1
        value = random.randint(1, 999)
        color = Colors[i % len(Colors)]
        model.setValue(row, value, color)