import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir('pdfPython/arquivos')
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f'pdfPython/arquivos/{arquivo}')
        
merger.write('pdfPython/arquivos/novo_arquivo.pdf')