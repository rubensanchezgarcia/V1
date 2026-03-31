from airport import *

import tkinter as tk
from tkinter import messagebox

import os
from PIL import Image, ImageTk



# Añadimos la lista de aeropuertos que tendremos.
Airport_list=[]
#Las funciones que apareceran en el programa:
def LoadAirport():
    global Airport_list
    Airport_list=LoadAirports('Airports.txt')
    if len(Airport_list) == 0:
        messagebox.showinfo('Warning', 'No Airports found')
    else:
        messagebox.showinfo('Warning', 'Airport loaded successfully')
    return Airport_list
def SaveSchengen():
    SaveSchengenAirports( LoadAirport() , 'schengen_Airports.txt')
def NewAirport():
    global Airport_list

    icao_text = ICAO.get()
    latitude_text = latitude.get()
    longitude_text = longitude.get()

    airport = Airport(icao_text, float(latitude_text), float(longitude_text))
    resultado = AddAirport(Airport_list, airport)

    if resultado == 'Error|El aeropuerto ya existe':
        messagebox.showinfo('Error', 'Airport already in the list')
    else:
        messagebox.showinfo('Correct', 'Airport added correctly')

def RemoveAirport_Interface ():
    global Airport_list
    icao_R_text = ICAO_R.get()
    resultado=RemoveAirport(Airport_list, icao_R_text)
    if resultado =='Error|Aeropuerto no encontrado':
        messagebox.showinfo('Error', 'Airport not founded')
    else:
        messagebox.showinfo('Correct', 'Airport removed correctly')

def schengen_plot_photo():
    if len(Airport_list) == 0:
        messagebox.showinfo('Error', 'First load the airports')
        return
    fig = PlotAirports(Airport_list)
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()

    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=500, height=500)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5, sticky= tk.N + tk.E + tk.W + tk.S)

def open_maps():
    global Airport_list
    MapAirports(Airport_list)
    os.startfile('mapAirports.kml')
########Inciamos el programa de la interfaz #####

ventana= tk.Tk()
ventana.geometry('1000x1000')
ventana.title('Expert Airoport Management® - By Jana, Pablo and Rubén | Airport Management Consulting™ ')
ventana.rowconfigure(0,weight=10)
ventana.rowconfigure(7,weight=1)
ventana.columnconfigure(0, weight = 5)
ventana.columnconfigure(1, weight = 1)
ventana.columnconfigure(2, weight = 2)
ventana.columnconfigure(3, weight = 2)

#Primer botón: LoadAirport
button_load_airport_frame = tk.LabelFrame(ventana, text='Airports Management')
button_load_airport_frame.grid(row = 7, column = 0, padx = 5, pady= 5, sticky=tk.N + tk.E + tk.W + tk.S)
button_load_airport_frame.columnconfigure(0, weight = 1)
button_load_airport_frame.columnconfigure( 1, weight = 2)
button_load_airport_frame.columnconfigure( 2, weight = 1)
button_load_airport_frame.rowconfigure(0, weight = 1)

button_load_airport = tk.Button(button_load_airport_frame, text='Load Airports', command=LoadAirport)
button_load_airport.grid(row=0, column=0 , padx = 2, pady = 2, sticky=tk.W + tk.E + tk.N + tk.S)
# Hacemos un cuadro dentro del cuadro de management de aeropuertos para añadir un aeropuerto donde habrá que añadir latitud, longitud e ICAO.
button_add_airport_data_frame = tk.LabelFrame(button_load_airport_frame, text='Add Airport')
button_add_airport_data_frame.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_add_airport_data_frame.columnconfigure(0, weight = 1)
button_add_airport_data_frame.columnconfigure( 1, weight = 1)

button_add_airport_data_frame.rowconfigure(0, weight = 1)
button_add_airport_data_frame.rowconfigure(1, weight = 1)
button_add_airport_data_frame.rowconfigure(2, weight = 1)
#Añadimos las entradas de texto.
ICAO_frame = tk.LabelFrame(button_add_airport_data_frame, text='ICAO')
ICAO_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
ICAO_frame.rowconfigure(0, weight = 1)
ICAO_frame.columnconfigure(0, weight = 1)
ICAO = tk.Entry(ICAO_frame)
ICAO.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

latitude_frame = tk.LabelFrame(button_add_airport_data_frame, text='Latitude')
latitude_frame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
latitude_frame.rowconfigure(0, weight = 1)
latitude_frame.columnconfigure(0, weight = 1)
latitude = tk.Entry(latitude_frame)
latitude.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

