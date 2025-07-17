# src/controller.py

from googletrans import Translator

LANG_MAP = {
    "Deutsch": "de",
    "Englisch": "en",
    "Spanisch": "es",
    "Französisch": "fr",
    "Italienisch": "it"
}

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    src = LANG_MAP.get(src_lang, "de")
    dest = LANG_MAP.get(dest_lang, "fr")
    try:
        result = translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"Fehler bei der Übersetzung: {e}"
    


