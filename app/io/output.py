"""Модуль для роботи з виведенням даних"""

def print_to_console(text):
    """Виводить текст у консоль."""
    print(text)

def write_to_file(filename, text):
    """Записує текст у файл."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
