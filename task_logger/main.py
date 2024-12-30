from ParserOfElements import ParserOfElements

def main():
    url = input("Введите задачу с LeetCode: ")
    row = []
    poe = ParserOfElements()
    html = poe.load_html(url)
    row = poe.parse(html, row)
    print(row)


if __name__ == "__main__":
    main()