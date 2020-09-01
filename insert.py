#!/usr/bin/python3

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fpdf import FPDF
from sendemail import connect, send_mail_arquivo

import os
import sys
import csv
import local
import time
import matplotlib.font_manager as fontman
from validate_email import validate_email
from unidecode import unidecode


def find_font_file(query):
    matches = []
    for path in fontman.findSystemFonts():
        if query in os.path.basename(path):
            matches.append(path)
    return matches


def tokenize(string):
    return ''.join(e for e in string if e.isalnum())


def gera_pdf(nome):
    font_path = find_font_file("DejaVuSans.ttf")
    img = Image.open(local.modelo)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path[0], local.font_size)
    color = 'rgb(0,0,0)'
    draw.text((local.coluna, local.linha), nome, fill=color, font=font)
    filename = unidecode(tokenize(nome))
    img.save(filename+'.png', optimize=True, quality=50)
    pdf = FPDF(orientation='L', format='A4')
    pdf.add_page()
    pdf.title = local.subject
    pdf.author = 'PPGCI/IBICT/UFRJ'
    pdf.image(filename+'.png', 0, 0, pdf.w, pdf.h)
    dest_filename = filename+'.pdf'
    pdf.output(dest_filename, 'F')
    os.remove(filename+'.png')
    return dest_filename


def gera_certificados(filename):
    if not os.path.exists(filename):
        print('%s não encontrado' % filename)
        exit(1)

    conn = None
    smtp_login = None
    if isinstance(local.smtp, dict) and 'login' in local.smtp:
        smtp_login = local.smtp['login']
        password = local.smtp['password']
        conn = connect(smtp_login, password)

    tot_emails = 0
    tot_certificados = 0
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for aluno in reader:
                file_name = gera_pdf(aluno[0].upper())
                tot_certificados += 1
                if conn and file_name:
                    if len(aluno) > 1:
                        email = aluno[1].strip().replace(" ", "")
                        is_valid = validate_email(email)
                        if is_valid:
                            if 'bcc' in local.smtp:
                                email = [email, local.smtp['bcc']]
                            send_mail_arquivo(conn, local.sender, email, file_name, local.subject)
                            os.remove(file_name)
                            tot_emails += 1
                            if tot_emails % 50 == 0:
                                print('sent %d' % tot_emails)
                                conn.quit()
                                time.sleep(30)
                                conn = connect(smtp_login, password)
                        else:
                            print('Email inválido: %s' % email)
                    else:
                        print('Email não encontrado na linha ')
    finally:
        conn.quit()
        print('Certificados gerados: %d' % tot_certificados)
        print('Certificados enviados: %d' % tot_emails)
        return 0


if __name__ == "__main__":
    exit(gera_certificados(sys.argv[1]))