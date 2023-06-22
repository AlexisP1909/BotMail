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
VariablesEnvoiMail["destinateur"] = 'maintenanceswish@gmail.com'
VariablesEnvoiMail["password"] = 'kpptzjgmoqcwhrmw'
# Modifier les adresses mail suivantes pour le destinataire (l'employé qui gère la planification d'entretiens) et son superviseur 
VariablesEnvoiMail["destinataire"] = ['nicolas.gorgette@epfedu.fr']
mailDuSuperviseur = 'alexis.pouillieute@epfedu.fr'