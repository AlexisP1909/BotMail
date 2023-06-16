import smtplib, ssl           #le module smtplib définit un objet de session client SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os
def EnvoiMail(Variables):
    html_content=Variables["html_content"]
    smtp_server = Variables["smtp_server"]
    port = Variables["port"]
    destinateur = Variables["destinateur"]
    password = Variables["password"]                        #mdp généré avec gmail
    destinataire = Variables["destinataire"]
    date = Variables["date"]

    message = MIMEMultipart()

    nom_fichiert = "Envoi_logs.txt"
    
    repertoire_actuel = os.path.dirname(os.path.abspath(__file__))
    # Créez le chemin absolu en combinant le répertoire de travail et le nom du fichier
    chemin_fichier = os.path.join(repertoire_actuel, nom_fichiert)
    
    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    message['Subject'] = f'{date.strftime("%B %Y")}:Maintenances à planifier'    #objet du mail
    message['From'] = destinateur              #destinateur du mail
    message['To'] = ", ".join(destinataire)               #destinataire du mail

    server = smtplib.SMTP_SSL(smtp_server, port) 
    server.ehlo()
    server.login(destinateur, password)             #connexion au serveur Gmail
    server.sendmail(destinateur, destinataire, message.as_string())    #envoie le mail
    print("ENVOYE")
    server.quit()
    fichier = open(chemin_fichier,'w')
    fichier.write(date.strftime('%d/%m/%Y')) 