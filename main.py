"""Головний модуль програми"""

from app.io.input import read_from_console, read_from_file, read_from_csv
from app.io.output import print_to_console, write_to_file


def main():
    """Основна функція програми"""
    # Зчитування тексту з консолі
    text_console = read_from_console()
    print_to_console(text_console)
    write_to_file("output_console.txt", text_console)

    # Зчитування тексту з файлу
    text_file = read_from_file("input.txt")
    print_to_console(text_file)
    write_to_file("output_file.txt", text_file)

    # Зчитування тексту з CSV-файлу
    text_csv = read_from_csv("data.csv")
    print_to_console(text_csv)
    write_to_file("output_csv.txt", text_csv)

if __name__ == "__main__":
    main()
