from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from pyqt.ui_children_form import Ui_Form
class ChildrenForm(QWidget,Ui_Form):

    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)
