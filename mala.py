#!/usr/bin/python3
# Este script envia uma mala direta para todas pessoas a partir do texto data/aviso.html

from sendemail import connect, send_html_mail

import os
import time
import csv
import local
from validate_email import validate_email
from unidecode import unidecode


def send_mass_mail(datafile):
    conn = None
    smtp_login = None
    if isinstance(local.smtp, dict) and 'login' in local.smtp:
        smtp_login = local.smtp['login']
        password = local.smtp['password']
        conn = connect(smtp_login, password)

    tot_emails = 0
    tot_lidos = 0
    with open('data/aviso.html', 'r') as f:
        html = f.read()

    with open(datafile, 'r') as f:
        reader = csv.reader(f)
        try:
            for aluno in reader:
                tot_lidos += 1
                email = aluno[0].strip().replace(" ", "")
                is_valid = validate_email(email)
                if is_valid:
                    if 'bcc' in local.smtp:
                        email = [email, local.smtp['bcc']]
                    send_html_mail(conn, local.sender, email, local.subject, html)
                    tot_emails += 1
                    if tot_emails % 50 == 0:
                        print('sent %d' % tot_emails)
                        conn.quit()
                        time.sleep(30)
                        conn = connect(smtp_login, password)
                else:
                    print('Email inválido: %s' % email)
            conn.quit()
        except Exception as E:
            print('Erro no envio do email %s' % email)
            print(E)

    print('Emails lidos: %d' % tot_lidos)
    print('Emails enviados: %d' % tot_emails)


if __name__ == "__main__":
    send_mass_mail('mala2.csv')
    exit(0)
