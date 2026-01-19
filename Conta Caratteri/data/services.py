import re
from constant import REGEX_SENZA_SPAZI, REGEX_PAROLE_LETTERE, REGEX_FRASI
# ===========================
# Service
# ===========================

"""Conta i caratteri"""
def get_caratteri_len(text: str)-> int:
    if not text:
        return 0
    return len(text)

"""Restituisci il testo senza gli spazi"""
import re
def get_text_no_space(text: str) -> str:
    return "".join(re.findall(REGEX_SENZA_SPAZI, text))

"""Restituisce il numero di parole in una stringa"""
def get_words_number(text: str) -> int:
    if not text:
        return 0
    return len(re.findall(REGEX_PAROLE_LETTERE, text))

"""Restituisce il numero di frasi in una stringa"""
def get_phrase_number(text: str) -> int:
    if not text:
        return 0
    return len(re.findall(REGEX_FRASI, text))