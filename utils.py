import os
import warnings
from email.message import EmailMessage
import smtplib
import json


# Variables
data = None  # Pour send_mail


def send_mail(subject="Code terminé", credential_file="_credential.json", disp=False):
    """
    Cette focntion envoie un mail depuis et vers l'adresse spécifiée dans le fichier json credential_file
    avec l'objet demandé. Elle est paramétrée pour fonctionner avec Yahoo mail

    :param str subject: Objet du mail
    :param str credential_file: Chemin du fichier json contenant les identifiants de la boite mail
    (champ username du json) et le mot de passe (champ password du json) pour plus de sécurité
    :param bool disp: Si True, print la variable subject dans la console
    """
    global data
    if disp:
        print(subject)
    if data is None:
        if os.path.isfile(credential_file):
            with open(credential_file) as read_file:
                data = json.load(read_file)
        else:
            warnings.warn("Au fichier credential détecté pour envoyer des notifications par mail")
            return None
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = data["username"]
        msg['To'] = data["username"]

        s = smtplib.SMTP('smtp.mail.yahoo.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication

        s.login(data["username"], data["password"])
        s.send_message(msg)
        s.quit()
    except Exception as e:  # Empêche le code de planter quand le mail n'est pas parti
        warnings.warn("Le mail n'a pas été envoyé")