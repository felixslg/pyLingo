pyLingo
pyLingo ist ein moderner, plattformunabhängiger Desktop-Übersetzer mit Sprachausgabe und einfacher Bedienung, entwickelt mit Python, PyQt6 und Google Text-to-Speech (gTTS).

<!-- Füge einen Screenshot hinzu, falls vorhanden -->

Features
Schnelle Textübersetzung zwischen Deutsch, Englisch, Spanisch, Französisch und Italienisch

Sprachauswahl über intuitive Drop-down-Menüs

Kopieren der Übersetzung per Knopfdruck

Vorlesen des Ergebnisses (Text-to-Speech) direkt im Programm

Modernes, responsives UI (an iOS angelehnt)

Benachrichtigungen bei Aktionen (z.B. „Kopiert!“ oder „Vorlesen…“)

Technologie
Python 3

PyQt6 (für die Benutzeroberfläche)

gtts (Google Text-to-Speech)

playsound (Audio-Ausgabe)

Installation
bash
Kopieren
Bearbeiten
git clone https://github.com/deinusername/easytranslate.git
cd easytranslate
python -m venv venv
venv\Scripts\activate      # Windows
# oder
source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
python src/main.py
Hinweise
Für Text-to-Speech ist eine Internetverbindung erforderlich (gTTS nutzt Google-API).

Getestet unter Windows 10/11. Für Linux/Mac kann es zu Anpassungsbedarf bei der Audio-Ausgabe kommen.
