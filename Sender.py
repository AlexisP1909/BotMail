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
    message['To'] = destinataire               #destinataire du mail

    context = ssl.create_default_context()     
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(destinateur, password)             #connexion au serveur Gmail
        server.sendmail(destinateur, destinataire, message)    #envoie le mail
        print("ENVOYE")
    server.quit()