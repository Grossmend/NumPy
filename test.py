
import sys

with open('file.txt') as infile:
    for i, line in enumerate(infile):
        # записываем в переменную первую строку (должно быть имя файла)
        if i == 0:
            file_read = line.replace('\n', '')

        # записываем в переменную файл - ответ
        if i == 1:
            file_answer = line.replace('\n', '')

        # записываем в переменную вторую строку (должна быть нумерация строки)
        if i == 2:
            try:
                row_read = int(line.replace('\n', ''))
            except ValueError:
                sys.exit('Не могу преобразовать строку в файле в номер, выход')

if 'file_read' in locals() and 'row_read' in locals():
    with open(file_read) as infile_read:
        for i_read, line_read in enumerate(infile_read):
            if i_read == row_read:
                copy_text = line_read.replace('\n', '').lower()

if 'file_answer' in locals() and 'copy_text' in locals():
    with open(file_answer, 'a') as infile_read_append:
        infile_read_append.write(copy_text)