# コントローラーツールのPython移行

import os
import sys
import subprocess

from PySide2.QtGui import*
from PySide2.QtCore import*
from PySide2.QtWidgets import*

from maya import OpenMayaUI
from shiboken2 import wrapInstance
from . import kmt_get_image_paths
import importlib
importlib.reload(kmt_get_image_paths)

def get_main_window():
    """Maya画面の後ろにいかせない"""

    mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr),QWidget)
    return mayaMainWindow

def close_child(app):
    """ ウィンドウの重複回避 """

    parent_list =  app.parent().children()
    for i in parent_list:
        if app.__class__.__name__ == i.__class__.__name__:
            i.close()

class Tab1Widget(QWidget):
    def __init__(self, parent=None):
        super(Tab1Widget, self).__init__()
        self.icon_path = kmt_get_image_paths.get_image_paths()
        # print(self.icon_path[0])

        icon_path = os.path.dirname(__file__)+"/icons"
        btn_size = 37
        pixmap_Square = QPixmap(self.icon_path[0])
        scaled_pixmap_Square = pixmap_Square.scaled(btn_size, btn_size, Qt.KeepAspectRatio)
        self.tool_button00 = QPushButton()
        self.tool_button00.setIcon(scaled_pixmap_Square)
        self.tool_button00.setIconSize(QSize(btn_size,btn_size))

        pixmap_Cross = QPixmap(icon_path + "/KK_Controller_Cross")
        scaled_pixmap_Cross = pixmap_Cross.scaled(btn_size, btn_size, Qt.KeepAspectRatio)
        self.tool_button01 = QPushButton()
        self.tool_button01.setIcon(scaled_pixmap_Cross)
        self.tool_button01.setIconSize(QSize(btn_size,btn_size))

        pixmap_Dia = QPixmap(icon_path + "/KK_Controller_Dia")
        scaled_pixmap_Dia = pixmap_Dia.scaled(btn_size, btn_size, Qt.KeepAspectRatio)
        self.tool_button02 = QPushButton()
        self.tool_button02.setIcon(scaled_pixmap_Dia)
        self.tool_button02.setIconSize(QSize(btn_size,btn_size))

        pixmap_03 = QPixmap(icon_path + "/KK_Controller_Dia")
        scaled_pixmap_03 = pixmap_03.scaled(btn_size, btn_size, Qt.KeepAspectRatio)
        self.tool_button03 = QPushButton()
        self.tool_button03.setIcon(scaled_pixmap_03)
        self.tool_button03.setIconSize(QSize(btn_size,btn_size))

        pixmap_04 = QPixmap(icon_path + "/KK_Controller_Dia")
        scaled_pixmap_04 = pixmap_04.scaled(btn_size, btn_size, Qt.KeepAspectRatio)
        self.tool_button04 = QPushButton()
        self.tool_button04.setIcon(scaled_pixmap_04)
        self.tool_button04.setIconSize(QSize(btn_size,btn_size))

        hbox = QHBoxLayout()
        hbox.addWidget(self.tool_button00)
        hbox.addWidget(self.tool_button01)
        hbox.addWidget(self.tool_button02)
        hbox.addWidget(self.tool_button03)
        hbox.addWidget(self.tool_button04)
        
        self.setLayout(hbox)

