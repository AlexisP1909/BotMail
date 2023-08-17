from ExcelToJson import ExcelToPython
from Editor import create_html_content
from Sender import EnvoiMail
from config import VariablesExcelToPython,VariablesEnvoiMail,mailDuSuperviseur,PeriodeEntretienenMois

if __name__=="__main__":
    print("---Lancement du programme...---")
    ExcelToPython(VariablesExcelToPython)
    VariablesEnvoiMail["html_content"], VariablesEnvoiMail["date"], envoyerMail, envoiSuperviseur = create_html_content(VariablesExcelToPython["nom_fichierj"],PeriodeEntretienenMois)
    if envoiSuperviseur: VariablesEnvoiMail["destinataire"].append(mailDuSuperviseur) # S'il faut prévenir le superviseur, on ajoute son mail aux destinataires
    print("ENVOYÉ AU SUPERVISEUR:", envoiSuperviseur)
    if envoyerMail: EnvoiMail(VariablesEnvoiMail) # On envoie le mail si le script "Editor.py" (avec la fonction create_html_content()) l'a jugé nécessaire
    print("---Fin du programme---")