import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon


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
            self.open_admin_dashboard()
            self.close()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль!')

    def open_admin_dashboard(self):
        self.dashboard = AdminDashboard()
        self.dashboard.show()


class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Администраторская панель')
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon('resources/logo'))
        self.setStyleSheet("background-color: green;")

        layout = QVBoxLayout()

        self.animals_button = QPushButton('Животные')
        self.animals_button.clicked.connect(self.open_animals_window)
        self.animals_button.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(self.animals_button)

        self.staff_button = QPushButton('Сотрудники')
        self.staff_button.clicked.connect(self.open_staff_window)
        self.staff_button.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(self.staff_button)

        self.events_button = QPushButton('Мероприятия')
        self.events_button.clicked.connect(self.open_events_window)
        self.events_button.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(self.events_button)

        self.tickets_button = QPushButton('Касса')
        self.tickets_button.clicked.connect(self.open_tickets_window)
        self.tickets_button.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(self.tickets_button)

        self.setLayout(layout)

    def open_animals_window(self):
        pass

    def open_staff_window(self):
        pass

    def open_events_window(self):
        pass

    def open_tickets_window(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_window = AdminWin()
    admin_window.show()
    sys.exit(app.exec())