import sys
from PyQt6.QtWidgets import *


class TicketPurchaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Покупка билетов')
        self.setFixedSize(300, 250)

        self.ticket_label = QLabel("Детские билеты:")
        self.child_ticket_count = QSpinBox()
        self.child_ticket_count.setRange(0, 100)

        self.adult_ticket_label = QLabel("Взрослые билеты:")
        self.adult_ticket_count = QSpinBox()
        self.adult_ticket_count.setRange(0, 100)

        self.total_price_label = QLabel("Итого: 0 рублей")
        self.calculate_button = QPushButton("Рассчитать стоимость")
        self.calculate_button.clicked.connect(self.calculate_total)

        self.confirm_button = QPushButton("Подтвердить покупку")
        self.confirm_button.clicked.connect(self.confirm_purchase)

        layout = QVBoxLayout()
        layout.addWidget(self.ticket_label)
        layout.addWidget(self.child_ticket_count)
        layout.addWidget(self.adult_ticket_label)
        layout.addWidget(self.adult_ticket_count)
        layout.addWidget(self.total_price_label)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def calculate_total(self):
        child_count = self.child_ticket_count.value()
        adult_count = self.adult_ticket_count.value()
        total_price = child_count * 700 + adult_count * 1000
        self.total_price_label.setText(f"Итого: {total_price} рублей")

    def confirm_purchase(self):
        total_price = int(self.total_price_label.text().split()[1])
        QMessageBox.information(self, "Подтверждение", f"Вы купили билетов на сумму {total_price} рублей!")


class UserWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Пользовательское окно')
        self.setFixedSize(400, 300)

        self.ticket_button = QPushButton("Билеты")
        self.ticket_button.clicked.connect(self.open_ticket_purchase)
        self.feeding_button = QPushButton("Открытые кормления животных")
        self.tours_button = QPushButton("Экскурсии")
        self.exhibitions_button = QPushButton("Экспозиции и выставки")

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