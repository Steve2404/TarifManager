import pandas as pd


class Tarif:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)

    def get_salary(self, entgeltgruppe, stufe, salary_type="Brutto"):
        try:
            row = self.df[
                (self.df['Entgeltgruppe'] == entgeltgruppe.upper()) &
                (self.df['Type'].str.lower() == salary_type.lower())
            ]
            if row.empty:
                return 0
            return float(row[f'Stufe {stufe}'].values[0])
        except Exception:
            return 0