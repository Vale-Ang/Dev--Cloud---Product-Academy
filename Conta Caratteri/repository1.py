from typing import TextIO

"""Recupera un oggetto imput/output (IO) di tipo testuale da un file specificato"""
def get_file(file_path: str) -> TextIO:
    return open(file_path, "r")