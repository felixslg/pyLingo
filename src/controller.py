# src/controller.py

from googletrans import Translator
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtWidgets
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.gui import Ui_MainWindow
from gtts import gTTS
from playsound import playsound
import tempfile
from PyQt6.QtCore import QThread, pyqtSignal

LANG_MAP = {
    "Deutsch": "de",
    "Englisch": "en",
    "Spanisch": "es",
    "Französisch": "fr",
    "Italienisch": "it"
}

class TTSThread(QThread):
    finished_signal = pyqtSignal()

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        from playsound import playsound
        try:
            playsound(self.filename)
        except Exception:
            pass
        self.finished_signal.emit()

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    src = LANG_MAP.get(src_lang, "de")
    dest = LANG_MAP.get(dest_lang, "fr")
    try:
        result = translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"Fehler bei der Übersetzung: {e}"
    
class TTSThread(QThread):
    finished_signal = pyqtSignal()

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        from playsound import playsound
        try:
            playsound(self.filename)
        except Exception:
            pass
        self.finished_signal.emit()

    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        for combo in [self.ui.languageCombo1, self.ui.languageCombo2]:
            combo.clear()
            combo.addItems(["Deutsch", "Englisch", "Spanisch", "Französisch", "Italienisch"])
        self.ui.translateButton.clicked.connect(self.do_translate)
        self.ui.swapButton.clicked.connect(self.swap_languages)
        self.ui.copyButton.clicked.connect(self.copy_output)
        self.ui.ttsButton.clicked.connect(self.speak_output)
        self._active_notifications = {}  # Dictionary für Notifications mit Text als Key

    def do_translate(self):
        text = self.ui.textEntry.toPlainText()
        src_lang = self.ui.languageCombo1.currentText()
        dest_lang = self.ui.languageCombo2.currentText()
        if text.strip():
            result = translate_text(text, src_lang, dest_lang)
            self.ui.textOutput.setText(result)
        else:
            self.ui.textOutput.setText("Bitte Text eingeben!")

    def swap_languages(self):
        c1 = self.ui.languageCombo1
        c2 = self.ui.languageCombo2
        i1 = c1.currentIndex()
        i2 = c2.currentIndex()
        c1.setCurrentIndex(i2)
        c2.setCurrentIndex(i1)

    def copy_output(self):
        text = self.ui.textOutput.text()
        QApplication.clipboard().setText(text)
        self.show_notification("copied!", parent_btn=self.ui.copyButton)


    def speak_output(self):
        text = self.ui.textOutput.text()
        if not text.strip():
            self.show_notification("no text available!", parent_btn=self.ui.ttsButton)
            return
        lang_map = {
            "Deutsch": "de",
            "Englisch": "en",
            "Spanisch": "es",
            "Französisch": "fr",
            "Italienisch": "it"
        }
        lang = lang_map.get(self.ui.languageCombo2.currentText(), "de")
        filename = os.path.join(os.getcwd(), "tts_output.mp3")
        tts = gTTS(text, lang=lang)
        tts.save(filename)

        # Notification wie bei Copy
        self.show_notification("reading...", parent_btn=self.ui.ttsButton, persist=True)

        # Merker, damit wir wissen, dass das gerade die TTS-Notification ist
        self._tts_active = True

        # Thread fürs Abspielen
        self.tts_thread = TTSThread(filename)
        self.tts_thread.finished_signal.connect(self.tts_playback_finished)
        self.tts_thread.start()

    def tts_playback_finished(self):
        notif = getattr(self, "_tts_notif", None)
        if notif is not None and notif.graphicsEffect():
            anim_out = QtCore.QPropertyAnimation(notif.graphicsEffect(), b"opacity")
            anim_out.setDuration(500)
            anim_out.setStartValue(1)
            anim_out.setEndValue(0)
            anim_out.finished.connect(notif.close)
            anim_out.start()
            notif._fade_anim = anim_out
            self._tts_notif = None
        # tts_output.mp3 löschen
        filename = os.path.join(os.getcwd(), "tts_output.mp3")
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception:
                pass

    def show_notification(self, message, parent_btn=None, persist=False):
        if parent_btn is None:
            parent_btn = self.ui.copyButton
        parent = parent_btn.parentWidget()
        notif = QtWidgets.QLabel(message, parent)
        notif.setStyleSheet("""
            background: #003366;
            color: white;
            border-radius: 10px;
            padding: 8px 8px;
            font-size: 12px;
        """)
        notif.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        notif.adjustSize()
        btn_center = parent_btn.rect().center()
        btn_center_in_parent = parent_btn.mapToParent(btn_center)
        notif_x = btn_center_in_parent.x() - notif.width() // 2 - 0  # <- Verschiebung falls nötig hier anpassen
        notif_y = parent_btn.geometry().bottom() + 10
        above_y = parent_btn.geometry().top() - notif.height() - 10
        if above_y >= 0:
            notif_y = above_y
        notif.move(notif_x, notif_y)
        notif.show()
        notif.raise_()
        effect = QtWidgets.QGraphicsOpacityEffect(notif)
        notif.setGraphicsEffect(effect)
        anim_in = QtCore.QPropertyAnimation(effect, b"opacity")
        anim_in.setDuration(200)
        anim_in.setStartValue(0)
        anim_in.setEndValue(1)
        anim_in.start()
        notif._fade_anim = anim_in

        if persist:
            self._tts_notif = notif

        def fade_out_and_close():
            if notif and notif.graphicsEffect():
                anim_out = QtCore.QPropertyAnimation(notif.graphicsEffect(), b"opacity")
                anim_out.setDuration(500)
                anim_out.setStartValue(1)
                anim_out.setEndValue(0)
                anim_out.finished.connect(notif.close)
                anim_out.start()
                notif._fade_anim = anim_out

        if not persist:
            QtCore.QTimer.singleShot(1500, fade_out_and_close)

        return notif
    


