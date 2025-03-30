from app.io.input import read_from_console, read_from_file, read_from_csv
from app.io.output import print_to_console, write_to_file

def main():
    text = read_from_console()
    print_to_console(text)
    write_to_file("output.txt", text)

if __name__ == "__main__":
    main()