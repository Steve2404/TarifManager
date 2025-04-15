from datetime import datetime


class Employee:
    def __init__(self, name, entgeltgruppe, initial_stufe, start_date, end_date=None):
        self.name = name
        self.entgeltgruppe = entgeltgruppe
        self.initial_stufe = initial_stufe
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None

    def calculate_stufe_by_year(self, year):
        years = year - self.start_date.year
        return min(self.initial_stufe + years, 6)