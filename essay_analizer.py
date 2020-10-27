import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt5.QtWidgets import QLabel, QLineEdit, QFileDialog, QInputDialog


class Tricker(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('Не повторяйся!')

        self.name_place_for_text = QLabel(self)
        self.name_place_for_text.setText("Ваш текст")
        self.name_place_for_text.move(30, 30)

        self.btn = QPushButton('Обнаружить ошибки', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(339, 70)
        self.btn.clicked.connect(self.find_mistakes)

        self.choose_file_button = QPushButton('Выбрать файл', self)
        self.choose_file_button.resize(self.btn.sizeHint())
        self.choose_file_button.move(339, 150)
        self.choose_file_button.clicked.connect(self.choose_file)

        self.place_for_text = QTextEdit(self)
        self.place_for_text.move(30, 50)

        self.name_list_of_mistakes = QLabel(self)
        self.name_list_of_mistakes.setText("Ваши ошибки")
        self.name_list_of_mistakes.move(545, 30)

        self.list_of_mistakes = QLabel(self)
        self.list_of_mistakes.move(535, 50)

    def find_mistakes(self):
        pass

    def choose_file(self):
        fname, ok_pressed = QInputDialog.getText(self, "Введите название файла", "Название файла")

        if ok_pressed:
            self.file = open(fname)
            self.place_for_text.setPlainText(self.file.read())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tricker()
    ex.show()
    sys.exit(app.exec())
