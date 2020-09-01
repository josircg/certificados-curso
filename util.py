#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import local
import csv

from fpdf import FPDF
from insert import gera_pdf, gera_certificados


def teste_pdf(image_filename):
    pdf = FPDF(orientation='L', format='A4')
    pdf.add_page()
    pdf.image(image_filename, 0, 0, pdf.w, pdf.h)
    pdf.output('teste.pdf', 'F')
    print('teste.pdf criado')


def pdf_to_png(filename):
    dest_filename, dest_fileext = os.path.splitext(filename)
    command = 'pdftoppm %s %s -png -r 150 -singlefile' % (filename, dest_filename.split('/')[-1])
    os.system(command)
    print('PDF convertido: %s' % dest_filename.split('/')[-1])


# Remove os registros duplicados do csv original e grava em alunos
def remove_duplicados(filename):
    tot_gravados = 0
    tot_lidos = 0
    seen = set()  # set for fast O(1) amortized lookup
    with open(filename, 'r') as in_file, open('alunos.csv', 'w') as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)
        for aluno in reader:
            tot_lidos += 1
            if aluno[1].lower() in seen:
                continue  # skip duplicate
            seen.add(aluno[1].lower())
            writer.writerow(aluno)
            tot_gravados += 1

    print('Total Lidos: %d' % tot_lidos)
    print('Total Gravados: %d' % tot_gravados)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Indique o comando: convert_pdf <arquivo>, test_email ou test_insert <arquivo>')
        exit(1)
    if sys.argv[1] == 'convert_pdf':
        if len(sys.argv) == 3:
            pdf_to_png(sys.argv[2])
        else:
            print('Indique o arquivo como parâmetro para o comando convert_pdf')
    elif sys.argv[1] == 'test_email':
        gera_certificados('teste2.csv')
    elif sys.argv[1] == 'remove_duplic':
        if len(sys.argv) == 3:
            remove_duplicados(sys.argv[2])
            print('Arquivo alunos.csv gerado')
        else:
            print('Indique o arquivo como parâmetro para o comando remove_duplic')
    elif sys.argv[1] == 'test_insert':
        gera_pdf(' '.join(sys.argv[2:]))
        print('PDF Gerado')
    else:
        print('comando %s não definido' % sys.argv[0])

    exit(0)
