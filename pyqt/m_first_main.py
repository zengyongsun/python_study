"""
实现 first 模块
"""

from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QFileDialog
from pyqt.first_main import Ui_MainWindow
from pyqt.contol_ui_children_form import ChildrenForm

class MFirstMain(QMainWindow,Ui_MainWindow):
    """

    """
    def __init__(self,parent=None):
        super(MFirstMain, self).__init__(parent)
        self.setupUi(self)

        # 生成子窗口实例
        self.child = ChildrenForm()

        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        self.fileCloseAction.triggered.connect(self.close())

        self.fileOpenAction.triggered.connect(self.openMsg)

        self.addWinAction.triggered.connect(self.childShow)

    def close(self):
        QFileDialog.close(self)

    def childShow(self):
        # 添加子窗口
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file,ok = QFileDialog.getOpenFileName(self,"打开","c:/","All Files (*);;Text Files(*.text)")
        # 在状态栏显示文件地址
        self.statusBar().showMessage(file)






if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = MFirstMain()
    ui.show()
    sys.exit(app.exec_())