import smtplib, ssl           #le module smtplib définit un objet de session client SMTP
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

html_content=""

smtp_server = 'smtp.gmail.com'
port = 465
destinateur = 'alexis.pouillieute@gmail.com'
password = 'GMAAlexis2002-'                        #mdp généré avec gmail
destinataire = 'alexis.pouillieute@epfedu.fr'

message = MIMEMultipart()

html_part = MIMEText(html_content, 'html')
message.attach(html_part)

message['Subject'] = 'Maintenances à planifier'    #objet du mail
message['From'] = destinateur              #destinateur du mail
message['To'] = destinataire               #destinataire du mail

context = ssl.create_default_context()     
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(destinateur, password)             #connexion au serveur Gmail
    server.sendmail(destinateur, destinataire, message.as_string())    #envoie le mail
server.quit()