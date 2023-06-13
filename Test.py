import smtplib, ssl           #le module smtplib définit un objet de session client SMTP
import csv
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

smtp_server = 'smtp.gmail.com'
port = 465
destinateur = ''
password = ''                        #mdp généré avec gmail
destinataire = 'nathan.lilamand@epfedu.fr'

with open(r"C:\Users\elora\OneDrive - Fondation EPF\Documents\Associations\Gala\Photos.csv") as f:    #on ouvre le fichier csv qui contient ligne par ligne les noms des images
    reader = csv.reader(f)
    lignes = list(reader)
    for i in range(len(lignes)):        #correspond au nombre de mail qui vont être envoyés
        message = MIMEMultipart('Photos Gala 2022')
        
        message.attach(MIMEText('envoyer une pièce jointe', 'plain'))
        l = lignes[i]
        n = ''.join(l)                             #transforme l'objet l (nom de l'image) en String 
        name = n.rstrip(n[-2])                     #on enlève les deux ";" à la fin du nom de l'image (ne sait pas pk y'en a 2 qui apparaissent 
                                                   #automatiquement à la fin du nom de l'image dans le fichier csv)
        with open(r"C:\Users\elora\OneDrive - Fondation EPF\Documents\Associations\Gala\Photos\%s" % name, 'rb') as attachment:    #on ouvre l'image
            file_part = MIMEBase('application', 'octet-stream')     
            file_part.set_payload(attachment.read())
            encoders.encode_base64(file_part)      #on convertit l'image en Base64
            file_part.add_header(
            'Content-Disposition',
            'attachment; filename='+ str(name)
            )
            message.attach(file_part)
            context = ssl.create_default_context()     
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(destinateur, password)             #connexion au serveur Gmail
                server.sendmail(destinateur, destinataire, message.as_string())    #envoie le mail

server.quit()
