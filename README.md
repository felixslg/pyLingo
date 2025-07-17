# pyLingo

**pyLingo** ist ein moderner, plattformunabhängiger Desktop-Übersetzer mit Sprachausgabe und einfacher Bedienung, entwickelt mit Python, PyQt6 und Google Text-to-Speech (gTTS).

<img width="406" height="612" alt="image" src="https://github.com/user-attachments/assets/85613448-53e1-4fd4-9a61-2a7e29ee56d8" />


## Features

- **Schnelle Textübersetzung** zwischen Deutsch, Englisch, Spanisch, Französisch und Italienisch
- **Sprachauswahl** über intuitive Drop-down-Menüs
- **Kopieren der Übersetzung** per Knopfdruck
- **Vorlesen des Ergebnisses** (Text-to-Speech) direkt im Programm
- **Modernes, responsives UI** (an iOS angelehnt)
- **Benachrichtigungen** bei Aktionen (z.B. „Kopiert!“ oder „Vorlesen…“)

## Technologie

- **Python 3**
- **PyQt6** (für die Benutzeroberfläche)
- **gtts** (Google Text-to-Speech)
- **playsound** (Audio-Ausgabe)

## Installation

```bash
git clone https://github.com/felixslg/pyLingo.git
cd easytranslate
python -m venv venv
venv\Scripts\activate      # Windows
# oder
source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
python src/main.py
