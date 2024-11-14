import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *


class AdminWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вход администратора')
        self.setWindowIcon(QIcon('resources/zamok'))
        self.setFixedSize(300, 200)

        self.login_label = QLabel('Логин:')
        self.login_input = QLineEdit()

        self.password_label = QLabel('Пароль:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.submit_button = QPushButton('Войти')
        self.submit_button.clicked.connect(self.check_credentials)

        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def check_credentials(self):
        # Макет для проверки логина и пароля
        username = self.login_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "123":
            QMessageBox.information(self, 'Успех', 'Вход выполнен успешно!')
            self.close()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminWin()
    window.show()
    sys.exit(app.exec())