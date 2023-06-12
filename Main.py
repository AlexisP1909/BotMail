import pandas as pd
import openpyxl

# Charger le fichier Excel
wb = openpyxl.load_workbook('PlanningSandbox.xlsx')

# Sélectionner la feuille de calcul
feuille = wb.active

# Lire les données de la feuille de calcul dans un DataFrame pandas
data = feuille.values
colonnes = next(data)[0:]
df = pd.DataFrame(data, columns=colonnes)

print(df)