longitude_frame= tk.LabelFrame(button_add_airport_data_frame, text='Longitude')
longitude_frame.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
longitude = tk.Entry(longitude_frame)
longitude_frame.rowconfigure(0, weight = 1)
longitude_frame.columnconfigure(0, weight = 1)
longitude.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
#El boton que hará que se añada.
button_add_airport=tk.Button(button_add_airport_data_frame, text='Add Airport', command = NewAirport)
button_add_airport.grid( column=1, row=0, rowspan = 3 , padx = 5, pady = 5, sticky=tk.W + tk.E + tk.N + tk.S)

#Nuevo boton en el que vamos a hacer la función de quitar aeropuerto.
button_remove_airport_data_frame = tk.LabelFrame(button_load_airport_frame, text='Remove Airport')
button_remove_airport_data_frame.grid(row=0, column=2, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_remove_airport_data_frame.columnconfigure(0, weight = 1)
button_remove_airport_data_frame.rowconfigure( 0, weight = 1)
button_remove_airport_data_frame.rowconfigure(1, weight = 1)
button_remove_airport_data_frame.rowconfigure(2, weight = 1)
button_remove_airport_data_frame.rowconfigure(3, weight = 1)
button_remove_airport_data_frame.rowconfigure(4, weight = 1)
button_remove_airport_data_frame.rowconfigure(5, weight = 1)
button_remove_airport_data_frame.rowconfigure(6, weight = 1)
button_remove_airport_data_frame.rowconfigure(7, weight = 1)
button_remove_airport_data_frame.rowconfigure(8, weight = 1)


ICAO_frame_R = tk.LabelFrame(button_remove_airport_data_frame, text='ICAO')
ICAO_frame_R.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
ICAO_frame_R.rowconfigure(0, weight = 1)
ICAO_frame_R.columnconfigure(0, weight = 1)
ICAO_R = tk.Entry(ICAO_frame_R)
ICAO_R.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button_Remove_airport=tk.Button(button_remove_airport_data_frame, text='Remove Airport', command = RemoveAirport_Interface, bg='red')
button_Remove_airport.grid( column=0, row=1, rowspan = 7 , padx = 5, pady = 5, sticky=tk.W + tk.E + tk.N + tk.S)
#Segundo botón: SaveSchengen
button_SaveSchengen_frame = tk.LabelFrame(ventana, text='Schengen Airports')
button_SaveSchengen_frame.grid(row=7, column = 1, padx =5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_SaveSchengen_frame.rowconfigure(0, weight = 1)
button_SaveSchengen_frame.columnconfigure(0, weight = 1)
button_SaveSchengen = tk.Button(button_SaveSchengen_frame, text = 'Save Schengen Airports', command=SaveSchengen, bg='blue')
button_SaveSchengen.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S )

#Ahora vamos a crear el canvas para poder mostrar el gráfico por pantalla.
#Primero creamos el recinto donde va a estar este canvas.
canvas_frame=tk.LabelFrame(ventana, text='Advanced visualisation system© by Airport Management™', bg='light blue')
canvas_frame.grid(row=0, column=0, columnspan=4,  padx=5, pady=5, sticky=tk.N + tk.W + tk.S)
canvas_frame.columnconfigure(0, weight = 1)
canvas_frame.rowconfigure(0, weight = 1)



#Creamos el botón que hará que se vea la imagen.
button_show_plot_frame=tk.LabelFrame(ventana, text = 'Plot visualisation')
button_show_plot_frame.grid(row=7, column=2, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_show_plot_frame.columnconfigure(0, weight = 1)
button_show_plot_frame.rowconfigure(0, weight = 1)
button_show_plot=tk.Button(button_show_plot_frame, text='Show Schengen Airports plot', command = schengen_plot_photo)
button_show_plot.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Ahora creamos el botón que va a abrir el google maps con los aeropuertos en el.
button_maps_frame=tk.LabelFrame(ventana, text = 'Maps')
button_maps_frame.grid(row=7, column=3, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_maps_frame.columnconfigure(0, weight = 1)
button_maps_frame.rowconfigure(0, weight = 1)
button_maps= tk.Button(button_maps_frame, text='Show Airports in Google Earth®', command=open_maps, bg='green')
button_maps.grid(row=0, column=0, padx=10, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
ventana.mainloop()

