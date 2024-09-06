from PySide6.QtWidgets import QWidget, QComboBox, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QWidget, QGroupBox, QCheckBox,QButtonGroup,QVBoxLayout, QPushButton, QSizePolicy, QGridLayout,QRadioButton

class WidgetHolder(QWidget):
    def __init__(self):
        super().__init__()

        os = QGroupBox()
        windows = QCheckBox('Windows')
        linux = QCheckBox('Linux')
        mac = QCheckBox('Mac')

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        drinks = QGroupBox('Drinks')
        beer = QCheckBox('Beer')
        juice = QCheckBox('Juice')
        tea = QCheckBox('Tea')
        beer.setChecked(True)

        exclusive_check_group = QButtonGroup(self)
        exclusive_check_group.addButton(beer)
        exclusive_check_group.addButton(juice)
        exclusive_check_group.addButton(tea)
        exclusive_check_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(tea)
        drinks.setLayout(drink_layout)

        answers =QGroupBox()
        a = QRadioButton('A')
        b = QRadioButton('B')
        c = QRadioButton('C')
        a.setChecked(True)

        answer_layout = QVBoxLayout()
        answer_layout.addWidget(a)
        answer_layout.addWidget(b)
        answer_layout.addWidget(c)
        answers.setLayout(answer_layout)

        button1 = QPushButton('button1')
        button2 = QPushButton('button2')
        button3 = QPushButton('button3')
        button3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button4 = QPushButton('button4')
        button5 = QPushButton('button5')
        button6 = QPushButton('button6')
        button7 = QPushButton('button7')

        grid_buttons = QGroupBox()
        grid_layout = QGridLayout()
        grid_layout.addWidget(button1,0,0)
        grid_layout.addWidget(button2,0,1,1,2)
        grid_layout.addWidget(button3,1,0,2,1)
        grid_layout.addWidget(button4,1,1)
        grid_layout.addWidget(button5,1,2)
        grid_layout.addWidget(button6,2,1)
        grid_layout.addWidget(button7,2,2)
        grid_buttons.setLayout(grid_layout)

        layout = QVBoxLayout()
        layout.addWidget(os)
        layout.addWidget(drinks)
        layout.addWidget(answers)
        layout.addWidget(grid_buttons)
        self.setLayout(layout)