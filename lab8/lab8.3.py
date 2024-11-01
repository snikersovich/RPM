import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QComboBox, \
    QLabel, QPushButton
from PyQt6.QtCore import Qt


class OlympiadResultsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Olympiad Results")
        self.setGeometry(100, 100, 800, 600)

        self.results = self.load_results("results.csv")
        self.schools = sorted(set([login.split('-')[1] for _, _, login, *_, _ in self.results]))
        self.classes = sorted(set([login.split('-')[2] for _, _, login, *_, _ in self.results]))

        self.init_ui()

    def load_results(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            return list(reader)

    def init_ui(self):
        layout = QVBoxLayout()

        self.school_combo = QComboBox()
        self.school_combo.addItem("Все школы")
        self.school_combo.addItems(self.schools)
        self.school_combo.currentIndexChanged.connect(self.update_classes)

        self.class_combo = QComboBox()
        self.class_combo.addItem("Все классы")
        self.classes_by_school = {
            school: sorted(set([login.split('-')[2] for _, _, login in self.results if school in login])) for school in
            self.schools}
        self.update_classes()

        self.class_combo.currentIndexChanged.connect(self.filter_results)

        layout.addWidget(QLabel("Выберите номер школы:"))
        layout.addWidget(self.school_combo)
        layout.addWidget(QLabel("Выберите номер класса:"))
        layout.addWidget(self.class_combo)

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(["Логин", "ФИО", "Суммарный балл"])
        layout.addWidget(self.results_table)

        self.filter_results()
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)

    def update_classes(self):
        selected_school = self.school_combo.currentText()
        self.class_combo.clear()
        if selected_school == "Все школы":
            self.class_combo.addItem("Все классы")
            for school, classes in self.classes_by_school.items():
                self.class_combo.addItems(classes)
        else:
            self.class_combo.addItem("Все классы")
            self.class_combo.addItems(self.classes_by_school[selected_school])

    def filter_results(self):
        selected_school = self.school_combo.currentText()
        selected_class = self.class_combo.currentText()

        filtered_results = []
        for place, user_name, login, *scores, score in self.results:
            school, class_num, participant_num = login.split('-')[1:4]
            if (selected_school == "Все школы" or school == selected_school) and \
                    (selected_class == "Все классы" or class_num == selected_class):
                filtered_results.append((login, user_name, int(score)))

        self.populate_table(filtered_results)

    def populate_table(self, results):
        self.results_table.setRowCount(0)
        scores = [score for _, _, score in results]
        if scores:
            sorted_results = sorted(results, key=lambda x: x[2], reverse=True)
            rank = self.calculate_rank(scores)

            for index, (login, user_name, score) in enumerate(sorted_results):
                row_position = self.results_table.rowCount()
                self.results_table.insertRow(row_position)
                self.results_table.setItem(row_position, 0, QTableWidgetItem(login))
                self.results_table.setItem(row_position, 1, QTableWidgetItem(user_name))
                self.results_table.setItem(row_position, 2, QTableWidgetItem(str(score)))

                if rank[index] == 1:
                    self.results_table.item(row_position, 0).setBackground(Qt.GlobalColor.green)
                    self.results_table.item(row_position, 1).setBackground(Qt.GlobalColor.green)
                    self.results_table.item(row_position, 2).setBackground(Qt.GlobalColor.green)
                elif rank[index] == 2:
                    self.results_table.item(row_position, 0).setBackground(Qt.GlobalColor.yellow)
                    self.results_table.item(row_position, 1).setBackground(Qt.GlobalColor.yellow)
                    self.results_table.item(row_position, 2).setBackground(Qt.GlobalColor.yellow)
                elif rank[index] == 3:
                    self.results_table.item(row_position, 0).setBackground(Qt.GlobalColor.red)
                    self.results_table.item(row_position, 1).setBackground(Qt.GlobalColor.red)
                    self.results_table.item(row_position, 2).setBackground(Qt.GlobalColor.red)

    def calculate_rank(self, scores):
        score_to_rank = {}
        sorted_scores = sorted(set(scores), reverse=True)
        for rank, score in enumerate(sorted_scores, start=1):
            score_to_rank[score] = rank
        return [score_to_rank[score] for score in scores]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OlympiadResultsApp()
    window.show()
    sys.exit(app.exec())