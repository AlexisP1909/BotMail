import pandas as pd
from openpyxl import load_workbook
import datetime
import json
import os
from ExcelToJson import ExcelToPython
from Editor import create_html_content
VariablesExcelToPython= {}
VariablesExcelToPython["Nom_Feuille"] = "Clients"
VariablesExcelToPython["NuméroLigneEnTetes"] = 2
VariablesExcelToPython["NomC_Entreprise"] = "Entreprise"
VariablesExcelToPython["NomC_BornesSimpl"] = "Bornes Simples"
VariablesExcelToPython["NomC_BornesDoubles"] = "Bornes Doubles"
VariablesExcelToPython["NomC_Armoires"] = "Armoires"
VariablesExcelToPython["NomC_NbDemiJournees"] = "Nombre de demi-journées"
VariablesExcelToPython["NomC_Adresse"] = "Adresse"
VariablesExcelToPython["NomC_Departement"] = "Département"
VariablesExcelToPython["NomC_Contact"] = "Contact"
VariablesExcelToPython["NomC_DateMiseEnService"] = "Date de mise en service"
VariablesExcelToPython["NomC_Periodicite"] = "Périodicité en mois"
VariablesExcelToPython["NomC_VisiteOrganisee"] = "Visite Organisée?"
VariablesExcelToPython["NomC_VisiteOrganisee"] = "Visite Organisée?"
VariablesExcelToPython["nom_fichier"] = "PlanningSandbox.xlsx"
VariablesExcelToPython["nom_fichierj"] = "data.json"
if __name__=="__main__":
    ExcelToPython(VariablesExcelToPython)
    a = create_html_content(VariablesExcelToPython["nom_fichierj"])
    print(a)
