#!/usr/bin/python
# -*- coding: utf-8 -*-

from fpdf import FPDF

pdf = FPDF(orientation='L', format='A4')
pdf.add_page()
pdf.image('certificado.jpg', 0, 0, pdf.w, pdf.h)
pdf.output('tuto1.pdf', 'F')
