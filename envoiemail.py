import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Paramètres de l'email
from_addr = "mickael.abin@ecoles-epsi.net"
to_addr = "pascal.billerach@ecoles-epsi.net"
subject = "exercice 1 python"
body = "<h1>Email HTML</h1><p>Ceci est un exemple d'email HTML.</p>"

# Configuration du serveur SMTP
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
smtp_user = from_addr
smtp_password = ":mic$84ABI"

# Création du MIMEMultipart
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject

# Ajout du corps de l'email
msg.attach(MIMEText(body, 'html'))

# Ajout de la pièce jointe
filename = "exercice1.py"
attachment = open("exercice1.py", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

# Connexion au serveur et envoi de l'email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_user, smtp_password)
text = msg.as_string()
server.sendmail(from_addr, to_addr, text)
server.quit()
