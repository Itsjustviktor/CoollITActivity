import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a QWidget widget')

        self.label = QtWidgets.QLabel()
        self.pixmap = QPixmap('pract6\\image.jpg')
        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label)

        self.last_x, self.last_y = None, None

        btn = QPushButton('SAVE', self)
        btn.setToolTip('Save this picture')
        btn.resize(btn.sizeHint())
        btn.move(1050, 575)
        btn.clicked.connect(self.save_image)

        self.setGeometry(300, 300, 1200, 620)
        self.setWindowTitle('Paint')
        self.show()

    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        painter = QPainter(self.label.pixmap())
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


    def save_image(self):
        filename = QFileDialog.getSaveFileName(self, 'D:\\visual studio\\laba Python\\LR1\\pract9',
                    'D:\\', 'PNG Image (*.png)')[0]
        self.label.pixmap().save(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())