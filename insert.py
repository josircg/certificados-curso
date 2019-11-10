#!/usr/bin/python3

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fpdf import FPDF
from sendemail import connect, send_mail

import os
import csv
import local
import matplotlib.font_manager as fontman
from validate_email import validate_email


def find_font_file(query):
    matches = []
    for path in fontman.findSystemFonts():
        if query in os.path.basename(path):
            matches.append( path ) 
    return matches


def tokenize(string):
    return ''.join(e for e in string if e.isalnum())


def gera_pdf(nome):
    font_path = find_font_file("DejaVuSans.ttf")
    img = Image.open("hd2019.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path[0], 20)
    color = 'rgb(0,0,0)'
    draw.text((140, 580), nome, fill=color, font=font)
    filename = tokenize(nome)
    img.save(filename+'.png', optimize=True, quality=20)
    pdf = FPDF(orientation='L', format='A4')
    pdf.add_page()
    pdf.image(filename+'.png', 0, 0, pdf.w, pdf.h)
    pdf.output(filename+'.pdf', 'F')        
    os.remove(filename+'.png')
    return filename+'.pdf'


tot_emails = 0
login = local.smtp['email']
password = local.smtp['password']
s = connect(login, password)
try:
    with open('aluno.csv', 'r') as f:
        reader = csv.reader(f)
        for aluno in reader:
            file_name = gera_pdf(aluno[0].upper())
            if len(aluno) > 1:
                email = aluno[1].strip()
                is_valid = validate_email(email)
                if is_valid:
                    send_mail(s, email, file_name)
                    print(email)
                    tot_emails += 1
                else:
                    print('Email inválido: %s' % email)
finally:
    s.quit()
    print('Emails gerados: %d' % tot_emails)




