import unittest
from aa import DateValidator


class TestDateValidator(unittest.TestCase):

    def setUp(self):
        self.validator = DateValidator()

    def test_correct_dates(self):
        dates = ["01.01.2023", "15.06.1999", "31.12.2020", "29.02.2020", "28.02.2021", "30.04.2022"]
        for date in dates:
            if not self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть правильной")

    def test_day_32_to_99(self):
        dates = ["32.01.2023", "35.05.2020", "40.12.1999", "99.06.2021"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_day_00_and_negative(self):
        dates = ["00.01.2023", "-5.05.2020", "-1.12.1999"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_month_13_to_99(self):
        dates = ["15.13.2023", "01.15.2020", "10.99.1999"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_month_00_and_negative(self):
        dates = ["15.00.2023", "01.-5.2020", "10.-1.1999"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_year_0000(self):
        dates = ["01.01.0000", "15.06.0000", "31.12.0000"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой: год 0000 не существует")

    def test_year_0001_to_9999(self):
        dates = ["01.01.0001", "15.06.1000", "31.12.9999"]
        for date in dates:
            if not self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть правильной")

    def test_year_000_to_999(self):
        dates = ["01.01.999", "15.06.500", "31.12.000"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_negative_year(self):
        dates = ["01.01.-100", "15.06.-500", "31.12.-001"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_slash_separator(self):
        dates = ["01/01/2023", "15/06/1999", "31/12/2020"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_dash_separator(self):
        dates = ["01-01-2023", "15-06-1999", "31-12-2020"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_comma_separator(self):
        dates = ["01,01,2023", "15,06,1999", "31,12,2020"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_space_separator(self):
        dates = ["01 01 2023", "15 06 1999", "31 12 2020"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_short_day_month(self):
        dates = ["1.01.2023", "01.1.2023", "1.1.2023"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_short_year(self):
        dates = ["01.01.23", "15.06.99", "31.12.20"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_invalid_february(self):
        dates = ["29.02.2021", "30.02.2020", "31.02.1999"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_invalid_30_day_months(self):
        dates = ["31.04.2023", "31.06.1999", "31.09.2020", "31.11.2021"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_letters_in_date(self):
        dates = ["ab.cd.efgh", "01.01.20ab", "xx.yy.zzzz"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")

    def test_symbols_in_date(self):
        dates = ["!!.@@.####", "##.$$.%%%%", "&&.**.^^^^"]
        for date in dates:
            if self.validator.is_valid_date(date):
                raise AssertionError(f"Дата {date} должна быть ошибкой")


if __name__ == '__main__':
    unittest.main()
