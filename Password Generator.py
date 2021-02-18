# Password Generator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIcon, QFont, QPixmap
from random import shuffle

class Generator:
    def __init__(self):
        # Create frame
        frame = QFrame()
        vb.addWidget(frame)

        # Add label
        form = QFormLayout(frame)
        Title = QLabel('Password Generator')
        Title.setFont(QFont('Elephant', 26))
        Title.setStyleSheet('color:blue;')
        Title.setAlignment(Qt.AlignCenter)
        form.addRow(Title)
        Name = QLabel('Full Name: ')
        Number = QLabel('Mobile: ')
        Password = QLabel('Password: ')

        # Add entry field
        self.name = QLineEdit()
        self.name.setPlaceholderText('PeterOyelegbin')
        form.addRow(Name, self.name)
        self.number = QLineEdit()
        form.addRow(Number, self.number)
        self.pwd = QLineEdit()

        # Add button
        btn = QPushButton('Generate', clicked=self.generate)
        btn.setToolTip('click to generate')
        form.addRow(btn)
        form.addRow(Password, self.pwd)

    def generate(self):
        if len(self.name.text()) < 1 or len(self.number.text()) < 1:
            QMessageBox.critical(win, 'Error Message', 'Error: Input required!')
        else:
            nme = list(self.name.text())
            num = list(self.number.text())
            shuffle(nme)
            name = nme[2] + nme[0] + nme[5]
            shuffle(num)
            number = num[8] + num[3]
            characters = ['~', '!', '@', '$', '%', '^', '*', '_', "'", '|', '?']
            shuffle(characters)
            character = characters[0]
            password = name + character + number
            self.pwd.setText(password)


app = QApplication([])
app.setStyle('Fusion')

# Set window and widget color
qp = QPalette()
qp.setColor(QPalette.Window, Qt.yellow)
qp.setColor(QPalette.Button, Qt.blue)
app.setPalette(qp)

# Create window
win = QWidget()
win.setFixedSize(400,280)
win.setWindowTitle('Password Generator')
win.setFont(QFont('Arial Bold', 20))

# Create menu bar
vb = QVBoxLayout(win)
bar = QMenuBar()
bar.setNativeMenuBar(False)
Menu = bar.addMenu("≡ Menu")
vb.addWidget(bar)

def about(self):
    dialog = QDialog()
    dialog.setWindowTitle('About')
    dialog.setFont(QFont('Arial Bold', 10))
    dialog.setFixedSize(250,300)
    vb = QVBoxLayout(dialog)
    fme = QFrame()
    vb.addWidget(fme)
    grid = QGridLayout(fme)
    product = QLabel('Password\nGenerator')
    product.setFont(QFont('Elephant', 16))
    product.setStyleSheet('color:blue;')
    grid.addWidget(product, 0,0)

    frame = QGroupBox('Developed by:')
    vb.addWidget(frame)
    form = QFormLayout(frame)
    details = QLabel('Name: Peter Oyelegbin \n\nWhatsApp: 08078828296 \n\nGmail: peteroyelegbin@gmail.com \n\n© 2020')
    form.addRow(details)

    close = QPushButton('Close', clicked=dialog.close)
    vb.addWidget(close)
    dialog.exec_()

# Add menu item
About = QAction("About", triggered=about)
Menu.addAction(About)
Quit = QAction("Quit", triggered=win.close)
Quit.setShortcut('Ctrl+Q')
Quit.setStatusTip('Exit application')
Menu.addAction(Quit)

Password = Generator()

win.show()
app.exec_()
