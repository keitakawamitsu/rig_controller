# kmt_controller.py
# 製作者 : みっつ
# 更新日 : 2023/02/01(水)

import os
import sys
import subprocess

from PySide2.QtGui import*
from PySide2.QtCore import*
from PySide2.QtWidgets import*

from maya import OpenMayaUI
from shiboken2 import wrapInstance
from . import kmt_get_image_paths as path
from . import kmt_make_curves as curves


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
        self.icon_path = path.get_image_paths("main")
        
        self.btn_size = 37
        self.cv_cube = curves.Curves("cube",1)#jsonの名前読み込んでる
        self.cv_cone = curves.Curves("cone",1)
        self.cv_ball = curves.Curves("ball",1)
        self.cv_ForeArrow = curves.Curves("ForeArrow",1)
        self.cv_SingleArrow = curves.Curves("SingleArrow",1)
        self.cv_Square = curves.Curves("Square",1)

        self.make_button()

    def make_button(self):
        pixmap_Square = QPixmap(self.icon_path[0])
        scaled_pixmap_Square = pixmap_Square.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button00 = QPushButton()
        self.tool_button00.setIcon(scaled_pixmap_Square)
        self.tool_button00.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button00.clicked.connect(self.cv_cube.move_cv)

        pixmap_Cross = QPixmap(self.icon_path[1])
        scaled_pixmap_Cross = pixmap_Cross.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button01 = QPushButton()
        self.tool_button01.setIcon(scaled_pixmap_Cross)
        self.tool_button01.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button01.clicked.connect(self.cv_cone.move_cv)


        pixmap_Dia = QPixmap(self.icon_path[2])
        scaled_pixmap_Dia = pixmap_Dia.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button02 = QPushButton()
        self.tool_button02.setIcon(scaled_pixmap_Dia)
        self.tool_button02.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button02.clicked.connect(self.cv_ball.move_cv)


        pixmap_03 = QPixmap(self.icon_path[3])
        scaled_pixmap_03 = pixmap_03.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button03 = QPushButton()
        self.tool_button03.setIcon(scaled_pixmap_03)
        self.tool_button03.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button03.clicked.connect(self.cv_ForeArrow.move_cv)
        

        pixmap_04 = QPixmap(self.icon_path[4])
        scaled_pixmap_04 = pixmap_04.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button04 = QPushButton()
        self.tool_button04.setIcon(scaled_pixmap_04)
        self.tool_button04.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button04.clicked.connect(self.cv_SingleArrow.move_cv)

        pixmap_05 = QPixmap(self.icon_path[5])
        scaled_pixmap_05 = pixmap_05.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button05 = QPushButton()
        self.tool_button05.setIcon(scaled_pixmap_05)
        self.tool_button05.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button05.clicked.connect(self.cv_Square.move_cv)

        hbox = QHBoxLayout()
        hbox.addWidget(self.tool_button00)
        hbox.addWidget(self.tool_button01)
        hbox.addWidget(self.tool_button02)
        hbox.addWidget(self.tool_button03)
        hbox.addWidget(self.tool_button04)
        hbox.addWidget(self.tool_button05)
        
        self.setLayout(hbox)


class Tab2Widget(QWidget):
    def __init__(self, parent=None):
        super(Tab2Widget, self).__init__()
        self.icon_path1 = path.get_image_paths("sub")

        self.icon_path  = os.path.dirname(__file__)+"/icons/sub"
        self.btn_size = 37

        self.cv_circle = curves.Curves("circle",1)
        self.cv_cross = curves.Curves("cross",1)
        self.cv_pentagon = curves.Curves("pentagon",1)
        self.cv_hexagon = curves.Curves("hexagon",1)
        self.cv_Triangular = curves.Curves("Triangular",1)
        self.cv_Spear = curves.Curves("Spear",1)
  
        self.cv_hexagon2 = curves.Curves("hexagon2",1)
        self.cv_dia = curves.Curves("dia",1)
        self.cv_dirSingleThin = curves.Curves("dirSingleThin",1)
        self.cv_dirDoubleThin = curves.Curves("dirDoubleThin",1)
        self.cv_dirDoubleFat = curves.Curves("dirDoubleFat",1)
        self.cv_dirFourThin = curves.Curves("dirFourThin",1)
  
        self.cv_dirEight = curves.Curves("dirEight",1)
        self.cv_Rot90Thin = curves.Curves("Rot90Thin",1)
        self.cv_Rot90Fat = curves.Curves("Rot90Fat",1)
        self.cv_rot180Thin = curves.Curves("rot180Thin",1)
        self.cv_rot180Fat = curves.Curves("rot180Fat",1)
        self.cv_arrowsOnBall = curves.Curves("arrowsOnBall",1)

        self.cv_cog = curves.Curves("cog",3)
        self.cv_pin = curves.Curves("pin",1)
        self.cv_doublePin = curves.Curves("doublePin",1)
        self.cv_fourPin = curves.Curves("fourPin",1)
        self.cv_dumbell = curves.Curves("dumbell",1)
        self.cv_aim = curves.Curves("aim",1)


        self.make_button()
    def make_button(self):
        self.vbox = QVBoxLayout()

        pixmap_05 = QPixmap(self.icon_path1[0])
        scaled_pixmap_05 = pixmap_05.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button05 = QPushButton()
        self.tool_button05.setIcon(scaled_pixmap_05)
        self.tool_button05.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button05.clicked.connect(self.cv_circle.move_cv)


        pixmap_06 = QPixmap(self.icon_path1[1])
        scaled_pixmap_06 = pixmap_06.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button06 = QPushButton()
        self.tool_button06.setIcon(scaled_pixmap_06)
        self.tool_button06.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button06.clicked.connect(self.cv_cross.move_cv)


        pixmap_07 = QPixmap(self.icon_path1[2])
        scaled_pixmap_07 = pixmap_07.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button07 = QPushButton()
        self.tool_button07.setIcon(scaled_pixmap_07)
        self.tool_button07.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button07.clicked.connect(self.cv_pentagon.move_cv)


        pixmap_08 = QPixmap(self.icon_path1[3])
        scaled_pixmap_08 = pixmap_08.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button08 = QPushButton()
        self.tool_button08.setIcon(scaled_pixmap_08)
        self.tool_button08.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button08.clicked.connect(self.cv_hexagon.move_cv)

        pixmap_09 = QPixmap(self.icon_path1[4])
        scaled_pixmap_09 = pixmap_09.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button09 = QPushButton()
        self.tool_button09.setIcon(scaled_pixmap_09)
        self.tool_button09.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button09.clicked.connect(self.cv_Triangular.move_cv)

        pixmap_10 = QPixmap(self.icon_path1[5])
        scaled_pixmap_10 = pixmap_10.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button10 = QPushButton()
        self.tool_button10.setIcon(scaled_pixmap_10)
        self.tool_button10.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button10.clicked.connect(self.cv_Spear.move_cv)

        hbox = QHBoxLayout()
        hbox.addWidget(self.tool_button05)
        hbox.addWidget(self.tool_button06)
        hbox.addWidget(self.tool_button07)
        hbox.addWidget(self.tool_button08)
        hbox.addWidget(self.tool_button09)
        hbox.addWidget(self.tool_button10)
        
        pixmap_11 = QPixmap(self.icon_path1[6])
        scaled_pixmap_11 = pixmap_11.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button11 = QPushButton()
        self.tool_button11.setIcon(scaled_pixmap_11)
        self.tool_button11.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button11.clicked.connect(self.cv_hexagon2.move_cv)


        pixmap_12 = QPixmap(self.icon_path1[7])
        scaled_pixmap_12 = pixmap_12.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button12 = QPushButton()
        self.tool_button12.setIcon(scaled_pixmap_12)
        self.tool_button12.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button12.clicked.connect(self.cv_dia.move_cv)

        pixmap_13 = QPixmap(self.icon_path1[8])
        scaled_pixmap_13 = pixmap_13.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button13 = QPushButton()
        self.tool_button13.setIcon(scaled_pixmap_13)
        self.tool_button13.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button13.clicked.connect(self.cv_dirSingleThin.move_cv)

        pixmap_14 = QPixmap(self.icon_path1[9])
        scaled_pixmap_14 = pixmap_14.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button14 = QPushButton()
        self.tool_button14.setIcon(scaled_pixmap_14)
        self.tool_button14.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button14.clicked.connect(self.cv_dirDoubleThin.move_cv)

        pixmap_15 = QPixmap(self.icon_path1[10])
        scaled_pixmap_15 = pixmap_15.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button15 = QPushButton()
        self.tool_button15.setIcon(scaled_pixmap_15)
        self.tool_button15.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button15.clicked.connect(self.cv_dirDoubleFat.move_cv)

        pixmap_16 = QPixmap(self.icon_path1[11])
        scaled_pixmap_16 = pixmap_16.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button16 = QPushButton()
        self.tool_button16.setIcon(scaled_pixmap_16)
        self.tool_button16.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button16.clicked.connect(self.cv_dirFourThin.move_cv)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.tool_button11)
        hbox1.addWidget(self.tool_button12)
        hbox1.addWidget(self.tool_button13)
        hbox1.addWidget(self.tool_button14)
        hbox1.addWidget(self.tool_button15)
        hbox1.addWidget(self.tool_button16)

        pixmap_17 = QPixmap(self.icon_path1[12])
        scaled_pixmap_17 = pixmap_17.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button17 = QPushButton()
        self.tool_button17.setIcon(scaled_pixmap_17)
        self.tool_button17.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button17.clicked.connect(self.cv_dirEight.move_cv)

        pixmap_18 = QPixmap(self.icon_path1[13])
        scaled_pixmap_18 = pixmap_18.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button18 = QPushButton()
        self.tool_button18.setIcon(scaled_pixmap_18)
        self.tool_button18.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button18.clicked.connect(self.cv_Rot90Thin.move_cv)

        pixmap_19 = QPixmap(self.icon_path1[14])
        scaled_pixmap_19 = pixmap_19.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button19 = QPushButton()
        self.tool_button19.setIcon(scaled_pixmap_19)
        self.tool_button19.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button19.clicked.connect(self.cv_Rot90Fat.move_cv)

        self.pixmap_20 = QPixmap(self.icon_path1[15])
        self.scaled_pixmap_20 = self.pixmap_20.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button20 = QPushButton()
        self.tool_button20.setIcon(self.scaled_pixmap_20)
        self.tool_button20.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button20.clicked.connect(self.cv_rot180Thin.move_cv)


        self.pixmap_21 = QPixmap(self.icon_path1[16])
        self.scaled_pixmap_21 = self.pixmap_21.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button21 = QPushButton()
        self.tool_button21.setIcon(self.scaled_pixmap_21)
        self.tool_button21.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button21.clicked.connect(self.cv_rot180Fat.move_cv)

        self.pixmap_22 = QPixmap(self.icon_path1[17])
        self.scaled_pixmap_22 = self.pixmap_22.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button22 = QPushButton()
        self.tool_button22.setIcon(self.scaled_pixmap_22)
        self.tool_button22.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button22.clicked.connect(self.cv_arrowsOnBall.move_cv)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.tool_button17)
        hbox2.addWidget(self.tool_button18)
        hbox2.addWidget(self.tool_button19)
        hbox2.addWidget(self.tool_button20)
        hbox2.addWidget(self.tool_button21)
        hbox2.addWidget(self.tool_button22)


        self.pixmap_23 = QPixmap(self.icon_path1[18])
        self.scaled_pixmap_23 = self.pixmap_23.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button23 = QPushButton()
        self.tool_button23.setIcon(self.scaled_pixmap_23)
        self.tool_button23.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button23.clicked.connect(self.cv_cog.move_cv)

        self.pixmap_24 = QPixmap(self.icon_path1[19])
        self.scaled_pixmap_24 = self.pixmap_24.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button24 = QPushButton()
        self.tool_button24.setIcon(self.scaled_pixmap_24)
        self.tool_button24.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button24.clicked.connect(self.cv_pin.move_cv)

        self.pixmap_25 = QPixmap(self.icon_path1[20])
        self.scaled_pixmap_25 = self.pixmap_25.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button25 = QPushButton()
        self.tool_button25.setIcon(self.scaled_pixmap_25)
        self.tool_button25.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button25.clicked.connect(self.cv_doublePin.move_cv)


        self.pixmap_26 = QPixmap(self.icon_path1[21])
        self.scaled_pixmap_26 = self.pixmap_26.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button26 = QPushButton()
        self.tool_button26.setIcon(self.scaled_pixmap_26)
        self.tool_button26.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button26.clicked.connect(self.cv_fourPin.move_cv)

        self.pixmap_27 = QPixmap(self.icon_path1[22])
        self.scaled_pixmap_27 = self.pixmap_27.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button27 = QPushButton()
        self.tool_button27.setIcon(self.scaled_pixmap_27)
        self.tool_button27.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button27.clicked.connect(self.cv_dumbell.move_cv)

        self.pixmap_28 = QPixmap(self.icon_path1[23])
        self.scaled_pixmap_28 = self.pixmap_28.scaled(self.btn_size, self.btn_size, Qt.KeepAspectRatio)
        self.tool_button28 = QPushButton()
        self.tool_button28.setIcon(self.scaled_pixmap_28)
        self.tool_button28.setIconSize(QSize(self.btn_size,self.btn_size))
        self.tool_button28.clicked.connect(self.cv_aim.move_cv)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.tool_button23)
        hbox3.addWidget(self.tool_button24)
        hbox3.addWidget(self.tool_button25)
        hbox3.addWidget(self.tool_button26)
        hbox3.addWidget(self.tool_button27)
        hbox3.addWidget(self.tool_button28)

        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox1)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)
        self.setLayout(self.vbox)


class MakeCurvesWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MakeCurvesWindow,self).__init__(parent)
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
            """
            styleFile = os.path.join(os.path.dirname(__file__),'style.css')
            with open(styleFile, 'r') as f:
                style = f.read()
            self.setStyleSheet(style)

def main():
    maya_window = get_main_window()
    mainwindow = MakeCurvesWindow(maya_window)
    mainwindow.show()

if __name__ == "__main__":
    main()






 