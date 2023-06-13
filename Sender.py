import smtplib, ssl           #le module smtplib définit un objet de session client SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def EnvoiMail(Variables):
    html_content=Variables["html_content"]

    smtp_server = Variables["smtp_server"]
    port = Variables["port"]
    destinateur = Variables["destinateur"]
    password = Variables["password"]                        #mdp généré avec gmail
    destinataire = Variables["destinataire"]
    
    message = MIMEMultipart()

    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    message['Subject'] = 'Maintenances à planifier'    #objet du mail
    message['From'] = destinateur              #destinateur du mail
    message['To'] = ", ".join(destinataire)               #destinataire du mail

    server = smtplib.SMTP_SSL(smtp_server, port) 
    server.ehlo()
    server.login(destinateur, password)             #connexion au serveur Gmail
    server.sendmail(destinateur, destinataire, message.as_string())    #envoie le mail
    print("ENVOYE")
    server.quit()