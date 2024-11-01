import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap, QColor, QTransform, qRgba
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QSlider, QComboBox, \
    QHBoxLayout


class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editor")
        self.image = None

        self.image_label = QLabel("Загрузите изображение")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(0, 100)
        self.opacity_slider.setValue(100)
        self.opacity_slider.valueChanged.connect(self.update_opacity)

        self.rotate_left_button = QPushButton("Повернуть влево (90°)")
        self.rotate_right_button = QPushButton("Повернуть вправо (90°)")
        self.rotate_left_button.clicked.connect(self.rotate_left)
        self.rotate_right_button.clicked.connect(self.rotate_right)

        self.channel_combo = QComboBox()
        self.channel_combo.addItems(["Все каналы", "Красный", "Зелёный", "Синий"])
        self.channel_combo.currentIndexChanged.connect(self.update_channel)

        self.open_button = QPushButton("Открыть изображение")
        self.open_button.clicked.connect(self.open_image)

        control_layout = QHBoxLayout()
        control_layout.addWidget(self.open_button)
        control_layout.addWidget(self.rotate_left_button)
        control_layout.addWidget(self.rotate_right_button)

        channel_layout = QHBoxLayout()
        channel_layout.addWidget(self.channel_combo)

        main_layout = QVBoxLayout()
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(channel_layout)
        main_layout.addWidget(self.opacity_slider)

        self.setLayout(main_layout)

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть изображение")
        if file_name:
            self.load_image(file_name)

    def load_image(self, file_name):
        self.image = QImage(file_name)
        if self.image.isNull():
            self.image_label.setText("Ошибка при загрузке изображения")
        else:
            self.display_image()

    def display_image(self):
        scaled_image = self.image.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.image_label.setPixmap(QPixmap.fromImage(scaled_image))

    def update_opacity(self):
        if self.image is None:
            return

        opacity = self.opacity_slider.value() / 100
        alpha_image = self.image.convertToFormat(QImage.Format.Format_ARGB32)

        for x in range(alpha_image.width()):
            for y in range(alpha_image.height()):
                color = QColor(alpha_image.pixel(x, y))
                alpha_value = int(color.alpha() * opacity)
                color.setAlpha(alpha_value)
                alpha_image.setPixel(x, y, color.rgba())

        self.image_label.setPixmap(QPixmap.fromImage(alpha_image))

    def rotate_left(self):
        if not self.image:
            return
        transform = QTransform().rotate(-90)
        self.image = self.image.transformed(transform)
        self.display_image()

    def rotate_right(self):
        if not self.image:
            return
        transform = QTransform().rotate(90)
        self.image = self.image.transformed(transform)
        self.display_image()

    def update_channel(self):
        channel = self.channel_combo.currentText()
        if self.image is None:
            return

        # Конвертация в RGBA, если это еще не сделано
        image_rgb = self.image.convert("RGBA")
        width, height = image_rgb.size
        data = image_rgb.tobytes("raw", "RGBA")

        new_image = QImage(width, height, QImage.Format_RGBA8888)

        for y in range(height):
            for x in range(width):
                index = (y * width + x) * 4

                r = data[index]
                g = data[index + 1]
                b = data[index + 2]
                a = data[index + 3]

                # Применение палитры по выбору канала
                if channel == "Красный":
                    g = 0
                    b = 0
                elif channel == "Зелёный":
                    r = 0
                    b = 0
                elif channel == "Синий":
                    r = 0
                    g = 0

                # Установка пикселя нового изображения
                new_image.setPixel(x, y, qRgba(r, g, b, a))

        # Обновление QLabel с новым изображением
        self.image_label.setPixmap(QPixmap.fromImage(new_image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.resize(800, 600)
    editor.show()
    sys.exit(app.exec())