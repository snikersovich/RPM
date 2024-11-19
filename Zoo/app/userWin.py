import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *


class TicketPurchaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Покупка билетов')
        self.setFixedSize(300, 250)
        self.setWindowIcon(QIcon('resources/tickets'))

        self.child_ticket_price = 700  # цена детского билета
        self.adult_ticket_price = 1000   # цена взрослого билета

        self.child_ticket_label = QLabel("Детские билеты:")
        self.child_ticket_count = QSpinBox()
        self.child_ticket_count.setRange(0, 100)

        self.child_ticket_slider = QSlider(Qt.Orientation.Horizontal)
        self.child_ticket_slider.setRange(0, 100)
        self.child_ticket_slider.valueChanged.connect(self.update_child_ticket_count)

        self.adult_ticket_label = QLabel("Взрослые билеты:")
        self.adult_ticket_count = QSpinBox()
        self.adult_ticket_count.setRange(0, 100)

        self.adult_ticket_slider = QSlider(Qt.Orientation.Horizontal)
        self.adult_ticket_slider.setRange(0, 100)
        self.adult_ticket_slider.valueChanged.connect(self.update_adult_ticket_count)

        self.total_price_label = QLabel("Итого: 0 рублей")

        self.confirm_button = QPushButton("Подтвердить покупку")
        self.confirm_button.clicked.connect(self.confirm_purchase)

        layout = QVBoxLayout()
        layout.addWidget(self.child_ticket_label)
        layout.addWidget(self.child_ticket_slider)
        layout.addWidget(self.child_ticket_count)
        layout.addWidget(self.adult_ticket_label)
        layout.addWidget(self.adult_ticket_slider)
        layout.addWidget(self.adult_ticket_count)
        layout.addWidget(self.total_price_label)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def update_child_ticket_count(self, value):
        self.child_ticket_count.setValue(value)
        self.update_total_price()

    def update_adult_ticket_count(self, value):
        self.adult_ticket_count.setValue(value)
        self.update_total_price()

    def update_total_price(self):
        child_tickets = self.child_ticket_slider.value()
        adult_tickets = self.adult_ticket_slider.value()
        total_price = (child_tickets * self.child_ticket_price) + (adult_tickets * self.adult_ticket_price)
        self.total_price_label.setText(f"Итого: {total_price} рублей")

    def confirm_purchase(self):
        child_tickets = self.child_ticket_slider.value()
        adult_tickets = self.adult_ticket_slider.value()
        total_price = (child_tickets * self.child_ticket_price) + (adult_tickets * self.adult_ticket_price)
        QMessageBox.information(self, "Подтверждение покупки", f"Вы купили {child_tickets} детских и {adult_tickets} взрослых билетов."
                                                               f" \nНа сумму: {total_price}")


class UserWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Пользовательское окно')
        self.setWindowIcon(QIcon('resources/logo'))
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: green;")

        self.ticket_button = QPushButton("Билеты")
        self.ticket_button.clicked.connect(self.open_ticket_purchase)
        self.ticket_button.setStyleSheet("background-color: white; color: black;")

        self.feeding_button = QPushButton("Открытые кормления животных")
        self.feeding_button.setStyleSheet("background-color: white; color: black;")

        self.tours_button = QPushButton("Экскурсии")
        self.tours_button.setStyleSheet("background-color: white; color: black;")

        self.exhibitions_button = QPushButton("Экспозиции и выставки")
        self.exhibitions_button.setStyleSheet("background-color: white; color: black;")

        layout = QVBoxLayout()
        layout.addWidget(self.ticket_button)
        layout.addWidget(self.feeding_button)
        layout.addWidget(self.tours_button)
        layout.addWidget(self.exhibitions_button)

        self.setLayout(layout)

    def open_ticket_purchase(self):
        self.ticket_window = TicketPurchaseWindow()
        self.ticket_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_window = UserWin()
    user_window.show()
    sys.exit(app.exec())