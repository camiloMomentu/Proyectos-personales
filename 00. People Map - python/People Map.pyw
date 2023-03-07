# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:29:47 2021

@author: JFLORE1
"""

# People Map | Talent Analytics

# Librerías
from tkinter import *
import pandas as pd
import math
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import numpy as np
import getpass
import os
import tkinter.ttk as ttk
#from matplotlib.colors import to_rgb, to_hex
from tkinter import filedialog

# Seleccion de usuario
user = getpass.getuser()

op0 = r"D:\{}\One Drive\BANCO DE BOGOTA\Sanchez Sastoque, Walter Ivan - 12. People Map"
op1 = r'C:\Users\{}\BANCO DE BOGOTA\Sanchez Sastoque, Walter Ivan - 02. Repositorio de datos\02. Bases\12. People Map'
op2 = r"C:\Users\{}\OneDrive - BANCO DE BOGOTA\TALENT ANALYTICS\02. Repositorio de datos\02. Bases\12. People Map"
op3 = r"C:\Users\{}\BANCO DE BOGOTA\Sanchez Sastoque, Walter Ivan - 12. People Map"
op4 = r"C:\Users\{}\Downloads\12. People Map"
op5 = r"D:\Programación\People Map\12. People Map"

for i,pt in enumerate([op0, op1, op2, op3, op4, op5]):
    if os.path.exists(pt.format(user)):
        path = pt.format(user)
        print(f"Path_Principal({i}):", path)
        break

fondo = "white"


# Ventana
ventana = Tk()
ventana.iconbitmap(f"{path}/Recursos/Imagenes/Logo-Banco.ico")
ventana.title("People Map | Banco de Bogotá | Dir. Talento y Cultura | Talent Analytics")
ventana.minsize(800,400)
ventana.pack_propagate(FALSE)
ventana.config(bg="whitesmoke",bd = 0)
ventana.state('zoomed')
ventana_size_x = ventana.winfo_width()
ventana_size_y = ventana.winfo_height()

# Datos
planta = pd.read_csv(f"{path}/Consolidado People Map.csv")
planta['Prob renuncia']

planta['Pasivo Vacaciones']=planta['Pasivo Vacaciones'].replace({
    np.nan:0
    })
planta['Pasivo Vacaciones']= planta['Pasivo Vacaciones'].astype(int)

planta['Salario']= planta['Salario'].replace({
    np.nan:0
    })
planta['Salario']=planta['Salario'].astype(int)


planta['Costo Total'] = planta['Costo Total'].replace({
    np.nan:0
    })
planta['Costo Total'] = planta['Costo Total'].astype(int)


planta['Prob renuncia'] = planta['Prob renuncia'].replace({
    np.nan:-1
    })
planta['Prob renuncia'] = planta['Prob renuncia'].astype(float)

planta.loc[planta['Cod_Posicion']== 5, 'Cod Posic Jefe'] = 1
planta.loc[planta['Cod_Posicion']== 16297, 'Cod Posic Jefe'] = 1
planta.loc[planta['Cod_Posicion']== 17459, 'Cod Posic Jefe'] = 1
planta.loc[planta['Cod_Posicion']== 26012109, 'Cod Posic Jefe'] = 1
planta.loc[planta['Cod_Posicion']== 17667, 'Cod Posic Jefe'] = 1
planta.loc[planta['Cod_Posicion']== 13071, 'Cod Posic Jefe'] = 1
planta.loc[planta['Cod_Posicion']== 4291, 'Cod Posic Jefe'] = 1

planta.loc[planta['Cod_Posicion']== 53, 'Cod Posic Jefe'] = 5
planta.loc[planta['Cod_Posicion']== 14146, 'Cod Posic Jefe'] = 5
planta.loc[planta['Cod_Posicion']== 1410, 'Cod Posic Jefe'] = 5


# Usuarios y accesos 
usuarios_a = pd.read_excel(f"{path}/Usuarios y accesos.xlsx")

admin = usuarios_a[usuarios_a['Tipo usuario']=='admin']['Usuario'].values

# Listas
lista_lineas = []
posiciones  = []
lista_cuadros = []
lista_personas = []


# Cuadros
megacuadro = Canvas(ventana)
megacuadro.config(bg = fondo,bd = 0, borderwidth=0)
megacuadro.place(x = 0,y =-5)
megacuadro.config(width=ventana.winfo_width(),height=ventana.winfo_height())


def mover(x, y):
    if x >= 0:
        x = 0

    elif x < ((megacuadro.winfo_width()-ventana.winfo_width()))*-1:
        x =((megacuadro.winfo_width()-ventana.winfo_width()))*-1

    if y >= -5:
        y = -5

    elif y < ((megacuadro.winfo_height()-ventana.winfo_height()))*-1:
        y = ((megacuadro.winfo_height()-ventana.winfo_height()))*-1

    megacuadro.place(x = x, y = y)

import time
def drag_start(event):
    megacuadro._1click = (event.x ,event.y)

def drag_motion(event):
    x = megacuadro.winfo_x() - (megacuadro._1click[0] - (event.x_root - megacuadro.winfo_rootx()))
    y = megacuadro.winfo_y() - (megacuadro._1click[1] - (event.y_root - megacuadro.winfo_rooty()))
    mover(x,y)

def mover_rueda(event,tipo ='v'):
    if tipo == 'v':
        y = megacuadro.winfo_y() + int(event.delta/120)*3
        x = megacuadro.winfo_x()

    else:

        x = megacuadro.winfo_x() + int(event.delta/120)*5
        y = megacuadro.winfo_y()

    mover(x,y)

megacuadro.bind("<B1-Motion>",drag_motion)
megacuadro.bind("<Button-1>",drag_start)
megacuadro.bind("<MouseWheel>",mover_rueda)
megacuadro.bind('<Shift-MouseWheel>',lambda event: mover_rueda(event,'h'))
megacuadro.bind('<Button>',lambda event: mover_rueda(event,'h'))


legends = None
# imagenes
image = Image.open(f"{path}\Recursos\Imagenes\Imagen1.png").convert('RGBA')
image2 = Image.open(f"{path}\Recursos\Imagenes\Imagen2.png").convert('RGBA')
button = ImageTk.PhotoImage(image)
button2 = ImageTk.PhotoImage(image2)
flecha = Button(ventana,bd = 0, bg = fondo, image = button, width = 25, height = 90)
flecha.place(x = ventana.winfo_width()-40, y = -10)

fondo_imagen =Image.open(f"{path}/Recursos/Imagenes/fondo TA.png").convert('RGBA')
fondo_imagen_tk = ImageTk.PhotoImage(fondo_imagen)
fondo_megacuadro = megacuadro.create_image(int(ventana.winfo_width()/2),int(ventana.winfo_height()/2), image = fondo_imagen_tk)

despl_arriba = Image.open(f"{path}\Recursos\Imagenes\Imagen3.png").convert('RGBA')
despl_arriba2= Image.open(f"{path}\Recursos\Imagenes\Imagen4.png").convert('RGBA')
button3=ImageTk.PhotoImage(despl_arriba)
button4=ImageTk.PhotoImage(despl_arriba2)

desplegar_arriba = Button(ventana,bd = 0, bg = fondo, image = button3, width = 90, height = 25)
desplegar_arriba.place(x = 10, y = ventana.winfo_height()-70)

# Barra inferior
subcuadro = LabelFrame(ventana)
subcuadro.config(bg="whitesmoke",bd = 0)
subcuadro.place(x = 0,y = ventana.winfo_height()-53)
subcuadro.config(width=ventana.winfo_width(),height=50)
subcuadro.pack_propagate(False)


class subcuadro_simple():

    def __init__(self, expand = True, ocultar = False):

        #almacenamiento
        self.l_costos = []
        self.l_antiguedad = []
        self.l_vacaciones = []
        self.l_span_var = []
        self.l_evd = []
        self.l_evd_sep = []
        self.l_empresa = []
        self.costos_por_empresa = [[],[],[]] #0 directos, 1 temporales, 2 Aprendices
        self.l_edad = []

        # calif evd
        
        for count in lista_cuadros:
            self.l_costos.append(count.costo)
            self.l_antiguedad.append(count.antig)
            self.l_vacaciones.append(count.d_vacaciones)
            self.l_evd.append(count.calif_evd)
            self.l_evd_sep.append(count.EVD)
            self.l_empresa.append(count.empresa)
            self.l_edad.append(count.edad)

            if count.empresa == 'Bdb-Directo':
                self.costos_por_empresa[0].append(count.costo)
            elif count.empresa == 'BDB_Aprendiz':
                self.costos_por_empresa[2].append(count.costo)
            elif count.empresa == 'Vte':
                vacante = 'vacante'
            else:
                self.costos_por_empresa[1].append(count.costo)
        
        #Variables
        self.headcount_var = len(lista_cuadros)
        self.costos_var = int(sum(self.l_costos))
        self.antiguedad_var = np.nanmean(self.l_antiguedad) if len(self.l_antiguedad) > 0 else 0
        self.vacaciones_var = np.nanmean(self.l_vacaciones) if len(self.l_vacaciones) > 0 else 0
        
        self.evd_var = [
            len(list(filter(lambda tipo: tipo == 'Alto', self.l_evd))), 
            len(list(filter(lambda tipo: tipo == 'Medio', self.l_evd))),
            len(list(filter(lambda tipo: tipo == 'Bajo', self.l_evd))), 
            len(list(filter(lambda tipo: tipo == 'Sin EVD', self.l_evd))) 
             ]
        
        self.evd_var_sep = [[
            len(list(filter(lambda tipo: tipo == 'A - Ejec', self.l_evd_sep))),
            len(list(filter(lambda tipo: tipo == 'B - Ejec', self.l_evd_sep)))+len(list(filter(lambda tipo: tipo == 'C Ejec', self.l_evd_sep))),
            len(list(filter(lambda tipo: tipo == 'D - Ejec', self.l_evd_sep)))
            ],
            [
            len(list(filter(lambda tipo: tipo == 'E - Aux', self.l_evd_sep)))+len(list(filter(lambda tipo: tipo == 'D Aux', self.l_evd_sep))),
            len(list(filter(lambda tipo: tipo == 'C - Aux', self.l_evd_sep))),
            len(list(filter(lambda tipo: tipo == 'A - Aux', self.l_evd_sep)))+len(list(filter(lambda tipo: tipo == 'B Aux', self.l_evd_sep)))                
            ],
            [len(list(filter(lambda tipo: tipo == 'Sin EVD', self.l_evd_sep)))
             ]]

        self.directos_var = len(list(filter(lambda tipo: tipo == 'Bdb-Directo', self.l_empresa)))
        self.temporales_var = (
            len(list(filter(lambda tipo: tipo == 'SUMMAR', self.l_empresa))) +
            len(list(filter(lambda tipo: tipo == 'Megalinea', self.l_empresa))) +
            len(list(filter(lambda tipo: tipo == 'Mision Temporal', self.l_empresa)))
            )
        
        self.aprendices_var = len(list(filter(lambda tipo: tipo == 'BDB_Aprendiz', self.l_empresa)))
        self.costos_directos_var =int(sum(self.costos_por_empresa[0]))
        self.costos_temporales_var = int(sum(self.costos_por_empresa[1]))
        self.costos_aprendices_var = int(sum(self.costos_por_empresa[2]))
        self.edad_var = np.nanmean(self.l_edad) if len(self.l_edad) > 0 else 0

        def espacio(ventana, ancho = 1):
            espacio = Label(ventana, bg = 'whitesmoke', bd = 0, width = ancho)
            espacio.pack(side = LEFT)

        if ocultar == False:

            if expand:

                subcuadro.config(height = 50)
                subcuadro.place(x = 0,y = ventana.winfo_height()-50)

                desplegar_arriba.place(x = 10, y = ventana.winfo_height()-69)
                desplegar_arriba.config(image = button3)

                # limpiar formato
                for i in subcuadro.winfo_children():
                    i.destroy()

                self.subcuadro_contenedor_simple = LabelFrame(subcuadro)
                self.subcuadro_contenedor_simple.config(bg = 'whitesmoke', bd = 0, height = 50)
                self.subcuadro_contenedor_simple.pack(side = TOP, fill = X)
                self.subcuadro_contenedor_simple.pack_propagate(False)

                espacio(self.subcuadro_contenedor_simple,2)

                self.i_headcount = Label(self.subcuadro_contenedor_simple,text = f'Personas = {self.headcount_var:,}')
                self.i_headcount.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 23, anchor = 'w')
                self.i_headcount.pack(side = LEFT)

                self.i_costos = Label(self.subcuadro_contenedor_simple,text = f'Costo mes = $ {self.costos_var:,}')
                self.i_costos.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 26, anchor = 'w')
                self.i_costos.pack(side = LEFT)

                self.i_antiguedad = Label(self.subcuadro_contenedor_simple,text = f'Antiguedad = {self.antiguedad_var: .0f}' + ' años')
                self.i_antiguedad.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 23, anchor = 'w')
                self.i_antiguedad.pack(side = LEFT)

                self.i_vacaciones = Label(self.subcuadro_contenedor_simple,text = f'Vacaciones = {self.vacaciones_var:.0f}' + ' días')
                self.i_vacaciones.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 23, anchor = 'w')
                self.i_vacaciones.pack(side = LEFT)
                
                # EVD
                self.evd_alto = Label(self.subcuadro_contenedor_simple,text = f'EVD Alto = {self.evd_var[0]:.0f}')
                self.evd_alto.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 23, anchor = 'w')
                self.evd_alto.pack(side = LEFT)

                self.evd_medio = Label(self.subcuadro_contenedor_simple,text = f'EVD Medio = {self.evd_var[1]:.0f}')
                self.evd_medio.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 23, anchor = 'w')
                self.evd_medio.pack(side = LEFT)
                
                self.evd_bajo = Label(self.subcuadro_contenedor_simple,text = f'EVD Bajo = {self.evd_var[2]:.0f}')
                self.evd_bajo.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 23, anchor = 'w')
                self.evd_bajo.pack(side = LEFT)
                
                self.evd_sin = Label(self.subcuadro_contenedor_simple,text = f'Sin EVD = {self.evd_var[3]:.0f}')
                self.evd_sin.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 23, anchor = 'w')
                self.evd_sin.pack(side = LEFT)
                
            else:

                # limpiar formato
                for i in subcuadro.winfo_children():
                    i.destroy()

                self.subcuadro_contenedor_grande = LabelFrame(subcuadro)
                self.subcuadro_contenedor_grande.config(bg = 'whitesmoke', bd = 0, height = 120)
                self.subcuadro_contenedor_grande.pack(side = TOP, fill = X)
                self.subcuadro_contenedor_grande.pack_propagate(False)

                # Headcount
                self.contenedor_headcount = LabelFrame(self.subcuadro_contenedor_grande)
                self.contenedor_headcount.config(width =190, bg = 'whitesmoke', bd = 0)
                self.contenedor_headcount.pack(side = LEFT, fill = Y)
                self.contenedor_headcount.pack_propagate(False)

                self.i_headcount = Label(self.contenedor_headcount,text =  f'Personas = {self.headcount_var:,}')
                self.i_headcount.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',11,'italic','bold'), width = 25, anchor = CENTER, height = 2)
                self.i_headcount.pack(side = TOP, fill = X)

                self.i_directos = Label(self.contenedor_headcount,text = f'      Directos =  {self.directos_var: .0f}')
                self.i_directos.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 25, anchor = 'w')
                self.i_directos.pack(side = TOP, fill = X)

                self.i_temporales = Label(self.contenedor_headcount,text = f'      Temporales =  {self.temporales_var: .0f}' )
                self.i_temporales.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 25, anchor = 'w')
                self.i_temporales.pack(side = TOP, fill = X)

                self.i_aprendices = Label(self.contenedor_headcount,text = f'      Aprendices =  {self.aprendices_var: .0f}')
                self.i_aprendices.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 25, anchor = 'w')
                self.i_aprendices.pack(side = TOP, fill = X)
                

                # Costos
                self.contenedor_costos = LabelFrame(self.subcuadro_contenedor_grande)
                self.contenedor_costos.config(width =200, bg = 'whitesmoke', bd = 0)
                self.contenedor_costos.pack(side = LEFT, fill = Y)
                self.contenedor_costos.pack_propagate(False)

                self.i_costos = Label(self.contenedor_costos,text = f'Costo mes = $ {self.costos_var:,}')
                self.i_costos.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',11,'italic','bold'), anchor = CENTER, height = 2)
                self.i_costos.pack(side = TOP, fill = X)

                self.i_directos_costos = Label(self.contenedor_costos,text = f'      Directos =  ${self.costos_directos_var: ,}')
                self.i_directos_costos.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 25, anchor = 'w')
                self.i_directos_costos.pack(side = TOP, fill = X)

                self.i_temporales_costos = Label(self.contenedor_costos,text =  f'      Temporales =  ${self.costos_temporales_var: ,}')
                self.i_temporales_costos.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 25, anchor = 'w')
                self.i_temporales_costos.pack(side = TOP, fill = X)

                self.i_aprendices_costos = Label(self.contenedor_costos,text =  f'      Aprendices =  ${self.costos_aprendices_var: ,}')
                self.i_aprendices_costos.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), width = 25, anchor = 'w')
                self.i_aprendices_costos.pack(side = TOP, fill = X)
                
                espacio(self.subcuadro_contenedor_grande,4)
                
                #Descriptivos
                self.contenedor_descrip = LabelFrame(self.subcuadro_contenedor_grande)
                self.contenedor_descrip.config(width =200, bg = 'whitesmoke', bd = 0)
                self.contenedor_descrip.pack(side = LEFT, fill = Y)
                self.contenedor_descrip.pack_propagate(False)

                self.i_antiguedad = Label(self.contenedor_descrip,text = f'Antiguedad promedio = {self.antiguedad_var: .0f}' + ' años')
                self.i_antiguedad.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), anchor = 'w', height = 2)
                self.i_antiguedad.pack(side = TOP, fill = X)

                self.i_edad = Label(self.contenedor_descrip,text = f'Edad promedio = {self.edad_var: .0f}'+' años')
                self.i_edad.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), anchor = 'w', height = 2)
                self.i_edad.pack(side = TOP, fill = X)

                self.i_dias_vac = Label(self.contenedor_descrip,text = f'Días vacaciones prom = {self.vacaciones_var: .0f}' + ' días')
                self.i_dias_vac.config(bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',10,'italic'), anchor = 'w', height = 2)
                self.i_dias_vac.pack(side = TOP, fill = X)
                
                espacio(self.subcuadro_contenedor_grande,4)

                # Evaluación de desempeño
                self.colores = ["#36C783","#ACE8D1","#EB7B75","#FFFFFF"]
                
                self.contenedor_evd = LabelFrame(self.subcuadro_contenedor_grande,text = 'Evaluación de desempeño')
                self.contenedor_evd.config(width =550, bg = 'whitesmoke', bd = 0, labelanchor = "n", fg = 'dimgray', font = ('calibri',10,'italic', 'bold'))
                self.contenedor_evd.pack(side = LEFT, fill = Y)
                self.contenedor_evd.pack_propagate(False)
                
                self.evd_graf = Canvas(self.contenedor_evd, bg = 'whitesmoke', bd = 0, width = 540, height = 100)
                self.evd_graf.pack(side = TOP)
                self.evd_graf.pack_propagate(False)
                
                self.ejec = Label(self.evd_graf, text = 'EVD Ejecutivos', font = ('calibri',9,'italic'), fg = 'dimgray', width = 30)
                self.ejec.pack(side = LEFT, anchor = 's')
                
                self.aux = Label(self.evd_graf, text = 'EVD Auxiliares', font = ('calibri',9,'italic'), fg = 'dimgray', width = 30)
                self.aux.pack(side = LEFT, anchor = 's')
                
                self.sin = Label(self.evd_graf, text = 'Sin EVD', font = ('calibri',9,'italic'), fg = 'dimgray', width = 10)
                self.sin.pack(side = LEFT, anchor = 's')
                
                self.leyendas = LabelFrame(self.evd_graf, bd = 0, bg = 'whitesmoke', width = 90, height = 60)
                self.leyendas.pack(side = RIGHT)
                
                self.indicador_alto = LabelFrame(self.leyendas, width = 10, height =10, bd= 0 , bg= self.colores[0])
                self.indicador_alto.place(x = 5,y= 2)
                
                self.indicador_medio = LabelFrame(self.leyendas, width = 10, height =10, bd= 0 , bg= self.colores[1])
                self.indicador_medio.place(x = 5,y= 17)
                
                self.indicador_bajo = LabelFrame(self.leyendas, width = 10, height =10, bd= 0 , bg= self.colores[2])
                self.indicador_bajo.place(x = 5,y= 32)
                
                self.indicador_sin = LabelFrame(self.leyendas, width = 10, height =10, bd= 0 , bg= self.colores[3])
                self.indicador_sin.place(x = 5,y= 47)
                
                self.leyenda_alto = Label(self.leyendas, text = 'Alto', bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',8), bd = 0)
                self.leyenda_alto.place(x = 15, y = 1)
                
                self.leyenda_medio = Label(self.leyendas, text = 'Medio', bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',8), bd = 0)
                self.leyenda_medio.place(x = 15, y = 16)
                
                self.leyenda_bajo = Label(self.leyendas, text = 'Bajo', bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',8), bd = 0)
                self.leyenda_bajo.place(x = 15, y = 31)
                
                self.leyenda_bajo = Label(self.leyendas, text = 'Sin evd', bg = 'whitesmoke', fg = 'dimgray', font = ('calibri',8), bd = 0)
                self.leyenda_bajo.place(x = 15, y = 46)
                
                maxim = max(max(self.evd_var_sep[0]),max(self.evd_var_sep[1]),max(self.evd_var_sep[2]))
                
                self.evd_graf.create_rectangle(30, 80-((self.evd_var_sep[0][0]/maxim)*68), 30+30, 90, fill=self.colores[0]) # Ejec Alto
                self.evd_graf.create_rectangle(80, 80-((self.evd_var_sep[0][1]/maxim)*68), 30+80, 90, fill = self.colores[1]) # Ejec Medio
                self.evd_graf.create_rectangle(130, 80-((self.evd_var_sep[0][2]/maxim)*68), 30+130, 90, fill =self.colores[2]) # Ejec Bajo
                
                self.evd_graf.create_rectangle(210, 80-((self.evd_var_sep[1][0]/maxim)*68), 30+210, 90, fill=self.colores[0]) # Aux Alto
                self.evd_graf.create_rectangle(260, 80-((self.evd_var_sep[1][1]/maxim)*68), 30+260, 90, fill=self.colores[1]) # Aux Medio
                self.evd_graf.create_rectangle(310, 80-((self.evd_var_sep[1][2]/maxim)*68), 30+310, 90, fill=self.colores[2]) # Aux Bajo
                
                self.evd_graf.create_rectangle(390, 80-((self.evd_var_sep[2][0]/maxim)*68), 30+390, 90, fill=self.colores[3]) # Sin evd
                
                # Etiquetas
                def etiqueta(text, x ,y):
                    etiq = Label(self.evd_graf, text = text, font = ('calibri',7,'italic'), fg = 'dimgray', width = 5, bd = 0, bg = 'whitesmoke')
                    etiq.place(x = x, y= y)
                
                etiqueta(self.evd_var_sep[0][0],30+1,(80-((self.evd_var_sep[0][0]/maxim)*68))-14) # Ejec Alto
                etiqueta(self.evd_var_sep[0][1],80+1,(80-((self.evd_var_sep[0][1]/maxim)*68))-14) # Ejec Medio
                etiqueta(self.evd_var_sep[0][2],130+1,(80-((self.evd_var_sep[0][2]/maxim)*68))-14) # Ejec Bajo
                
                etiqueta(self.evd_var_sep[1][0],210+1,(80-((self.evd_var_sep[1][0]/maxim)*68))-14) # Aux Alto
                etiqueta(self.evd_var_sep[1][1],260+1,(80-((self.evd_var_sep[1][1]/maxim)*68))-14) # Aux Medio
                etiqueta(self.evd_var_sep[1][2],310+1,(80-((self.evd_var_sep[1][2]/maxim)*68))-14) # Aux Bajo
                
                etiqueta(self.evd_var_sep[2][0],390+1,(80-((self.evd_var_sep[2][0]/maxim)*68))-14) # Sin evd


        else:

            for i in subcuadro.winfo_children():
                i.destroy()


# Barra lateral
listado_nombres = LabelFrame(ventana)
listado_nombres.config(bg='whitesmoke',width = 20,bd =0)
listado_nombres.place(x = ventana.winfo_width()-(listado_nombres.winfo_width()),y =-5)
listado_nombres.pack_propagate(False)

image_hom = Image.open(f"{path}\Recursos\Imagenes\Hombres.png").convert('RGBA')
image_hom_f = Image.open(f"{path}\Recursos\Imagenes\Hombres-Filtered.png").convert('RGBA')
image_muj = Image.open(f"{path}\Recursos\Imagenes\Mujeres.png").convert('RGBA')
image_muj_f = Image.open(f"{path}\Recursos\Imagenes\Mujeres-Filtered.png").convert('RGBA')
image_vac = Image.open(f"{path}\Recursos\Imagenes\Vacante.png").convert('RGBA')
image_nc = Image.open(f"{path}\Recursos\Imagenes\Confidencial.png").convert('RGBA')
image_nc_f = Image.open(f"{path}\Recursos\Imagenes\Confidencial-Filtered.png").convert('RGBA')
Hombres = ImageTk.PhotoImage(image_hom)
Hombres_Filtered = ImageTk.PhotoImage(image_hom_f)
Mujeres = ImageTk.PhotoImage(image_muj)
Mujeres_Filtered = ImageTk.PhotoImage(image_muj_f)
Vacante =ImageTk.PhotoImage(image_vac)
Confidencial =ImageTk.PhotoImage(image_nc)
Confidencial_Filtered =ImageTk.PhotoImage(image_nc_f)

# Menu listado nombres
## Estructura de Nombres
contenedor_estruc_nom = LabelFrame(listado_nombres,bg = 'whitesmoke',bd = 0)

indicador_despl_estruc = False

image5 = Image.open(f"{path}\Recursos\Imagenes\Imagen5.png").convert('RGBA')
image6 = Image.open(f"{path}\Recursos\Imagenes\Imagen6.png").convert('RGBA')
boton_5 = ImageTk.PhotoImage(image5)
boton_6 = ImageTk.PhotoImage(image6)

boton = Button(contenedor_estruc_nom,image = boton_5)
boton.config(bg = 'whitesmoke',bd = 0)

boton2 = Button(contenedor_estruc_nom,image = boton_6)
boton2.config(bg = 'whitesmoke',bd = 0)

estructura_nombres = Canvas(contenedor_estruc_nom)
estructura_nombres.config(bg = 'whitesmoke', bd = 0, height = ventana.winfo_height()/2)
estructura_nombres.pack_propagate(False)

subventana_nombres = LabelFrame(estructura_nombres)
subventana_nombres.config(bg = 'whitesmoke', bd = 0, height = 500)

def scrollwheel_estructura_nombres(event):
    if event.delta != 0:
        y_steps = int(-np.sign(event.delta)*1)
        estructura_nombres.yview_scroll(y_steps, "units")

sub_Verti = Scrollbar(estructura_nombres)
sub_Verti.config(bd = 0,command=estructura_nombres.yview)
estructura_nombres.config(yscrollcommand=sub_Verti.set)
estructura_nombres.bind("<MouseWheel>",scrollwheel_estructura_nombres)

## Ver
contenedor_ver = LabelFrame(listado_nombres,bg = 'whitesmoke', bd = 0)

image7 = Image.open(f"{path}\Recursos\Imagenes\Imagen7.png").convert('RGBA')
image8 = Image.open(f"{path}\Recursos\Imagenes\Imagen8.png").convert('RGBA')
boton7 = ImageTk.PhotoImage(image7)
boton8 = ImageTk.PhotoImage(image8)

boton3 = Button(contenedor_ver,image = boton7)
boton3.config(bg = 'whitesmoke',bd = 0)

boton4 = Button(contenedor_ver,image = boton8)
boton4.config(bg = 'whitesmoke',bd = 0)

ver = LabelFrame(contenedor_ver)
ver.config(bg = 'whitesmoke', bd = 0)

try:
    import pyi_splash
    pyi_splash.update_text('Cargado Correctamente')
    pyi_splash.close()
except:
    pass

'''
Función que capta los cambios en el radiobutton y actualiza los colores.
- Si el filtro nuevo es igual al anterior, no se hace nada
'''
def cambio_color():
    if radios_var.get() == legends.filtro:
        return
    
    legends.filtro = radios_var.get()
    legends.actualizar()
    [legends.colorear(i) for i in lista_cuadros]


            
radios_var = IntVar()

'''
0: Default
1: salario
2: Costo
3: Prob Renuncia
4: modalidad_trabajo
5: EVD
'''
radio_salario = Radiobutton(ver, text = ' Salario', variable = radios_var, value = 1, command=cambio_color)
radio_salario.config(bg='whitesmoke', bd = 0,activebackground = 'whitesmoke' )

#radio_costo= Radiobutton(ver, text = ' Costo', variable = radios_var, value = 2, command=cambio_color)
#radio_costo.config(bg='whitesmoke', bd = 0,activebackground = 'whitesmoke' )

radio_prob_renuncia= Radiobutton(ver, text = ' Probabilidad de renuncia', variable = radios_var, value = 3, command=cambio_color)
radio_prob_renuncia.config(bg='whitesmoke', bd = 0,activebackground = 'whitesmoke' )

radio_mod_trabajo= Radiobutton(ver, text = ' Modalidad de trabajo', variable = radios_var, value = 4, command=cambio_color)
radio_mod_trabajo.config(bg='whitesmoke', bd = 0,activebackground = 'whitesmoke' )

radio_EVD= Radiobutton(ver, text = ' EVD', variable = radios_var, value = 5, command=cambio_color)
radio_EVD.config(bg='whitesmoke', bd = 0,activebackground = 'whitesmoke' )

radio_subordinados= Radiobutton(ver, text = ' Reportes Directos', variable = radios_var, value = 6, command=cambio_color)
radio_subordinados.config(bg='whitesmoke', bd = 0,activebackground = 'whitesmoke' )

radio_todo= Radiobutton(ver, text = ' Sin formato', variable = radios_var, value = 0, command=cambio_color)
radio_todo.config(bg='whitesmoke', bd = 0,activebackground = 'whitesmoke' )


#radios = [ver, radio_salario, radio_costo, radio_prob_renuncia, radio_mod_trabajo, radio_EVD, radio_subordinados,radio_todo]
radios = [ver, radio_salario, radio_prob_renuncia, radio_mod_trabajo, radio_EVD, radio_subordinados,radio_todo]

## Filtrar
contenedor_filtrar = LabelFrame(listado_nombres,bg = 'whitesmoke', bd = 0)

image9 = Image.open(f"{path}\Recursos\Imagenes\Imagen9.png").convert('RGBA')
image10 = Image.open(f"{path}\Recursos\Imagenes\Imagen10.png").convert('RGBA')
boton9 = ImageTk.PhotoImage(image9)
boton10 = ImageTk.PhotoImage(image10)

boton5 = Button(contenedor_filtrar,image = boton9)
boton5.config(bg = 'whitesmoke',bd = 0)

boton6 = Button(contenedor_filtrar,image = boton10)
boton6.config(bg = 'whitesmoke',bd = 0)

filtrar = LabelFrame(contenedor_filtrar)
filtrar.config(bg = 'whitesmoke', bd = 0)

#### Filtros ###
'''
Filtros
Esta es una plantilla, la idea es que por cada filtro nuevo, se use esta misma
plantilla
'''
class filtro_template(LabelFrame):
    def __init__(self, imagen_mostrar, imagen_oculto, get_val, nombre_columna=""):
        self.showimg = imagen_mostrar
        self.hideimg = imagen_oculto

        self.oculto = True

        # Funcion que recibe un cuadro creador() y retorna el dato con el que
        # se filtra
        self.get_val = get_val

        # diccionario de valores con los que se filtra, son valores unicos
        # la llave es el string a filtrar y el valor es una variable booleana
        # que se relacina con el listbox
        self.filter_values = dict()
        #selected_cargos = []

        # Lista de valores que no están seleccinados en los checkbox
        self.diselected_filter = []

        self.nombre_columna = nombre_columna

        LabelFrame.__init__(self, filtrar, bg = 'whitesmoke', bd = 0)
        self.pack(side = TOP, anchor = 'nw')

        self.boton_ocultar_mostrar = Button(self, bg = 'whitesmoke',font = ('calibri',12,'bold'), fg = 'dimgray',
                               height = 20, width = 195, bd = 0,
                               image = self.showimg, command = self.ocultar_mostrar_template)
        self.boton_ocultar_mostrar.pack(side = TOP, anchor = 'nw')
        #Button(self, width=55, height = 20, bd=0, image = self.showimg).pack(side=RIGHT,anchor="nw")

        self.contenedor = Canvas(self)
        self.contenedor.config(bg = 'whitesmoke', bd = 0, width = 250, height =150)
        self.contenedor.pack_propagate(False)

        self.subventana = LabelFrame(self.contenedor)
        self.subventana.config(bg = 'whitesmoke', bd = 0)
        self.Scroll_Vertical = Scrollbar(self.contenedor)

    def ocultar_mostrar_template(self):

        if self.oculto == True:

            self.oculto = False
            self.boton_ocultar_mostrar.config(image = self.hideimg)

            self.update()

        else:

            for elim in self.subventana.winfo_children():
                elim.destroy()

            self.oculto = True
            self.boton_ocultar_mostrar.config(image = self.showimg)

            self.contenedor.pack_forget()
            self.subventana.pack_forget()

    def limpiar(self):
        for i in list(self.filter_values.keys()):
            self.filter_values[i].set(0)
        self.diselected_filter = []

    def cambio_filtro(self):
        # Si no hay ningun cuadro, o solo esta el primero, no hace nada (no hay nada que filtrar)
        if len(lista_cuadros) < 2:
            return
        # print(posiciones)
        # print([(i.cod_pos,self.get_val(i)) for i in lista_cuadros if i.cod_pos in posiciones])
        #global selected_cargos
        #global diselected_filter
        #selected_cargos = [lista_cargos[i] for i in range(len(lista_cargos)) if not cargos_vars[i].get()]
        self.diselected_filter = [i for i in list(self.filter_values.keys()) if self.filter_values[i].get()]
        #print(f"Selected: {selected_cargos}")
        # print(f"Filter: {self.nombre_columna}, Diselected: {self.diselected_filter}")
        #print([i.get() for i in self.filter_vars])

        # print(posiciones)

        pos_aux = posiciones.copy()
        disel_filter = [j.diselected_filter.copy() for j in total_filtros]
        fil_val = [j.filter_values.copy() for j in total_filtros]
        limpiar()
        for idx,j in enumerate(total_filtros):
            j.diselected_filter = disel_filter[idx]
            j.filter_values = fil_val[idx]
        lista_cuadros.append(creador(pos_aux[0]))

        for cod in pos_aux:
            cuad = next(i for i,v in enumerate(lista_cuadros) if (v.cod_pos == cod))
            #print(ind_cuad)
            lista_cuadros[cuad].desplegar(None)
        # lista_cuadros.append(creador(pos_aux[0]))
        # for i in lista_cuadros:
        #     i.dark_filter = True
        #     i.change_filtered()

    def scrollwheel_wid(self, event):
        if event.delta != 0:
            # Si la barra está en (0,1) está desactivada,
            # entonces no debe haber Scroll
            if self.Scroll_Vertical.get() != (0,1):
                y_steps = int(-np.sign(event.delta)*1)
                self.contenedor.yview_scroll(y_steps, "units")
    def update(self):
        if self.oculto:
            return
        self.contenedor.destroy()
        self.contenedor = Canvas(self)
        self.contenedor.config(bg = 'whitesmoke', bd = 0, width = 250, height =150)
        self.contenedor.pack_propagate(False)
        self.subventana = LabelFrame(self.contenedor)
        self.subventana.config(bg = 'whitesmoke', bd = 0)

        self.nn = set(self.filter_values.keys())
        for cod_po in posiciones:
            cargos_unicos = set({planta[planta['Cod_Posicion']==cod_po][self.nombre_columna].values[0]})
            cargos_unicos = cargos_unicos.union(set([planta[planta['Cod_Posicion']==cc][self.nombre_columna].values[0] for cc in planta[planta['Cod Posic Jefe']==cod_po]['Cod_Posicion'].values]))
            self.nn = self.nn.union(cargos_unicos)

        lista_anterior = list(self.filter_values.keys())
        self.filter_values = {i:(IntVar() if i not in lista_anterior else self.filter_values[i]) for i in self.nn}

        cargos_prohibidos = [self.get_val(i) for i in lista_cuadros if i.cod_pos in posiciones]
        for cargo in sorted(list(self.filter_values.keys())):

            cargos_check = Checkbutton(self.subventana,
                                      text = cargo,
                                      bg='whitesmoke',
                                      variable = self.filter_values[cargo],
                                      onvalue=0,
                                      offvalue=1,
                                      command=self.cambio_filtro)

            if cargo in cargos_prohibidos:
                cargos_check.config(state=DISABLED)

            cargos_check.pack(side = TOP, anchor = 'w')
            cargos_check.bind("<MouseWheel>",self.scrollwheel_wid)

        self.contenedor.bind("<MouseWheel>",self.scrollwheel_wid)
        self.subventana.bind("<MouseWheel>",self.scrollwheel_wid)
        self.Scroll_Vertical = Scrollbar(self.contenedor)
        self.Scroll_Vertical.config(bd = 0,command=self.contenedor.yview)
        self.contenedor.config(yscrollcommand=self.Scroll_Vertical.set)
        self.subventana.pack(side = TOP, anchor = 'nw')
        self.contenedor.pack(side = TOP,anchor = 'nw',fill = X)
        self.subventana.pack(side = TOP)
        self.Scroll_Vertical.pack(side = RIGHT, fill = Y)
        self.contenedor.create_window((0,0), window = self.subventana,anchor = 'nw')
        self.contenedor.bind("<Configure>",lambda x:self.contenedor.config(scrollregion = self.contenedor.bbox('all')))


'''
########################### Boton limpio de filtros ###########################
'''
def remove_filters():
    for filtro in total_filtros:
        filtro.limpiar()
    if len(total_filtros) > 0:
        total_filtros[0].cambio_filtro()

imagen_remfilter = Image.open(f"{path}\Recursos\Imagenes\limpiar_filtro.png").convert('RGBA')
imagen_remove_filter = ImageTk.PhotoImage(imagen_remfilter)

RR = Button(filtrar, bg = 'whitesmoke',font = ('calibri',12,'bold'),
            fg = 'dimgray', height = 20, width = 195, bd = 0,
            image=imagen_remove_filter, command=remove_filters)
RR.pack(side=TOP, anchor="nw")

'''
############################## Filtrar por Cargos ##############################
'''
imagen_cargos2_i = Image.open(f"{path}\Recursos\Imagenes\cargos2.png").convert('RGBA')
imagen_cargos2 = ImageTk.PhotoImage(imagen_cargos2_i)

imagen_cargos_i = Image.open(f"{path}\Recursos\Imagenes\cargos.png").convert('RGBA')
imagen_cargos = ImageTk.PhotoImage(imagen_cargos_i)
filtro_cargos = filtro_template(imagen_mostrar=imagen_cargos, imagen_oculto=imagen_cargos2, get_val=lambda i: i.cargo, nombre_columna="Desc Cargo")


''' Empresa
############################## Filtrar por Empresa ##############################
'''
imagen_filtros2_2 = Image.open(f"{path}\Recursos\Imagenes\empresa2.png").convert('RGBA')
imagen_empresa2 = ImageTk.PhotoImage(imagen_filtros2_2)

imagen_filtros2 = Image.open(f"{path}\Recursos\Imagenes\empresa.png").convert('RGBA')
imagen_empresa = ImageTk.PhotoImage(imagen_filtros2)
filtro_empresa = filtro_template(imagen_mostrar=imagen_empresa, imagen_oculto=imagen_empresa2, get_val=lambda i: i.empresa, nombre_columna="Empresa")


''' Tipo contrato
############################## Filtrar por Tipo de contrato ##############################
'''
imagen_contrato2_2 = Image.open(f"{path}\Recursos\Imagenes\contrato2.png").convert('RGBA')
imagen_contrato2 = ImageTk.PhotoImage(imagen_contrato2_2)

imagen_contrato3 = Image.open(f"{path}\Recursos\Imagenes\contrato.png").convert('RGBA')
imagen_contrato = ImageTk.PhotoImage(imagen_contrato3)
filtro_contrato = filtro_template(imagen_mostrar=imagen_contrato, imagen_oculto=imagen_contrato2, get_val=lambda i: i.contrato, nombre_columna="Tipo Contrato")


''' Categoría
############################## Filtrar por categoría ##############################
'''
imagen_categoria2_2 = Image.open(f"{path}\Recursos\Imagenes\categoria2.png").convert('RGBA')
imagen_categoria2 = ImageTk.PhotoImage(imagen_categoria2_2)

imagen_categoria3 = Image.open(f"{path}\Recursos\Imagenes\categoria.png").convert('RGBA')
imagen_categoria = ImageTk.PhotoImage(imagen_categoria3)
filtro_categoria = filtro_template(imagen_mostrar=imagen_categoria, imagen_oculto=imagen_categoria2, get_val=lambda i: i.categ, nombre_columna="Cat Salarial")

''' Area
############################## Filtrar por área ##############################
'''
imagen_area2_2 = Image.open(f"{path}\Recursos\Imagenes\\area2.png").convert('RGBA')
imagen_area2 = ImageTk.PhotoImage(imagen_area2_2)

imagen_area3 = Image.open(f"{path}\Recursos\Imagenes\\area.png").convert('RGBA')
imagen_area = ImageTk.PhotoImage(imagen_area3)
filtro_area = filtro_template(imagen_mostrar=imagen_area, imagen_oculto=imagen_area2, get_val=lambda i: i.area, nombre_columna="Área / Oficina")


total_filtros = [filtro_cargos, filtro_empresa, filtro_contrato, filtro_categoria, filtro_area]

def mostrar_filtrar():
    boton6.pack(side = TOP, anchor = 'nw')
    boton5.pack_forget()
    filtrar.pack(side = TOP, anchor = 'nw')
    ocultar_ver()
    ocultar_estruc()

def ocultar_filtrar():
    boton6.pack_forget()
    boton5.pack(side = TOP, anchor = 'nw')
    filtrar.pack_forget()

boton5.config(command = mostrar_filtrar)
boton6.config(command = ocultar_filtrar)


def mostrar_ver():
    boton4.pack(side = TOP, anchor = 'nw')
    boton3.pack_forget()
    ocultar_filtrar()
    ocultar_estruc()

    for i in radios:
        i.pack(side = TOP, anchor = 'w')
    legends.pack(side=TOP,anchor="nw")

def ocultar_ver():
    boton3.pack(side = TOP, anchor = 'nw')
    boton4.pack_forget()

    for i in radios:
        i.pack_forget()
    legends.pack_forget()
boton3.config(command = mostrar_ver)
boton4.config(command = ocultar_ver)

def menu_mostrar():
    contenedor_estruc_nom.pack(side=TOP,anchor = 'nw',fill = X)
    boton.pack(side = TOP, anchor = 'nw')

    contenedor_ver.pack(side=TOP,anchor = 'nw',fill = X)
    boton3.pack(side = TOP, anchor = 'nw')

    contenedor_filtrar.pack(side=TOP,anchor = 'nw',fill = X)
    boton5.pack(side = TOP, anchor = 'nw')

def mostrar_estruc():
    if len(posiciones) > 0:
        boton2.pack(side = TOP, anchor = 'nw')

        estructura_nombres.pack(side=TOP,anchor = 'nw',fill = X)

        subventana_nombres.pack(side = TOP)

        sub_Verti.pack(side = RIGHT, fill = Y)

        indicador_despl_estruc = True
        
        estructura_nombres.create_window((0,0), window = subventana_nombres,anchor = 'nw')
        estructura_nombres.bind("<Configure>",lambda x:estructura_nombres.config(scrollregion = estructura_nombres.bbox('all')))

        boton.pack_forget()

    ocultar_ver()
    ocultar_filtrar()


def ocultar_estruc():
    boton.pack(side = TOP, anchor = 'nw')

    estructura_nombres.pack_forget()
    boton2.pack_forget()
    subventana_nombres.pack_forget()
    sub_Verti.pack_forget()
    
    indicador_despl_estruc = False
    
    

boton.config(command = mostrar_estruc)
boton2.config(command = ocultar_estruc)

class actualizar_span():

    def __init__(self,expand = True):

        self.lista_poligono = []
        self.span_graf = [[],[]]
        self.lista_puntos = []

        if expand:

            self.contenedor_general_span = LabelFrame(contenedor_span_ventana, bg = '#40423E', bd = 0, width = 249, height = 500)
            self.contenedor_general_span.pack_propagate(False)
            self.contenedor_general_span.pack(side=TOP)

            self.boton_bajo = Button(contenedor_span_ventana, width = 247, height = 27, bg = fondo, bd = 0, image = span_imagen3)
            self.boton_bajo.pack_propagate(False)
            self.boton_bajo.pack(side = TOP)

            self.graficar = Canvas(self.contenedor_general_span)
            self.graficar.config(width =240, height = 480,bg = '#40423E', bd = 0)
            self.graficar.pack(side = TOP)
            self.graficar.pack_propagate(False)

            self.capas = Label(self.graficar, text = f'Capas: {len(posiciones): .0f}')
            self.capas.config(font = ('calibri', 12,'italic'),bg = '#40423E', bd = 0, fg = fondo)
            self.capas.pack(side = BOTTOM, fill = X)

            self.titulo = Label(self.graficar, text = 'Span of control', fg = fondo, bg = '#40423E', font = ('calibri', 12,'italic'))
            self.titulo.pack(side = TOP, fill = X)

            self.iz = Label(self.graficar, bd = 0, bg = '#40423E', width = 1)
            self.iz.pack(side = LEFT, fill = Y)

            self.der = Label(self.graficar, bd = 0, bg = '#40423E', width = 1)
            self.der.pack(side = RIGHT, fill = Y)


            for elim2 in self.lista_poligono:
                self.graficar.delete(elim2)
                
            
            # actualizar variables
            for lider in posiciones:
                self.span_graf[0].append(lider)
                cont = 0
                
                for cant in lista_cuadros:
                    if cant.pos_jefe == lider:
                        cont += 1
                    
                self.span_graf[1].append(cont)



            self.ratio = 480/(len(self.span_graf[0])+1)
            self.x_in, self.y_in = 120, self.ratio*(0.5)

            self.posiciones_sup = []
            self.posiciones_inf = []

            self.posiciones_sup.append(self.x_in)
            self.posiciones_sup.append(self.y_in)

            self.posiciones_inf.append(self.y_in)
            self.posiciones_inf.append(self.x_in)

            for n in range(len(self.span_graf[0])):
                # points
                self.x1, self.y1 = (120),(self.ratio*(n+ 0.5))
                self.x2, self.y2 = (self.ratio*(n+ 0.5))+4, ((120)+ 4)

                # lines
                self.lx1, self.ly1 = (self.y1+(self.ratio)), (self.x1-((self.span_graf[1][n])/max(self.span_graf[1]))*110)
                self.lx2, self.ly2 = (self.y1+(self.ratio)), (self.x1+((self.span_graf[1][n])/max(self.span_graf[1]))*110)

                self.posiciones_sup.append(self.ly1)
                self.posiciones_sup.append(self.lx1)
                self.posiciones_inf.append(self.lx2)
                self.posiciones_inf.append(self.ly2)

                self.primero = True if n == 0 else False

                self.puntos(self.x1,self.y1,self.span_graf[1][n], self.primero, self.span_graf[0][n])

            self.posiciones_inf = self.posiciones_inf[::-1]
            self.posiciones_finales =  self.posiciones_sup + self.posiciones_inf

            self.lista_poligono.append(self.graficar.create_polygon(*self.posiciones_finales, fill = fondo, outline = fondo))

        else:

            for i in contenedor_span_ventana.winfo_children():
                i.destroy()



    def puntos(self,x1, y1, n, primero, cod_pos):

        punto = LabelFrame(self.graficar,text = str(n), width = 28, height = 16, bd = 0, labelanchor = 'n', font = ('calibri',10,'bold'))
        punto.place(x = x1-14, y = y1-8)

        if primero:
            punto.config(bg = '#40423E', fg = fondo)
        else:
            punto.config(bg = fondo, fg = 'dimgray')

        punto.bind("<Enter>", lambda event, pos = cod_pos: self.desplegar(event, pos))
        punto.bind("<Leave>",lambda event, pos = cod_pos: self.salida(event, pos))


    def desplegar(self,event,cod_pos):
        for i in lista_cuadros:
            if i.cod_pos == cod_pos and not i.dark_filter:
                i.barra_baja.config(bg="orange")
                i.emergente(None)

    def salida(self,event,cod_pos):
        for i in lista_cuadros:
            if i.cod_pos == cod_pos and not i.dark_filter:
                i.salida(None)
                return


oculto_span = True

def desplegar_span(mostrar = True):
    global oculto_span

    if mostrar:

        if oculto_span == False:

            actualizar_span(False)

            oculto_span = True
            boton_span.config(image = span_imagen, bd = 0, width = 35)
            contenedor_span_ventana.config(width =1, height = 1)

        else:

            actualizar_span()

            oculto_span = False
            boton_span.config(image = span_imagen2, bd = 0, width = 250)
    else:

        actualizar_span(False)

        oculto_span = True
        boton_span.config(image = span_imagen, bd = 0, width = 35)
        contenedor_span_ventana.config(width =1, height = 1)

# Imagenes
imagen_span = Image.open(f"{path}\Recursos\Imagenes\span.png").convert('RGBA')
span_imagen = ImageTk.PhotoImage(imagen_span)

imagen_span2 = Image.open(f"{path}\Recursos\Imagenes\span2.png").convert('RGBA')
span_imagen2 = ImageTk.PhotoImage(imagen_span2)

imagen_span3 = Image.open(f"{path}\Recursos\Imagenes\span_bajo.png").convert('RGBA')
span_imagen3 = ImageTk.PhotoImage(imagen_span3)

#objetos y contenedores
boton_span = Button(ventana, bg = fondo, bd = 0, image = span_imagen, command = desplegar_span)
boton_span.place(x = -2, y = 50)

contenedor_span_ventana = LabelFrame(ventana, bg = fondo, bd = 0)
contenedor_span_ventana.place(x = 0, y = 81)

# Unidad organizativa en Ventana
unidad_organizativa = Label(ventana)
unidad_organizativa.config(bg = fondo,fg = "dimgray", font=('calibri',10,'italic'))
unidad_organizativa.place(x = 0, y = 5)


def resize(event, desplazar = False):
    global ventana_size_x
    global ventana_size_y

    listado_nombres.config(height = ventana.winfo_height()-5)
    listado_nombres.place(x = ventana.winfo_width()-(listado_nombres.winfo_width()),y =-5)

    if ventana_size_x != ventana.winfo_width() or ventana_size_y != ventana.winfo_height():

        flecha.place(y = -10, x = ventana.winfo_width()-40)

        desplegar_arriba.place(x = 10, y = ventana.winfo_height()-70)

        if len(lista_cuadros)>0:
            n_tama_height = max(megacuadro.winfo_height(), ventana.winfo_height())
            n_tama_mega = max(megacuadro.winfo_width(),ventana.winfo_width())
        else:
            n_tama_height = ventana.winfo_height()
            n_tama_mega = ventana.winfo_width()

        megacuadro.config(width=n_tama_mega,height=n_tama_height)

        subcuadro.place(x = 0,y = ventana.winfo_height()-53)
        subcuadro.config(width=ventana.winfo_width(),height=50)


    ventana_size_x = ventana.winfo_width()
    ventana_size_y = ventana.winfo_height()

# resize de la ventana
ventana.bind("<Configure>", resize) # Ajustar tamaño

class cu_nombre(Label):
    
    def __init__(self,posicion,espacio):

        self.cod_pos = posicion
        self.nombre = "    "*espacio + planta[planta['Cod_Posicion']== self.cod_pos]['Nombres'].values[0] + ' - ' +  planta[planta['Cod_Posicion']== self.cod_pos]['Diminutivo cargo'].values[0]#####################################

        #self.cu = Label(subventana_nombres, text = self.nombre)
        Label.__init__(self, subventana_nombres, text = self.nombre)
        self.config(bg="whitesmoke",fg = "dimgray", font = ("calibri",9,'italic'))
        self.pack(side = TOP, anchor = "w")

        self.bind("<Enter>",self.entrada)
        self.bind("<Leave>",self.salida)
        self.bind("<ButtonPress-1>",self.presionar)
        self.bind("<MouseWheel>",scrollwheel_estructura_nombres)

    def entrada(self,event):
        self.config(fg='dimgray', font = ('calibri',10,'bold'))

        for i in lista_cuadros:
            if i.cod_pos == self.cod_pos and not i.dark_filter:
                i.emergente(None)

                if radios_var.get() != 0:
                    #i.cuadro_area.config(bg=legends.colorear(i), bd=0, fg = 'white')
                    color2_ = legends.colorear(i)
                    if color2_ != '#FFFFFF':
                        i.cuadro_area.config(bg=color2_, bd=0, fg = 'white')
                        i.descriptor_p.config(bg=color2_, bd=1, fg = 'white')
                        i.barra_baja.config(bg=color2_)
                        i.linea_color.config(bg=color2_)
                        return

    def salida(self,event):
        self.config(fg = "dimgray",font = ("calibri",9,'italic'))
        for i in lista_cuadros:
            if i.cod_pos == self.cod_pos and not i.dark_filter:
                i.salida(None)
                return

        # for i in lista_cuadros:
        #     if i.cod_pos == self.cod_pos:
        #         #i.cuadro.config(bg=fondo)
        #         legends.colorear(i)

    def presionar(self,event):
        for i in lista_cuadros:
            if i.cod_pos == self.cod_pos:
                i.desplegar(None)
                legends.colorear(i)
                #i.cuadro.config(bg=fondo)
                i.salida(None)
                return

# Nuvoooo (Csmbiar toda la clase)
class filter_legends(Canvas):
    
    def __init__(self, padre, n_colors = 3):
        Canvas.__init__(self, padre)
        self.filtro = 0
        self.n_colors = n_colors
        self.width = ventana.winfo_width()-(ventana.winfo_width()-276)
        self.config(width=self.width,height=150, bg="whitesmoke")

        self.gradiente_color = ["#FD3232","#DB5260","#DBD339","#95DB8A"]
        self.cuadro_info = None
        self.units = "U"
        self.categorico = False

        self.grads = [['#BED9DB',"#70FFF8","#57B5A1","#1A3630"], # Salario / modalidad trab [0]-[3]
                      ["#D1E0D4","#FFE487","#EB9C7E","#F53F38"], # proba renuncia
                      ["#36C783","#ACE8D1","#EB7B75","#FFFFFF"],#EVD
                      ['#FFFFFF',"#70FFF8","#57B5A1","#1A3630"]] #Reportes
        
        
        self.actual = 1

    '''
    Funcion que dado un valor, retorna el color indicado, (color presente en la paleta actual)

    - Si es categorico va recorriendo buscando la igualdad
    - Si es continuo, va recorriendo hasta que encuentra un color en el que el valo es menor en el rango indicado
    - Adicionalmente, revisa que el rango en el que se encuentra es activo, si no, retorna el color de fondo poe defecto
    '''
    def get_element_from_range(self, val):
        if self.filtro == 0:
            return fondo
        if not self.categorico:
            for i in range(len(self.valores)):
                if val <= self.valores[i]:
                    if not self.colores_activos[i]:
                        return fondo
                    return self.colores[i]
            if not self.colores_activos[-1]:
                return fondo
            return self.colores[-1]
        else:
            for i in range(len(self.valores)):
                if val == self.valores[i] and self.colores_activos[i]:
                    return self.colores[i]
            return fondo

    def dibujar_paleta(self):

        width_barra_color = 62
        height_barra_color = 20
        y_pos = 55
        x_pos = 8
        fontsize = 10

        if self.filtro == 0:
            return
        titulo = Label(self)

        if self.filtro == 1:
            textitulo = "Salario"
            self.units = "Unidades: Millones de pesos"
            vals = ['0 - 3','3 - 6','6 - 13','13+']
            posiciones = [(width_barra_color*i + x_pos, y_pos) for i in range(4)]

        elif self.filtro == 3:
            textitulo = "Prob. Renuncia"
            self.units = "Unidades: Probabilidad/Porcentaje"
            vals = ['0 - 25','25 - 50', '50 - 75', '75 - 100']
            posiciones = posiciones = [(width_barra_color*i + x_pos, y_pos) for i in range(4)]
            
        elif self.filtro == 4:
            textitulo = "Modalidad"
            self.units = ""
            vals = self.valores
            posiciones = posiciones = [(width_barra_color*i + x_pos, y_pos) for i in range(4)]
            
        elif self.filtro == 5:
            textitulo = "Eval. Desempeño"
            self.units = ""
            vals = self.valores
            posiciones = posiciones = [(width_barra_color*i + x_pos, y_pos) for i in range(4)]
            
        elif self.filtro == 6:
            textitulo = "Reportes Directos"
            self.units = "Personas"
            vals = ['0','1 - 5','5 - 10', '10+']
            posiciones = posiciones = [(width_barra_color*i + x_pos, y_pos) for i in range(4)]

        self.barras = [i for i in self.colores]
        self.colores_activos = [1 for i in self.colores]
        
        for i in range(len(self.colores)):
            
            if self.filtro == 1 or self.filtro == 6 or self.filtro == 4:
                if i == 3:
                    self.foreg = 'whitesmoke'
                else:
                    self.foreg = 'black'
                    
            elif self.filtro == 3 or self.filtro == 5:
                self.foreg = 'black'
                    
            
            self.titulo = Label(self, text = textitulo, width = 30)
            self.titulo.config(bg='whitesmoke',font=('calibri',10,'bold'),fg='black',bd =1)
            self.titulo.place(y = 15, x = int(self.width/2),anchor="center")

            self.tipo_units = Label(self, text = self.units, width = 30,anchor="w")
            self.tipo_units.config(bg='whitesmoke',font=('calibri',10,'bold'),fg='black',bd =1)

            self.barras[i] = Frame(self,width=width_barra_color,height=height_barra_color,bg=self.colores[i],relief="solid",bd=1)
            self.barras[i].pack_propagate(0) # Stops child widgets of label_frame from resizing it
            ss = Label(self.barras[i], bg=self.colores[i], fg=self.foreg, text=vals[i], font=('calibri',fontsize,'bold'))
            ss.pack()

            self.barras[i].bind("<Button-1>", lambda x, i=i: self.barraclick(posiciones[i], vals[i], i))
            ss.bind("<Button-1>", lambda x, i=i: self.barraclick(posiciones[i], vals[i], i))
            # self.barras[i].bind("<Leave>", lambda x, i=i: self.salida(i))

            if self.units != "":
                self.tipo_units.place(y = 35, x = 5)
                self.barras[i].place(y = posiciones[i][1], x = posiciones[i][0])
            else:
                self.barras[i].place(y = posiciones[i][1]-20, x = posiciones[i][0])

        titulo.config(font =('calibri',10), width = 50, height = 1, bg = "whitesmoke", bd =0, text = textitulo, fg = 'black')

        self.config(height=posiciones[-1][1]+40)

    def barraclick(self, pos, texto, barra_i):
        
        if self.barras[barra_i].cget("bd")==1:
            
            self.barras[barra_i].config(bd = 0)
            self.colores_activos[barra_i] = 0
            
        else:
            
            self.barras[barra_i].config(relief="solid", bd = 1)
            self.colores_activos[barra_i] = 1

        #cambio_color()
        [legends.colorear(i) for i in lista_cuadros]

    '''
    Funcion que actualiza la paleta de colores, los intervalos, gradientes ,y demas
    '''
    def actualizar(self):
        for i in self.winfo_children():
           i.destroy()
        if self.filtro == 0:
            return
        elif self.filtro == 1:
            self.categorico = False
            self.valores = [3000000.0,6000000.0,13000000.0,90000000.0]
            self.colores = self.grads[0]

        elif self.filtro == 3:
            self.categorico = False
            self.valores = [0.25, 0.50, 0.75, 0.1]
            self.colores = self.grads[1]

        elif self.filtro == 4:
            self.categorico = True
            self.valores = ["Presencial", "En casa", "Hibrido", "Vte"]
            self.colores = self.grads[0]
            
        elif self.filtro == 5:
            self.categorico = True
            self.valores = ["Alto", "Medio", "Bajo", "Sin EVD"]
            self.colores = self.grads[2]
            
        elif self.filtro == 6:
            self.categorico = False
            self.valores = [0,5,10,500]
            self.colores = self.grads[3]


        self.dibujar_paleta()
        self.pack(side=TOP,anchor="nw")

    '''
    Función que recibe un cuadro y lo colorea.
    El color dpende del tipo de filtro que se tenga actualmente y la información del cuadro.
    '''
    def colorear(self, cuadro_a_colorear):
        if self.filtro == 0 or cuadro_a_colorear.dark_filter:
            color_ = fondo
        elif self.filtro == 1:
            color_ = self.get_element_from_range(cuadro_a_colorear.salario)
        elif self.filtro == 2:
            color_ = self.get_element_from_range(cuadro_a_colorear.costo)
        elif self.filtro == 3:
            if cuadro_a_colorear.prob_renuncia >=0:
                color_ = self.get_element_from_range(cuadro_a_colorear.prob_renuncia)
            else:
                color_ = '#FFFFFF'
        elif self.filtro == 4:
            color_ = self.get_element_from_range(cuadro_a_colorear.modalidad_t)
        elif self.filtro == 5:
            color_ = self.get_element_from_range(cuadro_a_colorear.calif_evd)
        elif self.filtro == 6:
            color_ = self.get_element_from_range(len(cuadro_a_colorear.subordinados))
        else:
            color_= fondo
        cuadro_a_colorear.barra_baja.config(bg=color_ )

        return color_


class barra_lateral():

    def __init__(self,event, expandir = True):

        global lista_personas

        if listado_nombres.winfo_width() > 21:

            if expandir:
                listado_nombres.config(width = 20, bg = 'whitesmoke',bd =0)

                flecha.config(image = button2)
                flecha.place(x = ventana.winfo_width()-40, y = -10)

                # Limpiar nombres
                lista_personas.clear()

                # Limpiar barra
                for i in listado_nombres.winfo_children():
                    i.pack_forget()

                # Limpiar nombres
                for i2 in subventana_nombres.winfo_children():
                    i2.destroy()

            else:

                if len(posiciones) > 0:

                    # Limpiar nombres
                    lista_personas.clear()

                    # Limpiar nombres
                    #mostrar_estruc
                    for i2 in subventana_nombres.winfo_children():
                        i2.destroy()


                    # Agregar nombres
                    for n_pos in range(len(posiciones)):
                        # Dubujar Padre
                        lista_personas.append(cu_nombre(posiciones[n_pos],n_pos+1))

                    #Dibujar hijos
                    subordinados = planta[planta['Cod Posic Jefe']==posiciones[-1]]['Cod_Posicion'].values

                    for i in range(len(subordinados)):
                        lista_personas.append(cu_nombre(subordinados[i],len(posiciones)+1))
                        c = i 

                else:

                    # Limpiar nombres
                    lista_personas.clear()

        else:

            if expandir:
                listado_nombres.config(width = ventana.winfo_width()-(ventana.winfo_width()-276), bg = "whitesmoke",bd = 0,relief=FLAT)

                flecha.config(image = button)
                flecha.place(x = ventana.winfo_width()-296, y = -10)

                # Mostrar menu
                ocultar_ver()
                ocultar_filtrar()
                ocultar_estruc()
                menu_mostrar()

                #lambda:(mostrar_estruc(),ocultar_estruc())

                if len(posiciones) > 0:
                    # agregar nombres
                    for n_pos in range(len(posiciones)):

                        # Dubujar Padre
                        lista_personas.append(cu_nombre(posiciones[n_pos],n_pos+1))


                    #Dibujar hijos
                    subordinados = planta[planta['Cod Posic Jefe']==posiciones[-1]]['Cod_Posicion'].values

                    for i in range(len(subordinados)):
                        lista_personas.append(cu_nombre(subordinados[i],len(posiciones)+1))
                        c = i 


# llamada de funciones listado_desplegar
flecha.bind("<ButtonPress-1>",barra_lateral)
listado_nombres.bind("<ButtonPress-1>",barra_lateral)

def barra_inferior(event):
    if subcuadro.winfo_height() > 51:
        subcuadro.config(height = 50)
        subcuadro.place(x = 0,y = ventana.winfo_height()-50)

        desplegar_arriba.place(x = 10, y = ventana.winfo_height()-69)
        desplegar_arriba.config(image = button3)

        if len(lista_cuadros)>0:
            subcuadro_simple()

    else:
        subcuadro.config(height = 150)
        subcuadro.place(x = 0,y = ventana.winfo_height()-120)

        desplegar_arriba.place(x = 10, y = ventana.winfo_height()-140)
        desplegar_arriba.config(image = button4)

        if len(lista_cuadros)>0:
            subcuadro_simple(False)


subcuadro.bind("<ButtonPress-1>",barra_inferior)
desplegar_arriba.bind("<ButtonPress-1>",barra_inferior)

class creador(Button):
    
    def __init__(self,cod_pos, X_pos=0, Y_pos =0):

        # Datos del nodo
        self.cod_pos = cod_pos
        self.X_pos = X_pos
        self.Y_pos = Y_pos

        # variables
        self.cod_pos = cod_pos
        self.persona = planta[planta['Cod_Posicion']==cod_pos]
        self.area = self.persona['Área / Oficina'].values[0]
        self.nombre = self.persona['Nombres'].values[0]
        self.cargo = self.persona['Desc Cargo'].values[0]
        self.sexo = self.persona['Genero'].values[0]
        self.edad = self.persona['Edad'].values[0]
        self.antig = self.persona['Antiguedad'].values[0]
        self.categ = self.persona['Cat Salarial'].values[0]
        self.salario = self.persona['Salario'].values[0]
        self.costo = self.persona['Costo Total'].values[0]
        self.EVD = self.persona['EVD'].values[0]
        self.pasivo = self.persona['Pasivo Vacaciones'].values[0]
        self.empresa = self.persona['Empresa'].values[0]
        self.contrato = self.persona['Tipo Contrato'].values[0]
        self.sst = self.persona['Reporte de SST'].values[0]
        self.disciplinarios = self.persona['Procesos disciplinarios'].values[0]
        self.pension = self.persona['Tiempo para pens'].values[0]
        self.d_vacaciones = self.persona['Pasivo Vacaciones'].values[0]
        self.cargo_diminutivo = self.persona['Diminutivo cargo'].values[0]
        self.calif_evd =  self.persona['Calificacion EVD'].values[0]
        self.pos_jefe = self.persona['Cod Posic Jefe'].values[0]
        self.prob_renuncia = self.persona['Prob renuncia'].values[0]
        self.cedula = self.persona['Cedula'].values[0]
        self.dark_filter = False
        self.modalidad_t = self.persona['Trabajo en casa / Presencial'].values[0]
        
        # definición de subordinados
        self.subordinados = planta[planta['Cod Posic Jefe']==self.cod_pos]['Cod_Posicion'].values
        self.reportes_directos = len(self.subordinados)

        # Posiciones iniciales
        if X_pos == 0 and Y_pos == 0:
            self.X_pos = (ventana.winfo_width()/2)-25
            self.Y_pos = 40

        self.indicador_p = Label(megacuadro)
        self.indicador_p.config(font =('calibri',10), width = 1, height = 1, bg = fondo, bd =0, text = '*', fg = 'orangered')

        if self.pension != 'No aplica' and self.sst == 'Sin reporte de SST' and self.disciplinarios == 'Sin proceso':
                self.indicador_p.config(fg = 'blue')

        if self.sst != 'Sin reporte de SST' or self.disciplinarios != 'Sin proceso' or self.pension != 'No aplica':
            self.indicador_p.place(y = self.Y_pos -2,x =self.X_pos -7)
                
        # Barra que se colorea
        self.barra_baja = LabelFrame(megacuadro)
        self.barra_baja.config(width = 27, height = 6, bd = 0, bg = fondo)
        self.barra_baja.place(y = self.Y_pos -18, x = self.X_pos)

        # Diminutivo de cargo
        self.cargo_dim = Label(megacuadro)
        self.cargo_dim.config(width = 7, bd = 0, bg = fondo, text = self.cargo_diminutivo, font = ('calibri',10,'italic'), fg = 'dimgray', anchor = CENTER)
        self.cargo_dim.place(y = self.Y_pos -14, x = self.X_pos-12)

        # Cuadro
        Button.__init__(self, megacuadro,width = 25,height=25, bg = fondo, bd =0, relief = 'solid')
        self.place(y = self.Y_pos, x = self.X_pos)
        self.change_filtered()

        self.indicador_desp = False

        #llamada de funciones
        self.bind("<Enter>",self.entrada)
        self.bind("<Leave>",self.salida)
        self.bind("<ButtonPress-1>",self.desplegar)
        self.bind("<MouseWheel>",mover_rueda)
        self.bind('<Shift-MouseWheel>',lambda event: mover_rueda(event,'h'))

    '''
    Aquí se decide si la imagen es filtrada o normal
    '''
    def change_filtered(self):

        self.dark_filter = False
        for filtro in total_filtros:
            if filtro.get_val(self) in filtro.diselected_filter:
                self.dark_filter = True
                break

        if not self.dark_filter:
            if self.sexo == 'Mujer':
                self.imagen_sexo = Mujeres
            elif self.sexo == 'Hombre':
                self.imagen_sexo = Hombres
            elif self.sexo == 'Vte':
                self.imagen_sexo = Vacante
            elif self.sexo == 'Nc':
                self.imagen_sexo = Confidencial
            else:
                self.imagen_sexo = Vacante
        else:
            if self.sexo == 'Mujer':
                self.imagen_sexo = Mujeres_Filtered
            elif self.sexo == 'Hombre':
                self.imagen_sexo = Hombres_Filtered
            elif self.sexo == 'Vte':
                self.imagen_sexo = Vacante_Filtered
            elif self.sexo == 'Nc':
                self.imagen_sexo = Confidencial_Filtered
            else:
                self.imagen_sexo = Vacante_Filtered

        legends.colorear(self)
        self.config(image = self.imagen_sexo)

    def destroy(self):
        Button.destroy(self)
        self.barra_baja.destroy()
        self.indicador_p.destroy()
        self.cargo_dim.destroy()

    # cuadro emergente
    def emergente(self,posicion,pos_mouse = None):
        if self.dark_filter:
            return

        # linea_color
        self.linea_color = Label(megacuadro,width=38,height=1)
        self.linea_color.config(bg= 'gainsboro', bd=0)
        self.linea_color.pack_propagate(False)
        #legends.colorear(self)

        # cuadros
        # Cuadro área
        self.cuadro_area = Label(megacuadro, text = self.area, width = 38)
        self.cuadro_area.config(bg='gainsboro',font=('calibri',10,'bold'),fg='dimgray',bd =0)

        # Contenedor de datos personales
        self.cuadro_gen = LabelFrame(megacuadro,width=240,height=180)
        self.cuadro_gen.config(bg=fondo, bd =0)
        self.cuadro_gen.pack_propagate(False)

        if pos_mouse is None:
            posaux = self.X_pos
        else:
            posaux= pos_mouse

        if posaux > ventana.winfo_width()-250:
            self.cuadro_gen.place(y = self.Y_pos-6, x = self.X_pos - 240)
            self.cuadro_area.place(y = self.Y_pos-25, x = self.X_pos - 240)
            self.linea_color.place(y = self.Y_pos-17, x = self.X_pos - 240)
            
        else:
            self.cuadro_gen.place(y = self.Y_pos-6, x = self.X_pos +30)
            self.cuadro_area.place(y = self.Y_pos-25, x = self.X_pos)
            self.linea_color.place(y = self.Y_pos-17, x = self.X_pos)
            

            # Datos personales
        self.cuadro_nombre = Label(self.cuadro_gen, text = self.nombre)
        self.cuadro_nombre.config(bg=fondo,font=('calibri',10,'bold'),fg="dimgray", justify = 'right')
        self.cuadro_nombre.pack(side = TOP, anchor = "w")

        self.cuadro_cargo = Label(self.cuadro_gen, text = self.cargo + ' - ' + str(self.cod_pos))
        self.cuadro_cargo.config(bg=fondo,font=('calibri',9,'bold'),fg="midnightblue",justify = 'right')
        self.cuadro_cargo.pack(side = TOP, anchor = "w")

        self.cuadro_sexo = Label(self.cuadro_gen, text = "Sexo: " + str(self.sexo))
        self.cuadro_sexo.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_sexo.place(x = 5, y = 40)

        self.cuadro_ced = Label(self.cuadro_gen, text = f"Cédula: {self.cedula: .0f}")
        self.cuadro_ced.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_ced.place(x = 115, y = 40)

        self.cuadro_categ = Label(self.cuadro_gen, text = "Categoría: " + str(self.categ))
        self.cuadro_categ.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_categ.place(x = 115, y = 60)

        self.cuadro_edad = Label(self.cuadro_gen, text = f"Edad: {self.edad: .1f} años")
        self.cuadro_edad.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_edad.place(x = 5, y = 60)

        self.cuadro_antig = Label(self.cuadro_gen, text = f"Antigüedad: {self.antig: .1f} años" )
        self.cuadro_antig.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_antig.place(x = 115, y = 80)

        self.cuadro_evd = Label(self.cuadro_gen, text = "EVD: " + str(self.EVD))
        self.cuadro_evd.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_evd.place(x = 5, y = 80)

        self.cuadro_pasivo_vac = Label(self.cuadro_gen, text = "Vacaciones: " + str(self.pasivo) + " días")
        self.cuadro_pasivo_vac.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_pasivo_vac.place(x = 115, y = 100)

        self.cuadro_salario = Label(self.cuadro_gen, text = f"Salario: ${self.salario:,}")
        self.cuadro_salario.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_salario.place(x = 5, y = 100)

        self.cuadro_costo = Label(self.cuadro_gen, text = f"Costo Total: ${self.costo:,}")
        self.cuadro_costo.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_costo.place(x = 5, y = 120)

        self.cuadro_acargo = Label(self.cuadro_gen, text = "Reportes directos: " + str(len(self.subordinados)))
        self.cuadro_acargo.config(bg=fondo,font=('calibri',8),fg="dimgray")
        self.cuadro_acargo.place(x = 5, y = 140)

        self.cuadro_prob_renuncia = Label(self.cuadro_gen, text = f"Probabilidad de renuncia: {self.prob_renuncia*100:.0f}%")
        self.cuadro_prob_renuncia.config(bg=fondo,font=('calibri',8),fg="dimgray")
        
        if self.prob_renuncia >-1:
            self.cuadro_prob_renuncia.place(x = 10, y = 160)

        self.descriptor_p = Label(megacuadro)
        self.descriptor_p.config(font =('calibri',9,'italic'), width = 44, height = 2 , bg = 'gainsboro', bd =1, fg = 'orangered')
        self.descriptor_p.pack_propagate(False)
        
        if posaux > ventana.winfo_width()-250:
            
            if self.sst != 'Sin reporte de SST' or self.disciplinarios != 'Sin proceso' or self.pension != 'No aplica':
                self.descriptor_p.place(y = self.Y_pos -40,x =self.X_pos-240)
    
                if self.sst != 'Sin reporte de SST' and self.disciplinarios != 'Sin proceso' and self.pension == 'No aplica':
                    self.descriptor_p.config(text = '*Reporte en SST \n' + '*En proceso disciplinario')
                    self.descriptor_p.place(y = self.Y_pos -55,x =self.X_pos-240)
                    
                elif self.sst != 'Sin reporte de SST' and self.disciplinarios == 'Sin proceso' and self.pension == 'No aplica':
                    self.descriptor_p.config(text = '*Reporte en SST', height = 1)
    
                elif self.sst == 'Sin reporte de SST' and self.disciplinarios != 'Sin proceso'and self.pension == 'No aplica':
                    self.descriptor_p.config(text = '*En proceso disciplinario', height = 1)
    
                elif self.sst == 'Sin reporte de SST' and self.disciplinarios == 'Sin proceso'and self.pension != 'No aplica':
                    self.descriptor_p.config(text = f'*{self.pension}', height = 1)        
                    self.descriptor_p.config(fg = 'blue')
    
                elif self.sst == 'Sin reporte de SST' and self.disciplinarios != 'Sin proceso'and self.pension != 'No aplica':
                    self.descriptor_p.config(text = f'*{self.pension} \n' + '*En proceso disciplinario')
                    self.descriptor_p.place(y = self.Y_pos -55,x =self.X_pos-240)
    
                elif self.sst != 'Sin reporte de SST' and self.disciplinarios == 'Sin proceso'and self.pension != 'No aplica':
                    self.descriptor_p.config(text = f'*{self.pension} \n' + '*Reporte en SST')
                    self.descriptor_p.place(y = self.Y_pos -55,x =self.X_pos-240)
                    
                elif self.sst != 'Sin reporte de SST' and self.disciplinarios != 'Sin proceso'and self.pension != 'No aplica':
                    self.descriptor_p.config(text = f'*{self.pension} \n' + '*Reporte en SST \n' + '*En proceso disciplinario')
                    self.descriptor_p.place(y = self.Y_pos -55,x =self.X_pos-240)
        else:
            
            if self.sst != 'Sin reporte de SST' or self.disciplinarios != 'Sin proceso' or self.pension != 'No aplica':
                self.descriptor_p.place(y = self.Y_pos -40,x =self.X_pos)
    
                if self.sst != 'Sin reporte de SST' and self.disciplinarios != 'Sin proceso' and self.pension == 'No aplica':
                    self.descriptor_p.config(text = '*Reporte en SST \n' + '*En proceso disciplinario')
                    self.descriptor_p.place(y = self.Y_pos -55,x =self.X_pos)
                    
                elif self.sst != 'Sin reporte de SST' and self.disciplinarios == 'Sin proceso' and self.pension == 'No aplica':
                    self.descriptor_p.config(text = '*Reporte en SST', height = 1)
    
                elif self.sst == 'Sin reporte de SST' and self.disciplinarios != 'Sin proceso'and self.pension == 'No aplica':
                    self.descriptor_p.config(text = '*En proceso disciplinario', height = 1)
    
                elif self.sst == 'Sin reporte de SST' and self.disciplinarios == 'Sin proceso'and self.pension != 'No aplica':
                    self.descriptor_p.config(text = f'*{self.pension}', height = 1)        
                    self.descriptor_p.config(fg = 'blue')
    
                elif self.sst == 'Sin reporte de SST' and self.disciplinarios != 'Sin proceso'and self.pension != 'No aplica':
                    self.descriptor_p.config(text = f'*{self.pension} \n' + '*En proceso disciplinario')
                    self.descriptor_p.place(y = self.Y_pos -55,x =self.X_pos)
    
                elif self.sst != 'Sin reporte de SST' and self.disciplinarios == 'Sin proceso'and self.pension != 'No aplica':
                    self.descriptor_p.config(text = f'*{self.pension} \n' + '*Reporte en SST')
                    self.descriptor_p.place(y = self.Y_pos -55,x =self.X_pos)
                    
                elif self.sst != 'Sin reporte de SST' and self.disciplinarios != 'Sin proceso'and self.pension != 'No aplica':
                    self.descriptor_p.config(text = f'*{self.pension} \n' + '*Reporte en SST \n' + '*En proceso disciplinario')
                    self.descriptor_p.place(y = self.Y_pos -55,x =self.X_pos)

                
    def desplegar(self,event):
        if self.dark_filter:
            return
        global lista_lineas
        global lista_cuadros
        global posiciones
        global pos_com
        
        if self.indicador_desp == True:

            #contraer
            # print(len(lista_cuadros), len(megacuadro.winfo_children()))
            # for cont in megacuadro.winfo_children():
            #     if cont.winfo_y() > self.Y_pos+1:
            #         cont.destroy()

            for elim_cuad in lista_cuadros:
                if elim_cuad.Y_pos > self.Y_pos+1:
                    elim_cuad.destroy()
                    lista_cuadros = [i for i in lista_cuadros if i.cod_pos!= elim_cuad.cod_pos]
                elim_cuad.indicador_desp = False

            for elim_lin in lista_lineas:
                if megacuadro.coords(elim_lin)[1] > self.Y_pos+1:
                    megacuadro.delete(elim_lin)
                    lista_lineas = [i for i in lista_lineas if i!= elim_lin]

            for n in range(len(posiciones)):
                if posiciones[n] == self.cod_pos:
                    posiciones = posiciones[:n]
                    break
            self.indicador_desp = False


        else:
            #desplegar

            # indicador de despliegue
            self.indicador_desp = True


            # limpiar formato
            # for cont in megacuadro.winfo_children():
            #     if cont.winfo_y() > self.Y_pos+1:
            #         cont.destroy()

            for elim_cuad in lista_cuadros:
                if elim_cuad.cod_pos != self.cod_pos:
                    elim_cuad.indicador_desp = False

                if elim_cuad.Y_pos > self.Y_pos+1:
                    elim_cuad.destroy()
                    lista_cuadros = [i for i in lista_cuadros if i.cod_pos!= elim_cuad.cod_pos]

            for elim_lin in lista_lineas:
                if megacuadro.coords(elim_lin)[1] > self.Y_pos+1:
                    megacuadro.delete(elim_lin)
                    lista_lineas = [i for i in lista_lineas if i!= elim_lin]

            for n in range(len(posiciones)):
                if posiciones[n] == self.cod_pos:
                    posiciones = posiciones[:n]
                    break

            def filtro_hijos(cod_po):
                persona = planta[planta['Cod_Posicion']==cod_po]
                for filtro in total_filtros:
                    if persona[filtro.nombre_columna].values[0] in filtro.diselected_filter:
                        return False
                return True

            # desplegar información
            cuadros_hijos = self.subordinados.copy()
            cuadros_hijos = list(filter(filtro_hijos, cuadros_hijos))
            n_cuadros =len(cuadros_hijos)

            if n_cuadros != 0:

                # Posiciones
                X_pos = self.X_pos
                Y_pos = (ventana.winfo_height()/4)+self.Y_pos

                y_horizontal = int((2/3)*ventana.winfo_height()/4) + self.Y_pos
                min_x = np.infty
                max_x = -np.infty

                try:
                    # Pares
                    if n_cuadros % 2 == 0:
                        pos_com = next(X_pos-(25+25)*i + 25 for i in range(int(n_cuadros/2), 0,-1) if X_pos - (25+25)*i + 25 > 0)
                        #pos_com = X_pos-(25+25)*comienzo + 25

                     # Impares
                    else:
                        pos_com = next(X_pos-(25+25)*i for i in range(int(n_cuadros/2), 0,-1) if X_pos - (25+25)*i > 0)
                        #pos_com = X_pos-(25+25)*comienzo
                        
                # Si todos se salen de la pantalla
                except:
                    pos_com = self.X_pos
                
                for i in range(n_cuadros):
                
                    lista_cuadros.append(creador(cuadros_hijos[i], i*(25 + 25) + pos_com, Y_pos))
                    # linea = megacuadro.create_line(self.X_pos+10, self.Y_pos+20, (X_pos-(30*i)-30)+10, Y_pos, fill='gray')
                    linea = megacuadro.create_line(i*(25 + 25) + pos_com + 12, y_horizontal, i*(25 + 25) + pos_com + 12, Y_pos, fill='gray')
                    lista_lineas.append(linea)

                min_x = pos_com + 12
                max_x = (n_cuadros-1)*(25 + 25) + pos_com + 12
                # Lineas Finales
                # Linea de self hacia la mitad (Vertical)
                linea = megacuadro.create_line(X_pos+12, y_horizontal, X_pos+12, self.Y_pos+20, fill='gray')
                lista_lineas.append(linea)
                # Linea de self hacia la mitad (Horizontal)
                linea = megacuadro.create_line(min_x, y_horizontal, max_x, y_horizontal, fill='gray')
                lista_lineas.append(linea)

                # Agregar a posiciones y Eliminar del mismo nivel
                jefe_pos_self = planta[planta['Cod_Posicion']==self.cod_pos]['Cod Posic Jefe'].values[0]

                for colegas in posiciones:
                    jefe_pos_colegas = planta[planta['Cod_Posicion']==colegas]['Cod Posic Jefe'].values[0]

                    if jefe_pos_colegas == jefe_pos_self:
                        posiciones.remove(colegas)

                posiciones.append(self.cod_pos)

                areas = list(map(lambda cod_pos: planta[planta['Cod_Posicion']==cod_pos]['Área / Oficina'].values[0],np.array(posiciones)))
                to_show =[areas[index] for index in sorted(np.unique(areas, return_index=True)[1])]
                to_show2 = " / ".join(to_show)
                unidad_organizativa.config(text = to_show2)

        desplegar_span(False)
        subcuadro_simple()
        barra_lateral(None,False)

        max_alto = max(max(lista_cuadros,key=lambda x: x.Y_pos).Y_pos + 250, megacuadro.winfo_height(),ventana.winfo_height())
        max_ancho = max(max(lista_cuadros,key=lambda x: x.X_pos).X_pos + 100, megacuadro.winfo_width(),ventana.winfo_width())

        megacuadro.config(width = max_ancho , height = max_alto)
        for filtro in total_filtros:
            filtro.update()

    def entrada(self,event):
        if not self.dark_filter:
            self.emergente(self.cod_pos,event.x_root - ventana.winfo_rootx() )
            if radios_var.get() != 0 and self.sexo != "Nc":
                color2_ = legends.colorear(self)
                if color2_ != '#FFFFFF':
                    self.cuadro_area.config(bg=color2_, bd=0, fg = 'white')
                    self.descriptor_p.config(bg=color2_, bd=1, fg = 'white')
                    self.barra_baja.config(bg=color2_)
                    self.linea_color.config(bg=color2_)

    def salida(self,event):
        if not self.dark_filter:
            self.cuadro_gen.destroy()
            self.cuadro_area.destroy()
            self.linea_color.destroy()
            self.descriptor_p.destroy()
def inicio():

    limpiar()
    if np.isin(user.lower(), admin):
        lista_cuadros.append(creador(1))
    else:
        lista_cuadros.append(creador(usuarios_a[usuarios_a['Usuario']==user.lower()]['Inicio por defecto'].values[0]))

        

def limpiar():

    megacuadro.place(x = 0, y = -5)

    for cont in megacuadro.winfo_children():
        cont.destroy()

    for elim_lin in lista_lineas:
        megacuadro.delete(elim_lin)


    posiciones.clear()
    lista_lineas.clear()
    lista_cuadros.clear()
    unidad_organizativa.config(text = "")

    for filtro in total_filtros:
        filtro.filter_values = dict()
        filtro.diselected_filter = []
        filtro.update()

    barra_lateral(None,False)
    subcuadro_simple(ocultar = True)

def export():
    
    if np.isin(user.lower(), admin):
        global posiciones
        if len(lista_cuadros)>0:
    
            tipo_export = Toplevel(ventana)
            tipo_export.title('Exportar información')
            tipo_export.geometry(f"350x155+{int(ventana.winfo_width()/2)-175}+{int(ventana.winfo_height()/2)-80}")
            tipo_export.iconbitmap(f"{path}/Recursos/Imagenes/Logo-Banco.ico")
            tipo_export.config(bg = fondo)
            tipo_export.resizable(False, False)
    
            # Titulo
            titulo = Label(tipo_export, text = 'Selecciona cómo deseas exportar la información')
            titulo.config(fg = 'dimgray', font = ('calibri',13,'bold', 'italic'), bg = fondo, bd = 0, height = 2)
            titulo.pack(side = TOP, fill = X)
    
            # Seleccionadores
            radios_export_var = IntVar()
    
            radio_export1 = Radiobutton(tipo_export, text = 'Exportar todos los elementos desplegados', variable = radios_export_var, value = 0)
            radio_export1.config(bg=fondo, bd = 0,activebackground = fondo)
            radio_export1.pack(side = TOP, anchor = 'w')
    
            radio_export2 = Radiobutton(tipo_export, text = 'Exportar la ruta de la última área desplegada ', variable = radios_export_var, value = 1)
            radio_export2.config(bg=fondo, bd = 0,activebackground = fondo)
            radio_export2.pack(side = TOP, anchor = 'w')
    
            radio_export3 = Radiobutton(tipo_export, text = 'Exportar sólo la última área desplegada', variable = radios_export_var, value = 2)
            radio_export3.config(bg=fondo, bd = 0,activebackground = fondo)
            radio_export3.pack(side = TOP, anchor = 'w')
    
            # boton
            boton_export = Button(tipo_export, text='Aceptar')
            boton_export.config(font = ('calibri',13,'bold', 'italic'), fg = 'dimgray', bg = fondo, bd = 1)
            boton_export.pack(side=BOTTOM,anchor = 'center')
    
            def exportar():
    
                if radios_export_var.get() == 0:
    
                    lista_personas_export = []
    
                    for i in lista_cuadros:
                        lista_personas_export.append(i.cod_pos)
    
                    planta_export = planta
                    planta_export['filtro'] = planta_export['Cod_Posicion'].isin(lista_personas_export)
                    planta_export = planta_export[planta_export['filtro']==True]
                    planta_export = planta_export.drop(['filtro'], axis = 1)
    
                    filepath = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Excel files", ".xlsx .xls")))
    
                    if filepath != '':
                        planta_export.to_excel(filepath + '.xlsx')
                        ms.showinfo(message="Datos exportados")
    
                elif radios_export_var.get() == 1:
                    if len(posiciones)>0:
                        jefe = []
                        posiciones_export = []
    
                        for i in posiciones:
                            jefe.append(i)
    
                        subordinados = planta[planta['Cod Posic Jefe']== jefe[-1]]['Cod_Posicion'].values
    
                        for x in jefe:
                            posiciones_export.append(x)
    
                        for n in subordinados:
                            posiciones_export.append(n)
    
                        planta_export = planta
                        planta_export['filtro'] = planta_export['Cod_Posicion'].isin(posiciones_export)
                        planta_export = planta_export[planta_export['filtro']==True]
                        planta_export = planta_export.drop(['filtro'], axis = 1)
    
                        filepath = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Excel files", ".xlsx .xls")))
    
                        if filepath != '':
                            planta_export.to_excel(filepath + '.xlsx')
                            ms.showinfo(message="Datos exportados")
                    else:
                        ms.showinfo(message="Es necesario que se desplieqgue al menos una persona para continuar")
    
                else:
                    jefe = []
                    posiciones_export = []
    
                    if len(posiciones) != 0:
                        jefe.append(posiciones[-1])
                    else:
                        for i in lista_cuadros:
                            jefe.append(i.cod_pos)
    
                    subordinados = planta[planta['Cod Posic Jefe']== jefe[-1]]['Cod_Posicion'].values
    
                    posiciones_export.append(jefe[-1])
    
                    for n in subordinados:
                        posiciones_export.append(n)
    
                    planta_export = planta
                    planta_export['filtro'] = planta_export['Cod_Posicion'].isin(posiciones_export)
                    planta_export = planta_export[planta_export['filtro']==True]
                    planta_export = planta_export.drop(['filtro'], axis = 1)
    
                    filepath = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Excel files", ".xlsx .xls")))
    
                    if filepath != '':
                        planta_export.to_excel(filepath + '.xlsx')
                        ms.showinfo(message="Datos exportados")
    
                tipo_export.withdraw()
    
            boton_export.config(command=exportar)
    
    
        else:
            ms.showinfo(message="Datos insuficientes para exportar")




def dibujar():

    ### Seleccionar estructura
    emergente_v = Toplevel(ventana)
    emergente_v.title('Elige que dibujar')
    emergente_v.geometry(f"540x140+{int(ventana.winfo_width()/2)-270}+{int(ventana.winfo_height()/2)-70}")
    emergente_v.iconbitmap(f"{path}/Recursos/Imagenes/Logo-Banco.ico")
    emergente_v.config(bg = fondo)
    emergente_v.resizable(False, False)

    def activar_dir(event):
        if vp_var.get() != '':
            direcciones = planta[planta['Vicepresidencia']==vp_var.get()]
            direcciones = list(direcciones['Dirección / Gerencia'].unique())
            try:
                direcciones.remove(vp_var.get())
            except:
                print('non error')

            dire.config(state = 'readonly')
            area.config(state = 'disabled')
            dire['values']= direcciones
            dire.set('')


    def activar_area(event):
        if dir_var.get() != '':
            areas = planta[planta['Dirección / Gerencia']==dir_var.get()]
            areas = list(areas['Área / Oficina'].unique())
            try:
                areas.remove(dir_var.get())
            except:
                print('non error')

            area.config(state = 'readonly')
            area['values']= areas
            area.set('')

    # VP
    vp_var = StringVar()
    titulo_vp = Label(emergente_v,text = 'Vicepresidencia')
    titulo_vp.config(width = 15, height = 2, bg = fondo, fg= 'dimgray', font = ('calibri',10,'italic'), anchor = 'e')
    titulo_vp.grid(row=0, column=0)

    vp = ttk.Combobox(emergente_v, width = 50, textvariable = vp_var, state = 'readonly')
    vp.grid(row=0, column=1)
    
    if np.isin(user.lower(), admin):
        vp['values']=list(planta['Vicepresidencia'].unique())
        vp.bind("<<ComboboxSelected>>", activar_dir)
    else:
        vp['values']= usuarios_a[usuarios_a['Usuario']==user.lower()]['VP inicial'].values[0].split(sep=',')


    # Dir
    dir_var = StringVar()
    titulo_dir = Label(emergente_v,text = 'Dirección')
    titulo_dir.config(width = 15, height = 2, bg = fondo, fg= 'dimgray', font = ('calibri',10,'italic'), anchor = 'e')
    titulo_dir.grid(row=1, column=0)

    dire = ttk.Combobox(emergente_v, width = 50, textvariable = dir_var, state = 'disabled')
    dire.grid(row=1, column=1)

    dire.bind("<<ComboboxSelected>>", activar_area)

    # Area
    area_var = StringVar()
    titulo_area = Label(emergente_v,text = 'Área / Oficina')
    titulo_area.config(width = 15, height = 2, bg = fondo, fg= 'dimgray', font = ('calibri',10,'italic'), anchor = 'e')
    titulo_area.grid(row=2, column=0)

    area = ttk.Combobox(emergente_v, width = 50, textvariable = area_var, state = 'disabled')
    area.grid(row=2, column=1)

    # Espacio
    espacio = Label(emergente_v,width = 2, height =1, bd = 0, bg = fondo)
    espacio.grid(row = 1, column = 2)

    #Boton
    boton = Button(emergente_v)
    boton.config(bg = fondo, text = 'Aceptar',  font = ('calibri',10,'italic', 'bold'), width = 10, fg = "dimgray", relief = SOLID, bd = 1)
    boton.grid(row = 1, column = 3)

    # seleccionador
    seleccion_var = IntVar()
    seleccion = Checkbutton(emergente_v, onvalue = 1, offvalue = 0, variable = seleccion_var, text = 'Dibujar sólo la última estructura')
    seleccion.config(bg = fondo,font = ('calibri',10,'italic', 'italic'), fg = 'dimgray', bd = 0)
    seleccion.grid(row =  3, column = 1 )

    def obtener_datos():
        global posicion_dibujar

        obtener_estruc = [vp_var.get(),dir_var.get(),area_var.get()]
        estruc = []


        if seleccion_var.get() == 1:

            for i in obtener_estruc:
                if len(i) > 0:
                    estruc.append(i)

            vices = {'9976 Dir Nal De Canales Para Personas': 4619,
                        '9929 Vic Sostenib Y Serv Corpor': 14146,
                        '9947 Div Credito': 16297,
                        '9034 Dir Nal De Operaciones': 1410,
                        '9313 Div Comercial Red Mega': 11833,
                        '9926 Vicep Banca Consumo Y Pyme': 4291,
                        '9890 Vic Banca De Empresas': 13071,
                        '9975 Dir Nal De Canales Para Mipymes': 4378,
                        '0934 Div Internal Y Tesor': 17667,
                        '9033 Vic De Tecnologia': 53,
                        '9978 Presidencia': 1,
                        '9935 Vicep Ejecutiva': 5,
                        '9923 Vic Control Financiero Y Regulaci': 17459,
                        '9924 Contral General': 17402,
                        '9914 Revisoria Fiscal': 4250,
                        '9893 Vic Estrat Y Plane Financ': 13814,
                        '9984 Defensoria Consumi Financ': 4282
                            }

            if len(estruc) == 1:

                posicion_dibujar = vices[vp_var.get()]


            elif len(estruc) == 2:
                planta_dibujar = planta[planta['Dirección / Gerencia']==estruc[1]]

                j = ~ np.isin(planta_dibujar['Cod Posic Jefe'].values,planta_dibujar['Cod_Posicion'].values)
                k = planta_dibujar["Cod Posic Jefe"].values[j]
                l = planta_dibujar[planta_dibujar['Cod Posic Jefe']== k[np.nonzero(k)][0]]['Cod_Posicion'].values[0]

                posicion_dibujar = l

            elif len(estruc) == 3:
                planta_dibujar = planta[planta['Área / Oficina']==estruc[2]]

                j = ~ np.isin(planta_dibujar['Cod Posic Jefe'].values,planta_dibujar['Cod_Posicion'].values)
                k = planta_dibujar["Cod Posic Jefe"].values[j]
                posicion_dibujar = planta_dibujar[planta_dibujar['Cod Posic Jefe']== k[np.nonzero(k)][0]]['Cod_Posicion'].values[0]



            limpiar()
            lista_cuadros.append(creador(posicion_dibujar))
            lista_cuadros[-1].desplegar(None)

        else:

            for i in obtener_estruc:
                if len(i) > 0:
                    estruc.append(i)
            estructura_dibujar = []

            vices = {'9976 Dir Nal De Canales Para Personas': 4619,
                        '9929 Vic Sostenib Y Serv Corpor': 14146,
                        '9947 Div Credito': 16297,
                        '9034 Dir Nal De Operaciones': 1410,
                        '9313 Div Comercial Red Mega': 11833,
                        '9926 Vicep Banca Consumo Y Pyme': 4291,
                        '9890 Vic Banca De Empresas': 13071,
                        '9975 Dir Nal De Canales Para Mipymes': 4378,
                        '0934 Div Internal Y Tesor': 17667,
                        '9033 Vic De Tecnologia': 53,
                        '9978 Presidencia': 1,
                        '9935 Vicep Ejecutiva': 5,
                        '9923 Vic Control Financiero Y Regulaci': 17459,
                        '9924 Contral General': 17402,
                        '9914 Revisoria Fiscal': 4250,
                        '9893 Vic Estrat Y Plane Financ': 13814,
                        '9984 Defensoria Consumi Financ': 4282
                            }

            if len(estruc) == 1:
                estructura_dibujar.append(vices[vp_var.get()])


            elif len(estruc) == 2:
                planta_dibujar = planta[planta['Dirección / Gerencia']==estruc[1]]

                j = ~ np.isin(planta_dibujar['Cod Posic Jefe'].values,planta_dibujar['Cod_Posicion'].values)
                k = planta_dibujar["Cod Posic Jefe"].values[j]
                l = planta_dibujar[planta_dibujar['Cod Posic Jefe']== k[np.nonzero(k)][0]]['Cod_Posicion'].values[0]
                l_jefe = planta[planta['Cod_Posicion']==l]['Cod Posic Jefe'].values[0]

                estructura_dibujar.append(l_jefe)
                estructura_dibujar.append(l)

            elif len(estruc) == 3:
                planta_dibujar = planta[planta['Área / Oficina']==estruc[2]]

                j = ~ np.isin(planta_dibujar['Cod Posic Jefe'].values,planta_dibujar['Cod_Posicion'].values)
                k = planta_dibujar["Cod Posic Jefe"].values[j]
                l = planta_dibujar[planta_dibujar['Cod Posic Jefe']== k[np.nonzero(k)][0]]['Cod_Posicion'].values[0]
                l_jefe = planta[planta['Cod_Posicion']==l]['Cod Posic Jefe'].values[0]

                estructura_dibujar.append(vices[vp_var.get()])
                estructura_dibujar.append(l_jefe)
                estructura_dibujar.append(l)


            limpiar()
            lista_cuadros.append(creador(estructura_dibujar[0]))

            for i in lista_cuadros:
                if np.isin(i.cod_pos,estructura_dibujar)== True:
                    i.desplegar(None)

        emergente_v.withdraw()


    boton.config(command=obtener_datos)

def buscar():
    
    limpiar()
    
    buscar_v = Toplevel(ventana)
    buscar_v.title('Buscar')
    buscar_v.geometry(f"340x100+{int(ventana.winfo_width()/2)-170}+{int(ventana.winfo_height()/2)-50}")
    buscar_v.iconbitmap(f"{path}/Recursos/Imagenes/Logo-Banco.ico")
    buscar_v.config(bg = fondo)
    buscar_v.resizable(False, False)
    
    def _color_():
        if var_buscar.get()== 1:
            radio_posicion.config(fg = "black")
            radio_cedula.config(fg = 'dimgray')
        else:
            radio_posicion.config(fg = "dimgray")
            
            radio_cedula.config(fg = 'black')
    
    def buscar_persona():
        variable_buscar = entrada.get('1.0','end')
        tipo = var_buscar.get()
        
        lista_dibujar = []
        
        if tipo == 1: #posicion
            
            try:
                try:
                    posicion = int(variable_buscar[:-1])
                    lista_dibujar.append(posicion)
                except:
                    print('sin pos')
                    
                try:
                    jefe = int(planta[planta['Cod_Posicion']== posicion]['Cod Posic Jefe'].values[0])
                    lista_dibujar.append(jefe)
                except:    
                    print('sin jefe')
                    
                try:
                    jefe_jefe = int(planta[planta['Cod_Posicion']== jefe]['Cod Posic Jefe'].values[0])
                    lista_dibujar.append(jefe_jefe)
                except:
                    print('Sin jefe jefe')            
                
                lista_dibujar = lista_dibujar[::-1]
                
                try:
                    lista_cuadros.append(creador(lista_dibujar[0]))
                    lista_cuadros[-1].desplegar(None)
                        
                    for i in lista_cuadros:
                        if i.cod_pos == lista_dibujar[1]:
                            i.desplegar(None)
                            break
                except:
                    lista_cuadros.append(creador(lista_dibujar[1]))
                    lista_cuadros[-1].desplegar(None)
                        
                    for i in lista_cuadros:
                        if i.cod_pos == lista_dibujar[2]:
                            i.desplegar(None)
                            break
                for i in lista_cuadros:
                    if i.cod_pos == lista_dibujar[-1]:
                        i.barra_baja.config(bg = "gold")
                
            except:
                ms.showinfo(message='No es posible dibujar a los líderes de esta persona')
                
            buscar_v.withdraw()
                
            
        elif tipo == 2: #cedula
            
            try:
                try:
                    posicion = int(planta[planta['Cedula']== int(variable_buscar[:-1])]['Cod_Posicion'].values[0])
                    lista_dibujar.append(posicion)
                except:
                    print('sin pos')
                    
                try:
                    jefe = int(planta[planta['Cod_Posicion']== posicion]['Cod Posic Jefe'].values[0])
                    lista_dibujar.append(jefe)
                except:    
                    print('sin jefe')
                    
                try:
                    jefe_jefe = int(planta[planta['Cod_Posicion']== jefe]['Cod Posic Jefe'].values[0])
                    lista_dibujar.append(jefe_jefe)
                except:
                    print('Sin jefe jefe')            
                
                lista_dibujar = lista_dibujar[::-1]
                
                try:
                    lista_cuadros.append(creador(lista_dibujar[0]))
                    lista_cuadros[-1].desplegar(None)
                        
                    for i in lista_cuadros:
                        if i.cod_pos == lista_dibujar[1]:
                            i.desplegar(None)
                            break
                except:
                    lista_cuadros.append(creador(lista_dibujar[1]))
                    lista_cuadros[-1].desplegar(None)
                        
                    for i in lista_cuadros:
                        if i.cod_pos == lista_dibujar[2]:
                            i.desplegar(None)
                            break
                        
                for i in lista_cuadros:
                    if i.cod_pos == lista_dibujar[-1]:
                        i.barra_baja.config(bg = "gold")
                        
            except:
                ms.showinfo(message='No es posible dibujar a los líderes de esta persona')
            
            buscar_v.withdraw()
            
        else:
            ms.showinfo(message = 'Seleccione el tipo de búsqueda')
            buscar_v.withdraw()
            
    var_buscar = IntVar()
    
    radio_posicion = Radiobutton(buscar_v, text = ' Buscar por posición', variable = var_buscar, value = 1, command = _color_)
    radio_posicion.config(bd = 0,activebackground = fondo, width = 20, bg = fondo, fg = 'dimgray')
    radio_posicion.pack(side = LEFT,anchor = "n")
    
    radio_cedula = Radiobutton(buscar_v, text = ' Buscar por cédula', variable = var_buscar, value = 2, command = _color_)
    radio_cedula.config(bd = 0,activebackground = fondo, width = 22, bg = fondo, fg = 'dimgray')
    radio_cedula.pack(side = LEFT,anchor = "n")
    
    entrada = Text(buscar_v, bd = 1, relief = 'solid', bg= fondo, font = ('calibri',15,'italic'), fg = 'dimgray')
    entrada.config(width = 30, height = 1)
    entrada.place(x = 20, y = 30)
    
    buscar_boton = Button(buscar_v, text = 'Buscar', fg = 'dimgray', font = ('calibri',12,'italic','bold'), bg = fondo, width = 10)
    buscar_boton.config(command = buscar_persona)
    buscar_boton.place(x = 125 , y = 65)    
            
    buscar_v.mainloop()
 


# Menu
Menu_principal = Menu(ventana)
Menu_principal.add_command(label="Inicio", command = inicio)
Menu_principal.add_command(label="Limpiar",command = limpiar)
Menu_principal.add_command(label='Dibujar', command = dibujar)

if np.isin(user.lower(), admin):
    Menu_principal.add_command(label='Exportar información', command = export)
    
if np.isin(user.lower(), admin):
    Menu_principal.add_command(label='Buscar', command = buscar)


legends = filter_legends(ver)

ventana.config(menu = Menu_principal)
ventana.focus_force()


ventana.mainloop()
