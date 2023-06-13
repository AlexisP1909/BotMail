import pandas as pd
from openpyxl import load_workbook
import datetime
import json
import os
from ExcelToJson import ExcelToPython
Nom_Feuille = 'Clients'
NuméroLigneEnTetes = 2
NomC_Entreprise = "Entreprise"
NomC_BornesSimpl = "Bornes Simples"
NomC_BornesDoubles = "Bornes Doubles"
NomC_Armoires = "Armoires"
NomC_NbDemiJournees = "Nombre de demi-journées"
NomC_Adresse = "Adresse"
NomC_Departement = "Département"
NomC_Contact = "Contact"
NomC_DateMiseEnService = "Date de mise en service"
NomC_Periodicite = "Périodicité en mois"
NomC_VisiteOrganisee = "Visite Organisée?"
nom_fichier = "PlanningSandbox.xlsx"
nom_fichierj = "data.json"
VariablesExcelToPython= {}
VariablesExcelToPython[Nom_Feuille] = "Clients"
VariablesExcelToPython[NuméroLigneEnTetes] = 2
VariablesExcelToPython[NomC_Entreprise] = "Entreprise"
VariablesExcelToPython[NomC_BornesSimpl] = "Bornes Simples"
VariablesExcelToPython[NomC_BornesDoubles] = "Bornes Doubles"
VariablesExcelToPython[NomC_Armoires] = "Armoires"
VariablesExcelToPython[NomC_NbDemiJournees] = "Nombre de demi-journées"
VariablesExcelToPython[NomC_Adresse] = "Adresse"
VariablesExcelToPython[NomC_Departement] = "Département"
VariablesExcelToPython[NomC_Contact] = "Contact"
VariablesExcelToPython[NomC_DateMiseEnService] = "Date de mise en service"
VariablesExcelToPython[NomC_Periodicite] = "Périodicité en mois"
VariablesExcelToPython[NomC_VisiteOrganisee] = "Visite Organisée?"
VariablesExcelToPython[NomC_VisiteOrganisee] = "Visite Organisée?"
if __name__=="__main__":
 