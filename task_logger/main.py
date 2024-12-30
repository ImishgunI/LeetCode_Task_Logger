from ParserOfElements import ParserOfElements
import openpyxl
import os

def main():
    url = input("Введите задачу с LeetCode: ")
    file = input("Введите путь до файла: ")

    row = []
    poe = ParserOfElements()
    html = poe.load_html(url)
    row = poe.parse(html, row)
    row.append(url)
    row.append('Solved')
    wb = 0
    if os.path.exists(file):
        wb = openpyxl.load_workbook(file)
    else:
        wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "LeetCode"
    ws.append(row)
    wb.save(file)


if __name__ == "__main__":
    main()