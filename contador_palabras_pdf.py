'''
Created by: Armando Hughes
22/07/2022
'''
import fitz
import tkinter as tk
from tkinter import messagebox
def inicio():
    ventana = tk.Tk()
    ventana.title('Contador de palabras')
    ventana.resizable(0, 0)
    ventana.config(bg = 'black')
    ventana.geometry("600x600+400+50")
    ############# FUNCIONES #####################
    def palabras_en_PDF(x, y):
        pdf_documento = x +'.pdf'
        documento = fitz.open(pdf_documento)
        numero_paginas = documento.pageCount
        l = []
        while numero_paginas > 0:
            numero_paginas = numero_paginas - 1
            l.append(numero_paginas)
        texto = ""
        for i in l:
            pagina = documento.load_page(i)
            texto1 = pagina.get_text("text")
            texto = texto1 + texto
            textoM = texto.upper()

        signos = ",;:-*)(._%&#$'´´/=<>¨|{}[]''1234567890\n!\"'´´"
        for i in signos:
            textoM = textoM.replace(i, "")
            textoM = textoM.replace('Ó', 'O')
            textoM = textoM.replace('Á', 'A')
            textoM = textoM.replace('É', 'E')
            textoM = textoM.replace('Í', 'I')
            textoM = textoM.replace('Ú', 'U')

        lista = textoM.split(" ")
        lista1 = set(lista)
        lista2 = list(lista1)
        lista2.remove('')
        lista3 = set(lista2)
        y1 = y.upper()
        y1 = y1.replace('Ó', 'O')
        y1 = y1.replace('Á', 'A')
        y1 = y1.replace('É', 'E')
        y1 = y1.replace('Í', 'I')
        y1 = y1.replace('Ú', 'U')
        for cc in sorted(lista3):
            m = lista.count(cc)
            if y1 == cc:
                return 'Número de apariciones \nen el texto: ' + str(m)

    def boton(ventana, relx, rely, command, texto, color, z):
        boton = tk.Button(ventana, cursor='hand2', text=texto, bg=color,
                          font=("Arial black", z), width=10, borderwidth=6,
                          relief="raised", command=command)
        boton.place(relx=relx, rely=rely)
    def label(ventana, texto, bg, fg, tipo_letra, tamaño_letra, x, y):
        miLabel = tk.Label(ventana, text=texto,
                           bg=bg, fg=fg, font=(tipo_letra, tamaño_letra))
        miLabel.place(relx=x, rely=y)
    ################## LABELS #######################
    label(ventana, 'CONTAR PALABRAS', 'black', 'light blue', "Bauhaus 93", 40, 0.15, 0.1)
    label(ventana, '¿Qué palabra quiere buscar?', 'black', 'light gray', "Arial black", 20, 0.1, 0.25)
    label(ventana, 'Nombre del texto en PDF:', 'black', 'light gray', 'Arial black', 20, 0.1, 0.45)
    ############### ENTRADAS #####################
    palabra = tk.StringVar()
    palabra21 = tk.Entry(ventana, textvar=palabra, width=20, font=('Arial black', 14),
                     cursor='hand2', bg='light green')
    palabra21.place(relx=0.15, rely=0.35)

    texto = tk.StringVar()
    texto21 = tk.Entry(ventana, textvar=texto, width=20, font=('Arial black', 14),
                     cursor='hand2', bg='light green')
    texto21.place(relx=0.15, rely=0.55)
    ######################################################
    def value ():
        x = texto.get()
        y = palabra.get()
        if x == '' or y == '':
            messagebox.showwarning("Error", "TODOS LOS CAMPOS DEBEN ESTAR LLENOS")
        elif ' ' in y:
            messagebox.showwarning("Error", "PARA EVITAR ERRORES NO SE ADMITEN ESPACIOS")
        else:
            try:
                l = palabras_en_PDF(x, y)
                LabelIND = tk.Label(ventana, text=l, fg="black",
                                    font=("Arial black", 16), borderwidth=6, relief='ridge')
                LabelIND.place(relx=0.1, rely=0.75)
            except:
                messagebox.showwarning("Error", "REVISA QUE EL TEXTO SE ENCUENTRE EN LA CARPETA")
    ################ BOTONES ####################
    boton(ventana, 0.8, 0.9, ventana.destroy, 'SALIR', 'gray', 10)
    boton(ventana, 0.78, 0.75, value, 'Contar', 'gray', 12)
    ventana.mainloop()

inicio()