import local
import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


def connect(login, password):
    conn = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    conn.login(login, password)
    return conn


def send_mail_arquivo(conn, remetente, destino, arquivo, subject):
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    # storing the senders email address   
    msg['From'] = remetente
    # storing the receivers email address
    if isinstance(destino, list):
        msg['To'] = destino[0]
    else:
        msg['To'] = destino
    # storing the subject  
    msg['Subject'] = subject
  
    # string to store the body of the mail 
    body = "Segue em anexo certificado de participação"
  
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent  
    fp = open(arquivo, "rb")
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form 
    p.set_payload(fp.read())
    fp.close()

    # encode into base64 
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', 'attachment', filename=arquivo)
  
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
  
    # Converts the Multipart msg into a string 
    text = msg.as_string()
    # sending the mail
    conn.sendmail(msg['From'], destino, text)
    return


def send_html_mail(conn, remetente, destino, subject, html):
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = remetente
    # storing the receivers email address
    if isinstance(destino, list):
        msg['To'] = destino[0]
    else:
        msg['To'] = destino
    # storing the subject
    msg['Subject'] = subject

    # attach the body with the msg instance
    msg.attach(MIMEText(html, 'html'))
    text = msg.as_string()
    conn.sendmail(msg['From'], destino, text)
    return


def test():
    if not os.path.exists('teste.pdf'):
        print('Arquivo teste.pdf não existe')
        exit(1)
    s = connect(local.smtp['login'], local.smtp['password'])
    print('Connected')
    send_mail_arquivo(s, local.sender, 'josircg@gmail.com', 'Teste', 'data/aviso.html')
    print('Email Enviado')
    s.quit()


if __name__ == "__main__":
    test()
    exit(0)
