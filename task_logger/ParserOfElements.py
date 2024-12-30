from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time

class ParserOfElements:
    def __init__(self):
        pass
    
    def load_html(self, url: str) -> str:
        # Настройка Firefox
        options = Options()
        options.add_argument("--headless")
        # Создание WebDriver
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        driver.set_page_load_timeout(240)  # Увеличиваем время ожидания до 3 минут
        try:
            # Открытие страницы
            driver.get(url)
        except:
            print("Ошибка: страница не загрузилась в отведенное время.")
        # Даем время странице загрузиться
        time.sleep(3)
        # Получаем HTML страницы после выполнения JavaScript
        html = driver.page_source
        # Закрываем браузер
        driver.quit()
        return html
    
    def parse(self, html: str, row: list[str]):
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find(
            "a",
            class_="no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]"
        )
        if title:
            row.append(title.text)

        level = soup.find(
            "div", 
            class_="relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-difficulty-easy dark:text-difficulty-easy") or soup.find(
                "div", 
                class_="relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-difficulty-medium dark:text-difficulty-medium") or soup.find(
                    "div", 
                    class_="relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-difficulty-hard dark:text-difficulty-hard")
        if level:
            row.append(level.text)
        
        
        acceptance_rate = soup.find("span", class_="text-md font-medium")
        if acceptance_rate:
                row.append(acceptance_rate.text)
        return row