class Tab2Widget(QWidget):
    def __init__(self, parent=None):
        super(Tab2Widget, self).__init__()
        self.icon_path  = os.path.dirname(__file__)+"/icons"
        self.btn_size = 37
        self.button()
    def button(self):
        self.vbox = QVBoxLayout()

        pixmap_05 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_05 = pixmap_05.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button05 = QPushButton()
        self.tool_button05.setIcon(scaled_pixmap_05)
        self.tool_button05.setIconSize(QSize(self.btn_size,self.btn_size))

        pixmap_06 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_06 = pixmap_06.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button06 = QPushButton()
        self.tool_button06.setIcon(scaled_pixmap_06)
        self.tool_button06.setIconSize(QSize(self.btn_size,self.btn_size))

        pixmap_07 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_07 = pixmap_07.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button07 = QPushButton()
        self.tool_button07.setIcon(scaled_pixmap_07)
        self.tool_button07.setIconSize(QSize(self.btn_size,self.btn_size))

        pixmap_08 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_08 = pixmap_08.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button08 = QPushButton()
        self.tool_button08.setIcon(scaled_pixmap_08)
        self.tool_button08.setIconSize(QSize(self.btn_size,self.btn_size))

        pixmap_09 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_09 = pixmap_09.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button09 = QPushButton()
        self.tool_button09.setIcon(scaled_pixmap_09)
        self.tool_button09.setIconSize(QSize(self.btn_size,self.btn_size))

        hbox = QHBoxLayout()
        hbox.addWidget(self.tool_button05)
        hbox.addWidget(self.tool_button06)
        hbox.addWidget(self.tool_button07)
        hbox.addWidget(self.tool_button08)
        hbox.addWidget(self.tool_button09)

        pixmap_10 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_10 = pixmap_10.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button10 = QPushButton()
        self.tool_button10.setIcon(scaled_pixmap_10)
        self.tool_button10.setIconSize(QSize(self.btn_size,self.btn_size))
        
        pixmap_11 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_11 = pixmap_11.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button11 = QPushButton()
        self.tool_button11.setIcon(scaled_pixmap_11)
        self.tool_button11.setIconSize(QSize(self.btn_size,self.btn_size))

        pixmap_12 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_12 = pixmap_12.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button12 = QPushButton()
        self.tool_button12.setIcon(scaled_pixmap_12)
        self.tool_button12.setIconSize(QSize(self.btn_size,self.btn_size))

        pixmap_13 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_13 = pixmap_13.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button13 = QPushButton()
        self.tool_button13.setIcon(scaled_pixmap_13)
        self.tool_button13.setIconSize(QSize(self.btn_size,self.btn_size))

        pixmap_14 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_14 = pixmap_14.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button14 = QPushButton()
        self.tool_button14.setIcon(scaled_pixmap_14)
        self.tool_button14.setIconSize(QSize(self.btn_size,self.btn_size))

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.tool_button10)
        hbox1.addWidget(self.tool_button11)
        hbox1.addWidget(self.tool_button12)
        hbox1.addWidget(self.tool_button13)
        hbox1.addWidget(self.tool_button14)

        pixmap_15 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_15 = pixmap_15.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button15 = QPushButton()
        self.tool_button15.setIcon(scaled_pixmap_15)
        self.tool_button15.setIconSize(QSize(self.btn_size,self.btn_size))
        
        pixmap_16 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_16 = pixmap_16.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button16 = QPushButton()
        self.tool_button16.setIcon(scaled_pixmap_16)
        self.tool_button16.setIconSize(QSize(self.btn_size,self.btn_size))


        pixmap_17 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_17 = pixmap_17.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button17 = QPushButton()
        self.tool_button17.setIcon(scaled_pixmap_17)
        self.tool_button17.setIconSize(QSize(self.btn_size,self.btn_size))

        pixmap_18 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_18 = pixmap_18.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button18 = QPushButton()
        self.tool_button18.setIcon(scaled_pixmap_18)
        self.tool_button18.setIconSize(QSize(self.btn_size,self.btn_size))

        pixmap_19 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        scaled_pixmap_19 = pixmap_19.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button19 = QPushButton()
        self.tool_button19.setIcon(scaled_pixmap_19)
        self.tool_button19.setIconSize(QSize(self.btn_size,self.btn_size))

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.tool_button15)
        hbox2.addWidget(self.tool_button16)
        hbox2.addWidget(self.tool_button17)
        hbox2.addWidget(self.tool_button18)
        hbox2.addWidget(self.tool_button19)

        self.pixmap_20 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        self.scaled_pixmap_20 = self.pixmap_20.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button20 = QPushButton()
        self.tool_button20.setIcon(self.scaled_pixmap_20)
        self.tool_button20.setIconSize(QSize(self.btn_size,self.btn_size))

        self.pixmap_21 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        self.scaled_pixmap_21 = self.pixmap_21.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button21 = QPushButton()
        self.tool_button21.setIcon(self.scaled_pixmap_21)
        self.tool_button21.setIconSize(QSize(self.btn_size,self.btn_size))

        self.pixmap_22 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        self.scaled_pixmap_22 = self.pixmap_22.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button22 = QPushButton()
        self.tool_button22.setIcon(self.scaled_pixmap_22)
        self.tool_button22.setIconSize(QSize(self.btn_size,self.btn_size))

        self.pixmap_23 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        self.scaled_pixmap_23 = self.pixmap_23.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button23 = QPushButton()
        self.tool_button23.setIcon(self.scaled_pixmap_23)
        self.tool_button23.setIconSize(QSize(self.btn_size,self.btn_size))

        self.pixmap_24 = QPixmap(self.icon_path  + "/KK_Controller_Dia")
        self.scaled_pixmap_24 = self.pixmap_24.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button24 = QPushButton()
        self.tool_button24.setIcon(self.scaled_pixmap_24)
        self.tool_button24.setIconSize(QSize(self.btn_size,self.btn_size))


        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.tool_button20)
        hbox3.addWidget(self.tool_button21)
        hbox3.addWidget(self.tool_button22)
        hbox3.addWidget(self.tool_button23)
        hbox3.addWidget(self.tool_button24)

        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox1)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)
        self.setLayout(self.vbox)

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        close_child(self)
        self.mainGUI()
        self._load_qss()

    def mainGUI(self):
        self.setWindowTitle("Python ")
        
        self.V_layout_0 = QVBoxLayout()
        self.qtab = QTabWidget()
        self.qtab.addTab(Tab1Widget(parent=self), 'Main')
        self.qtab.addTab(Tab2Widget(parent=self), 'Sub')

        self.V_layout_0.addWidget(self.qtab)

        widget = QWidget()
        widget.setLayout(self.V_layout_0)
        self.setCentralWidget(widget)

        #スタイルシート読み込み用関数
    def _load_qss(self):
            """
            同階層のstyle.qssを読み込む
            :return:
            """
            styleFile = os.path.join(os.path.dirname(__file__),'style.css')
            print(os.path.dirname(__file__))
            # print("======"+styleFile)
            with open(styleFile, 'r') as f:
                style = f.read()
            self.setStyleSheet(style)

def main():
    maya_window = get_main_window()
    mainwindow = MainWindow(maya_window)
    mainwindow.show()

if __name__ == "__main__":
    main()






 