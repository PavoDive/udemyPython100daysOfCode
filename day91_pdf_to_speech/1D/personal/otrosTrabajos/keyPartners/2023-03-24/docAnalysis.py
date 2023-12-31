# coding: utf-8

from pdfminer.high_level import extract_text

def convierte_pdf_txt():
    nombre_documento = input("Gran maestro, ¿qué documento deseas abrir?\n")
    
    tx = extract_text(nombre_documento)
    
    nombre_salida = input("\n¿Y qué nombre deseas ponerle al archivo de salida?\n")
    with open(nombre_salida, "w") as file1:
        file1.write(tx)

