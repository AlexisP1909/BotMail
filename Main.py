from ExcelToJson import ExcelToPython
from Editor import create_html_content
from Sender import EnvoiMail
VariablesExcelToPython= {}
#Variables Excel
VariablesExcelToPython["Nom_Feuille"] = "Clients"
VariablesExcelToPython["NuméroLigneEnTetes"] = 2
#Entêtes des colonnes Excel 
VariablesExcelToPython["NomC_Entreprise"] = "Entreprise"
VariablesExcelToPython["NomC_BornesSimpl"] = "Bornes Simples"
VariablesExcelToPython["NomC_BornesDoubles"] = "Bornes Doubles"
VariablesExcelToPython["NomC_Armoires"] = "Armoires"
VariablesExcelToPython["NomC_NbDemiJournees"] = "Nombre de demi-journées"
VariablesExcelToPython["NomC_Adresse"] = "Adresse"
VariablesExcelToPython["NomC_Departement"] = "Département"
VariablesExcelToPython["NomC_Contact"] = "Contact"
VariablesExcelToPython["NomC_DateMiseEnService"] = "Date de mise en service"
VariablesExcelToPython["NomC_Periodicite"] = "Periodicité en mois"
VariablesExcelToPython["NomC_VisiteOrganisee"] = "Visite Organisée?"
# Noms de fichiers Excel et JSON
VariablesExcelToPython["nom_fichier"] = "Planning d'intervention Maintenance CENSURE POUR TESTS.xlsx"
VariablesExcelToPython["nom_fichierj"] = "data.json"

# Changer la période sur laquelle porte les rappels
PeriodeEntretienenMois= 3

VariablesEnvoiMail = {}
VariablesEnvoiMail["smtp_server"] = 'smtp.gmail.com'
VariablesEnvoiMail["port"] = 465
VariablesEnvoiMail["destinateur"] = 'alexis.pouillieute@gmail.com'
VariablesEnvoiMail["password"] = 'eramkhznecqpnuob'
# Modifier les adresses mail suivantes pour le destinataire (l'employé qui gère la planification d'entretiens) et son superviseur 
VariablesEnvoiMail["destinataire"] = ['alexis.pouillieute@epfedu.fr']
mailDuSuperviseur = 'nicolas.gorgette@epfedu.fr'

if __name__=="__main__":
    ExcelToPython(VariablesExcelToPython)
    VariablesEnvoiMail["html_content"], VariablesEnvoiMail["date"], envoyerMail, envoiSuperviseur = create_html_content(VariablesExcelToPython["nom_fichierj"],PeriodeEntretienenMois)
    if envoiSuperviseur: VariablesEnvoiMail["destinataire"].append(mailDuSuperviseur) # S'il faut prévenir le superviseur, on ajoute son mail aux destinataires
    print("ENVOYÉ AU SUPERVISEUR:", envoiSuperviseur)
    if envoyerMail: EnvoiMail(VariablesEnvoiMail) # On envoie le mail si le script "Editor.py" (avec la fonction create_html_content()) l'a jugé nécessaire
