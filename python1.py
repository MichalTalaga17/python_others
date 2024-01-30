import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel

class ExampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Logowanie")

        # Tworzenie trzech QLabel o różnych kolorach
        label1 = QLabel("Label 1", self)
        label1.setStyleSheet("background-color: red;")

        label2 = QLabel("Label 2", self)
        label2.setStyleSheet("background-color: green;")

        label3 = QLabel("Label 3", self)
        label3.setStyleSheet("background-color: blue;")

        # Tworzenie siatki i dodawanie QLabel do niej
        layout = QGridLayout()

        # Dodaj trzy QLabel do siatki
        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 1, 1)
        layout.addWidget(label3, 1, 0)

        self.setLayout(layout)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExampleWindow()
    window.show()
    sys.exit(app.exec())