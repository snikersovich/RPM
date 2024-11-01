import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget,
    QPushButton, QFileDialog, QLabel, QLineEdit
)
from PyQt6.QtCore import Qt
import collections


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(100, 100, 600, 400)

        self.initUI()
        self.current_file = None

    def initUI(self):
        layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        self.text_edit.textChanged.connect(self.update_text_info)
        layout.addWidget(self.text_edit)

        self.open_button = QPushButton("Открыть файл", self)
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        self.save_button = QPushButton("Сохранить файл", self)
        self.save_button.clicked.connect(self.save_file)
        layout.addWidget(self.save_button)

        self.filename_line_edit = QLineEdit(self)
        self.filename_line_edit.setPlaceholderText("Имя файла для сохранения")
        layout.addWidget(self.filename_line_edit)

        self.char_count_label = QLabel("Количество символов: 0", self)
        layout.addWidget(self.char_count_label)

        self.word_count_label = QLabel("Количество слов: 0", self)
        layout.addWidget(self.word_count_label)

        self.longest_word_label = QLabel("Самое длинное слово: ", self)
        layout.addWidget(self.longest_word_label)

        self.shortest_word_label = QLabel("Самое короткое слово: ", self)
        layout.addWidget(self.shortest_word_label)

        self.most_common_word_label = QLabel("Самое часто встречающееся слово: ", self)
        layout.addWidget(self.most_common_word_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_text_info(self):
        text = self.text_edit.toPlainText()
        words = text.split()

        char_count = len(text)
        word_count = len(words)

        self.char_count_label.setText(f"Количество символов: {char_count}")
        self.word_count_label.setText(f"Количество слов: {word_count}")

        if word_count > 0:
            longest_word = max(words, key=len)
            shortest_word = min(words, key=len)

            word_freq = collections.Counter(words)
            most_common_word, _ = word_freq.most_common(1)[0]

            self.longest_word_label.setText(f"Самое длинное слово: {longest_word}")
            self.shortest_word_label.setText(f"Самое короткое слово: {shortest_word}")
            self.most_common_word_label.setText(f"Самое часто встречающееся слово: {most_common_word}")
        else:
            self.longest_word_label.setText("Самое длинное слово: ")
            self.shortest_word_label.setText("Самое короткое слово: ")
            self.most_common_word_label.setText("Самое часто встречающееся слово: ")

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    self.text_edit.setPlainText(file.read())
                    self.current_file = file_name
            except Exception as e:
                print(f"Ошибка при открытии файла: {e}")

    def save_file(self):
        if not self.current_file:
            file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt);;All Files (*)")
            if file_name:
                self.current_file = file_name
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())
            except Exception as e:
                print(f"Ошибка при сохранении файла: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec())