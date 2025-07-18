# Form implementation generated from reading ui file 'finishedgui2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import getpass
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer, Qt



class Ui_MainWindow(object):
    def retranslateUi(self, MainWindow):                                                                
                username = getpass.getuser().capitalize()
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "pyLingo"))
                self.textEntry.setPlaceholderText(_translate("MainWindow", "enter text"))
                self.logoLabel.setText(_translate("MainWindow", "pyLingo"))
                self.welcomeLabel.setText(_translate("MainWindow", f"welcome back, {username}!"))

    def animate_button(self, button):
        anim = QPropertyAnimation(button, b"geometry")
        rect = button.geometry()
        anim.setStartValue(rect)
        anim.setKeyValueAt(0.5, rect.adjusted(-5, -5, 5, 5))
        anim.setEndValue(rect)
        anim.setDuration(200)
        anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        anim.start()
        self._last_anim = anim  # Objekt speichern, sonst sofort gelöscht!

    def fade_in_widget(self, widget, duration=700):
        effect = QtWidgets.QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        anim = QPropertyAnimation(effect, b"opacity")
        anim.setDuration(duration)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        anim.start()
        widget._fade_anim = anim

    def add_shadow(self, widget, blur=16, x=0, y=3, color=QtGui.QColor(44, 62, 80, 90)):
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(blur)
        shadow.setOffset(x, y)
        shadow.setColor(color)
        widget.setGraphicsEffect(shadow)
        widget._shadow = shadow
        return shadow

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 587)
        MainWindow.setMinimumSize(QtCore.QSize(411, 587))
        MainWindow.setMaximumSize(QtCore.QSize(411, 587))
        MainWindow.setStyleSheet("/* --------- Grund-Layout --------- */\n"
"QWidget {\n"
"    background-color: #f9fafc;\n"
"    color: #1c274c;\n"
"    border-radius: 28px;\n"
"}\n"
"\n"
"/* --------- Kopfzeile --------- */\n"
"QFrame#header, QMenuBar, QToolBar {\n"
"    background-color: #1c274c;\n"
"    color: #fff;\n"
"    border-radius: 24px;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"    padding: 14px 24px;\n"

"}\n"
"\n"
"/* --------- Button (Translate, Nav, etc.) --------- */\n"
"QPushButton {\n"
"    background-color: #ff6c1a;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"



"}\n"
"QPushButton:hover {\n"
"    background-color: #ff881a;\n"
"}\n"
"\n"
"/* --------- Eingabe/Ausgabe (Textfelder) --------- */\n"
"QLineEdit, QTextEdit, QPlainTextEdit, QTextBrowser {\n"
"    background-color: #fff;\n"
"    color: #1c274c;\n"
"    border: 2px solid #e0e6ed;\n"
"    border-radius: 22px;\n"
"    padding: 14px 18px;\n"
"    font-size: 17px;\n"

"}\n"
"\n"
"/* --------- Übersetzungsboxen / Karten --------- */\n"
"QFrame#card, QLabel.card, QTextBrowser.card {\n"
"    background-color: #f4f6fa;\n"
"    color: #1c274c;\n"
"    border: none;\n"
"    border-radius: 22px;\n"
"    padding: 16px;\n"
"    font-size: 17px;\n"
"    margin-bottom: 18px;\n"

"}\n"
"\n"
"/* --------- ComboBox (Sprache wählen) --------- */\n"
"QComboBox {\n"
"    background-color: #e9effa;\n"
"    color: #1c274c;\n"
"    border: none;\n"
"    border-radius: 16px;\n"
"    padding: 10px 22px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    min-width: 120px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background: #fff;\n"
"    border-radius: 14px;\n"
"    color: #1c274c;\n"
"    selection-background-color: #e9effa;\n"
"}\n"
"\n"
"/* --------- runde Icon-Flächen / Bubbles --------- */\n"
"QLabel#icon, QLabel.bubble {\n"
"    background: #e9effa;\n"
"    border-radius: 50px;\n"
"    min-width: 44px;\n"
"    min-height: 44px;\n"
"    max-width: 44px;\n"
"    max-height: 44px;\n"
"    margin: 6px;\n"
"    display: flex;\n"
"    align-items: center;\n"
"    justify-content: center;\n"
"    font-size: 22px;\n"
"}\n"
"\n"
"/* --------- Navigationsleiste --------- */\n"
"QFrame#navbar, QWidget#navbar {\n"
"    background: #fff;\n"
"    border-radius: 22px;\n"
"    border-top: 1.5px solid #e0e6ed;\n"
"    color: #1c274c;\n"
"    padding: 10px 0 0 0;\n"
"    font-size: 15px;\n"

"}\n"
"\n"
"/* --------- Navigations-Buttons --------- */\n"
"QPushButton#nav {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #1c274c;\n"
"    border-radius: 16px;\n"
"    font-size: 16px;\n"
"    padding: 8px 20px;\n"
"}\n"
"QPushButton#nav:checked, QPushButton#nav:hover {\n"
"    color: #ff6c1a;\n"
"    background: #e9effa;\n"
"}\n"
"\n"
"/* --------- Kleinere Elemente --------- */\n"
"QLabel, QCheckBox, QRadioButton {\n"
"    font-size: 15px;\n"
     
"}\n"
"\n"
"/* --------- Globale Schatten --------- */\n"
"QWidget, QFrame, QTextEdit, QLineEdit, QPushButton {\n"
"    /* Box-Shadows für modernen Soft-Look */\n"

"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setStyleSheet("background-image: url(C:/Users/Felix/Documents/easytranslate/icons/wallpaper.jpg);\n"
# "background-repeat: no-repeat;\n"
# "background-position: center;\n"
# "")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 70, 391, 51))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QWidget {\n"
"    background-color: #f9fafc;\n"
"    color: #1c274c;\n"
"    border-radius: 28px;\n"
"}\n"
"\n"
"/* Alle QFrame mit modernem, sehr hellem Hintergrund */\n"
"QFrame {\n"
"    background-color: #F7F2F9;\n"
"    border-radius: 22px;\n"

"}\n"
"\n"
"/* Orange Button mit schwarzem Text */\n"
"QPushButton {\n"
"    background-color: #F7F2F9;\n"
"    color: #3D3D3E;  /* Standard Schwarz */\n"
"    border: none;\n"
"    border-radius: 22px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"

"}\n"
"QPushButton:hover {\n"
"    background-color: #F7F2F9;  /* Bleibt gleich */\n"
"    color: #000000;             /* Noch dunkleres Schwarz */\n"
"\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #F7F2F9;      /* Passend zum Frame */\n"
"    color: #1c274c;                 /* Dunkelblau als Standardtext */\n"
"    border: 1.5px solid #F7F2F9;    /* Subtiler Rahmen */\n"
"    border-radius: 16px;\n"
"    padding: 8px 18px;\n"
"    font-family: \'SF Pro Display\', \'Segoe UI\', Arial, sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1.5px solid #F7F2F9;    /* Orange als Fokus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"    border-radius: 12px;\n"
"    width: 30px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #fff;               /* Dropdown-Liste weiß */\n"
"    color: #1c274c;\n"
"    border-radius: 12px;\n"
"    font-family: \'SF Pro Display\', \'Segoe UI\', Arial, sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"    selection-background-color: #e9effa; /* Hellblauer Select */\n"
"    selection-color: #ff6c1a;            /* Orange bei Auswahl */\n"
"    padding: 6px 14px;\n"
"    outline: none;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.swapButton = QtWidgets.QPushButton(parent=self.frame)
        self.swapButton.setGeometry(QtCore.QRect(170, 13, 51, 24))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.swapButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        self.swapButton.setFont(font)
        self.swapButton.setStyleSheet("")
        self.swapButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Felix/Documents/easytranslate/resources/icons/repeat.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.swapButton.setIcon(icon)
        self.swapButton.setObjectName("swapButton")
        self.languageCombo1 = QtWidgets.QComboBox(parent=self.frame)
        self.languageCombo1.setGeometry(QtCore.QRect(10, 7, 165, 38))
        self.languageCombo1.setObjectName("languageCombo1")
        self.languageCombo2 = QtWidgets.QComboBox(parent=self.frame)
        self.languageCombo2.setGeometry(QtCore.QRect(221, 7, 165, 38))
        self.languageCombo2.setCurrentText("")
        self.languageCombo2.setObjectName("languageCombo2")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 140, 391, 191))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("QWidget {\n"
"    background-color: #f9fafc;\n"
"    color: #1c274c;\n"
"    border-radius: 28px;\n"
"}\n"
"\n"
"/* Alle QFrame mit modernem, sehr hellem Hintergrund */\n"
"QFrame {\n"
"    background-color: #F7F2F9;\n"
"    border-radius: 22px;\n"

"}\n"
"\n"
"/* Orange Button mit schwarzem Text */\n"
"QPushButton {\n"
"    background-color: #F7F2F9;\n"
"    color: #3D3D3E;  /* Standard Schwarz */\n"
"    border: none;\n"
"    border-radius: 22px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"

"}\n"
"QPushButton:hover {\n"
"    background-color: #F7F2F9;  /* Bleibt gleich */\n"
"    color: #000000;             /* Noch dunkleres Schwarz */\n"
"\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #F7F2F9;\n"
"    color: #1c274c;\n"
"    border: 1.5px solid #F7F2F9;\n"
"    border-radius: 18px;\n"
"    padding: 12px 16px;\n"
"    font-family: \'SF Pro Display\', \'Segoe UI\', Arial, sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"

"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1.5px solid #F7F2F9; /* Orange als Fokus */\n"
"    outline: none;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.textEntry = QtWidgets.QTextEdit(parent=self.frame_2)
        self.textEntry.setGeometry(QtCore.QRect(10, 10, 371, 161))
        self.textEntry.setObjectName("textEntry")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 380, 391, 191))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("QWidget {\n"
"    background-color: #f9fafc;\n"
"    color: #1c274c;\n"
"    border-radius: 28px;\n"
"}\n"
"\n"
"/* Alle QFrame mit modernem, sehr hellem Hintergrund */\n"
"QFrame {\n"
"    background-color: #F7F2F9;\n"
"    border-radius: 22px;\n"

"}\n"
"\n"
"/* Orange Button mit schwarzem Text */\n"
"QPushButton {\n"
"    background-color: #F7F2F9;\n"
"    color: #3D3D3E;  /* Standard Schwarz */\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"

"}\n"
"QPushButton:hover {\n"
"    background-color: #F7F2F9;  /* Bleibt gleich */\n"
"    color: #000000;             /* Noch dunkleres Schwarz */\n"
"\n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.copyButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.copyButton.setGeometry(QtCore.QRect(340, 150, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.copyButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        self.copyButton.setFont(font)
        self.copyButton.setStyleSheet("/* Orange Button mit schwarzem Text */\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"

"\n"
"}")
        self.copyButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Felix/Documents/easytranslate/resources/icons/copy.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.copyButton.setIcon(icon1)
        self.copyButton.setIconSize(QtCore.QSize(16, 16))
        self.copyButton.setObjectName("copyButton")
        self.ttsButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.ttsButton.setGeometry(QtCore.QRect(310, 150, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 242, 249))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 62, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.ttsButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        self.ttsButton.setFont(font)
        self.ttsButton.setStyleSheet("/* Orange Button mit schwarzem Text */\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"

"\n"
"\n"
"}")
        self.ttsButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Felix/Documents/easytranslate/resources/icons/volume-2.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ttsButton.setIcon(icon2)
        self.ttsButton.setIconSize(QtCore.QSize(16, 16))
        self.ttsButton.setObjectName("ttsButton")
        self.textOutput = QtWidgets.QLabel(parent=self.frame_3)
        self.textOutput.setGeometry(QtCore.QRect(20, 20, 351, 121))
        self.textOutput.setFont(self.textEntry.font())
        self.textOutput.setText("")
        self.textOutput.setObjectName("textOutput")
        # Output-Box exakt gleiche Schrift wie Input-Box
        self.textOutput.setFont(self.textEntry.font())
        self.textOutput.setAlignment(
    QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop
)
        self.textOutput.setStyleSheet(
    """
    background-color: #F7F2F9;
    color: #1c274c;
    border: 1.5px solid #F7F2F9;
    border-radius: 18px;
    padding: 12px 16px;
    font-family: 'SF Pro Display', 'Segoe UI', Arial, sans-serif;
    font-weight: bold;
    font-size: 16px;
    """
)
        self.translateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.translateButton.setEnabled(True)
        self.translateButton.setGeometry(QtCore.QRect(170, 320, 71, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 108, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 108, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 108, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 108, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 108, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 108, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 108, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 108, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 108, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.translateButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(1)
        font.setBold(True)
        self.translateButton.setFont(font)
        self.translateButton.setStyleSheet("/* Orange Button mit schwarzem Text */\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"

"}\n"
"QPushButton:hover {\n"
"    background-color: #F28638;  /* Bleibt gleich */\n"
"    color: #000000;             /* Noch dunkleres Schwarz */\n"
"\n"
"}")
        self.translateButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Felix/Documents/easytranslate/resources/icons/chevrons-down.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.translateButton.setIcon(icon3)
        self.translateButton.setIconSize(QtCore.QSize(32, 32))
        self.translateButton.setObjectName("translateButton")
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(-20, 0, 451, 51))
        self.frame_4.setStyleSheet("background-color: #003366")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.logoLabel = QtWidgets.QPushButton(parent=self.frame_4)
        self.logoLabel.setGeometry(QtCore.QRect(0, 0, 181, 51))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Felix/Documents/easytranslate/resources/icons/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.logoLabel.setIcon(icon4)
        self.logoLabel.setIconSize(QtCore.QSize(48, 48))
        self.logoLabel.setObjectName("logoLabel")
        self.welcomeLabel = QtWidgets.QLabel(parent=self.frame_4)
        self.welcomeLabel.setGeometry(QtCore.QRect(230, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(1)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet("color: #FFFFFF")
        self.welcomeLabel.setObjectName("welcomeLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        buttons = [self.translateButton, self.ttsButton, self.copyButton, self.swapButton, self.logoLabel]
        for btn in buttons:
                btn.clicked.connect(lambda checked, b=btn: self.animate_button(b))


        card_shadow = QtGui.QColor(44, 62, 80, 60)      # Neutral, leicht bläulich
        self.add_shadow(self.frame, blur=18, x=0, y=6, color=card_shadow)
        self.add_shadow(self.frame_4, blur=18, x=0, y=6, color=card_shadow)
        self.add_shadow(self.frame_2, blur=18, x=0, y=6, color=card_shadow)
        self.add_shadow(self.frame_3, blur=18, x=0, y=6, color=card_shadow)
        self.add_shadow(self.translateButton, blur=16, x=0, y=4, color=QtGui.QColor(44, 62, 80, 60))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)