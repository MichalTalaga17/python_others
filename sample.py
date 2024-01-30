from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog
from PyQt6.QtCore import QDir

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.openFile)

        self.filename_edit = QLineEdit()

        layout.addWidget(QLabel('Files')) 
        layout.addWidget(file_browse)
        layout.addWidget(self.filename_edit)

        self.setLayout(layout)

    def openFile(self):

        fileName, ok = QFileDialog.getOpenFileName(
            self,
            "Choose File",
            QDir.currentPath(),
            "Images (*.png *.jpg *.jpeg);;All Files (*)",
            
        )

        if fileName:
            self.filename_edit.setText(fileName)

if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()
