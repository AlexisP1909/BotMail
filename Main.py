import pandas as pd
import openpyxl

# Charger le fichier Excel
wb = openpyxl.load_workbook('chemin/vers/votre/fichier.xlsx')

# Sélectionner la feuille de calcul
feuille = wb.active

# Lire les données de la feuille de calcul dans un DataFrame pandas
data = feuille.values
colonnes = next(data)[0:]
df = pd.DataFrame(data, columns=colonnes)

# Sauvegarder le DataFrame au format CSV
df.to_csv('chemin/vers/votre/fichier.csv', index=False)
print('hello') 
