from ExcelToJson import ExcelToPython
from Editor import create_html_content
from Sender import EnvoiMail
VariablesExcelToPython= {}
#Variables Excel
VariablesExcelToPython["Nom_Feuille"] = "Clients"
VariablesExcelToPython["NuméroLigneEnTetes"] = 2
#Variables 
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
VariablesExcelToPython["nom_fichier"] = "Planning d'intervention Maintenance POUR TESTS.xlsx"
VariablesExcelToPython["nom_fichierj"] = "data.json"

VariablesEnvoiMail = {}
VariablesEnvoiMail["smtp_server"] = 'smtp.gmail.com'
VariablesEnvoiMail["port"] = 465
VariablesEnvoiMail["destinateur"] = 'alexis.pouillieute@gmail.com'
VariablesEnvoiMail["password"] = 'eramkhznecqpnuob'
VariablesEnvoiMail["destinataire"] = ['alexis.pouillieute@epfedu.fr']


if __name__=="__main__":
    ExcelToPython(VariablesExcelToPython)
    VariablesEnvoiMail["html_content"], VariablesEnvoiMail["date"] = create_html_content(VariablesExcelToPython["nom_fichierj"])
    #EnvoiMail(VariablesEnvoiMail)
