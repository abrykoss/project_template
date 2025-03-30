"""Модуль для роботи з введенням даних"""

import pandas as pd

def read_from_console():
    """Зчитує текст з консолі."""
    return input("Введіть текст: ")

def read_from_file(filename):
    """Зчитує дані з файлу."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def read_from_csv(filename):
    """Зчитує дані з CSV-файлу за допомогою pandas."""
    df = pd.read_csv(filename)
    return df.to_string()
