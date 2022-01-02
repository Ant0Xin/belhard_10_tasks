"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""


ROWS = "text.txt"


def revert_rows(f_name: str):
    with open(f_name) as file:
        with open("new_text.txt", "w") as w_file:
            for line in file:
                temp_list = line.partition(".")[0].split()
                temp_string = "." + " ".join(temp_list[::-1]) + "\n"
                w_file.write(temp_string)


if __name__ == "__main__":
    revert_rows(ROWS)
