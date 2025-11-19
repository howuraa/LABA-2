import re
import requests
from datetime import datetime

class DateValidator:
    """
    Класс для проверки и поиска синтаксически корректных дат в формате ДД.ММ.ГГГГ
    """

    def __init__(self):
        self.date_pattern = re.compile(
            r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b'
        )

    def is_valid_date(self, date_str):
        """
        Проверяет, является ли строка корректной датой
        """
        if not self.date_pattern.match(date_str):
            return False

        try:
            day, month, year = map(int, date_str.split('.'))
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    def find_dates_in_text(self, text):
        """
        Находит все потенциальные даты в тексте и проверяет их корректность
        """
        potential_dates = self.date_pattern.findall(text)
        results = []

        for match in potential_dates:
            date_str = f"{match[0]}.{match[1]}.{match[2]}"
            is_valid = self.is_valid_date(date_str)
            results.append((date_str, is_valid))

        return results

    def find_dates_from_url(self, url):
        """
        Загружает текст с веб-страницы и ищет в нем даты
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return self.find_dates_in_text(response.text)
        except requests.RequestException as e:
            print(f"Ошибка при загрузке страницы: {e}")
            return []

    def find_dates_from_file(self, filename):
        """
        Читает текст из файла и ищет в нем даты
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            return self.find_dates_in_text(content)
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []


def main():
    """
    Основная функция для взаимодействия с пользователем
    """
    validator = DateValidator()

    print("Возможны проверки:")
    print("1 - Одной даты")
    print("2 - Дат в тексте")
    print("3 - Дат на веб-странице")
    print("4 - Дат в файле")

    choice = input("\nВведите номер типа проверки (1-4): ").strip()

    if choice == '1':
        date_input = input("Введите дату в формате ДД.ММ.ГГГГ: ").strip()
        if validator.is_valid_date(date_input):
            print(f"Дата корректна")
        else:
            print(f"Дата некорректна")

    elif choice == '2':
        text = input("Введите текст для поиска дат: ").strip()
        dates = validator.find_dates_in_text(text)
        print(f"\nНайдено дат: {len(dates)}")
        for date_str, is_valid in dates:
            status = "корректна" if is_valid else "некорректна"
            print(f"  {date_str} - {status}")

    elif choice == '3':
        url = input("Введите URL веб-страницы: ").strip()
        dates = validator.find_dates_from_url(url)
        print(f"\nНайдено дат: {len(dates)}")
        for date_str, is_valid in dates:
            status = "корректна" if is_valid else "некорректна"
            print(f"  {date_str} - {status}")

    elif choice == '4':
        filename = input("Введите имя файла: ").strip()
        dates = validator.find_dates_from_file(filename)
        if len(dates) == 0:
            print(f"\nНайдено дат: 0")
        elif len(dates) > 0:
            print(f"\nНайдено коррекнтых дат: {len(dates)}")
            for date_str, is_valid in dates:
                print(f"{date_str}")

    else:
        print("Неверный выбор")



if __name__ == "__main__":
    main()
