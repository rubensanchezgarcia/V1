from airport import *
from aircraft import *

import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkintermapview

import os
from PIL import Image, ImageTk



# Añadimos la lista de aeropuertos que tendremos.
Airport_list=[]


########Inciamos el programa de la interfaz con la función correspondiente para cada botón.  #####

ventana= tk.Tk()
ventana.geometry('1400x800')
ventana.title('Expert Airoport Management® - By Jana, Pablo and Rubén | Airport Management Consulting™ ')
ventana.configure(bg="beige")
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=4)
ventana.columnconfigure(2, weight=4)
ventana.rowconfigure(0, weight=5)
ventana.rowconfigure(1, weight=5)


#Primer botón: LoadAirport con su correspondiente función.
def LoadAirport():
    global Airport_list
    Airport_list=LoadAirports('Airports.txt')
    if len(Airport_list) == 0:
        messagebox.showinfo('Warning', 'No Airports found')
    else:
        messagebox.showinfo('Warning', 'Airport loaded successfully')
    return Airport_list

button_load_airport_frame = tk.LabelFrame(ventana, text='Airports Management', bg= 'white')
button_load_airport_frame.grid(row = 7, column = 0, padx = 5, pady= 5, sticky=tk.N + tk.E + tk.W + tk.S)
button_load_airport_frame.columnconfigure(0, weight = 1)
button_load_airport_frame.columnconfigure( 1, weight = 2)
button_load_airport_frame.columnconfigure( 2, weight = 1)
button_load_airport_frame.rowconfigure(0, weight = 1)

button_load_airport = tk.Button(button_load_airport_frame, text='Load Airports', command=LoadAirport, bg='orange')
button_load_airport.grid(row=0, column=0 , padx = 2, pady = 2, sticky=tk.W + tk.E + tk.N + tk.S)
# Hacemos un cuadro dentro del cuadro de management de aeropuertos para añadir un aeropuerto donde habrá que añadir latitud, longitud e ICAO.
#La función que utilizremos:
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

#El frame, botón y entradas de texto.

button_add_airport_data_frame = tk.LabelFrame(button_load_airport_frame, text='Add Airport', bg ='white')
button_add_airport_data_frame.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_add_airport_data_frame.columnconfigure(0, weight = 1)
button_add_airport_data_frame.columnconfigure( 1, weight = 1)

button_add_airport_data_frame.rowconfigure(0, weight = 1)
button_add_airport_data_frame.rowconfigure(1, weight = 1)
button_add_airport_data_frame.rowconfigure(2, weight = 1)
#Añadimos las entradas de texto.
ICAO_frame = tk.LabelFrame(button_add_airport_data_frame, text='ICAO', bg='white')
ICAO_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
ICAO_frame.rowconfigure(0, weight = 1)
ICAO_frame.columnconfigure(0, weight = 1)
ICAO = tk.Entry(ICAO_frame)
ICAO.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)


latitude_frame = tk.LabelFrame(button_add_airport_data_frame, text='Latitude', bg='white')
latitude_frame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
latitude_frame.rowconfigure(0, weight = 1)
latitude_frame.columnconfigure(0, weight = 1)
latitude = tk.Entry(latitude_frame)
latitude.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

longitude_frame= tk.LabelFrame(button_add_airport_data_frame, text='Longitude', bg='white')
longitude_frame.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
longitude = tk.Entry(longitude_frame)
longitude_frame.rowconfigure(0, weight = 1)
longitude_frame.columnconfigure(0, weight = 1)
longitude.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
#El boton que hará que se añada.
button_add_airport=tk.Button(button_add_airport_data_frame, text='Add Airport', command = NewAirport, bg='yellow')
button_add_airport.grid( column=1, row=0, rowspan = 3 , padx = 5, pady = 5, sticky=tk.W + tk.E + tk.N + tk.S)

#Nuevo boton en el que vamos a hacer la función de quitar aeropuerto. Con su función correspondiente.
def RemoveAirport_Interface ():
    global Airport_list
    icao_R_text = ICAO_R.get()
    resultado=RemoveAirport(Airport_list, icao_R_text)
    if resultado =='Error|Aeropuerto no encontrado':
        messagebox.showinfo('Error', 'Airport not founded')
    else:
        messagebox.showinfo('Success', 'Airport removed correctly')
#En la interface
button_remove_airport_data_frame = tk.LabelFrame(button_load_airport_frame, text='Remove Airport', bg= 'white')
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


#Función e integración en la interface del gráfico de show schengen plot.
def schengen_plot_photo():
    if len(Airport_list) == 0:
        messagebox.showinfo('Error', 'First load the airports')
        return
    SaveSchengenAirports(Airport_list, 'schengen_Airports.txt')
    fig = PlotAirports(Airport_list)
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()

    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=500, height=300)
    canvas_picture.grid(row=1, column=0, padx=5, pady=5, sticky= tk.N + tk.E + tk.W + tk.S)

#Ahora vamos a crear el canvas para poder mostrar el gráfico por pantalla.
#Primero creamos el recinto donde va a estar este canvas.
canvas_frame=tk.LabelFrame(ventana, text='Advanced visualisation system© by Airport Management™', bg='light blue')
canvas_frame.grid(row=0, column= 1, columnspan=2,  padx=10, pady=10, sticky="nsew")
canvas_frame.columnconfigure(0, weight = 1)
canvas_frame.rowconfigure(0, weight = 1)


#Creamos el botón que hará que se vea la imagen.
button_show_plot_frame=tk.LabelFrame(ventana, text = 'Plot visualisation')
button_show_plot_frame.grid(row=7, column=1, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_show_plot_frame.columnconfigure(0, weight = 1)
button_show_plot_frame.rowconfigure(0, weight = 1)
button_show_plot=tk.Button(button_show_plot_frame, text='Show Schengen Airports plot', command = schengen_plot_photo)
button_show_plot.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Ahora creamos el botón que va a abrir el google maps. Añadimos también la función correspondiente.
def open_maps():
    global Airport_list
    if not Airport_list:
        messagebox.showinfo('Error', 'Primero carga los aeropuertos')
        return

    # Llamamos a la función original
    datos_aeropuertos = MapAirports(Airport_list)

    # Mstramos esos mismos datos en el widget de la interface
    map_widget = tkintermapview.TkinterMapView(frame_mapa, corner_radius=0)
    map_widget.pack(fill="both", expand=True)
    for ap in Airport_list:
        nombre = getattr(ap, 'icao', getattr(ap, 'ICAO', 'Aeropuerto'))
        map_widget.set_marker(ap.latitude, ap.longitude, text=nombre)


frame_mapa = tk.LabelFrame(ventana, text ='Google Earth View', bg='pink')
frame_mapa.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")



button_maps_frame=tk.LabelFrame(ventana, text = 'Maps')
button_maps_frame.grid(row=7, column=2, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_maps_frame.columnconfigure(0, weight = 1)
button_maps_frame.rowconfigure(0, weight = 1)
button_maps= tk.Button(button_maps_frame, text='Show Airports in Google Earth®', command=open_maps, bg='dark green')
button_maps.grid(row=0, column=0, padx=10, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)



###########Añadimos las funciones de la versión 2 ##########################
llegadas= []
def LoadArrivals_interface():
    global llegadas
    llegadas = LoadArrivals('Arrivals.txt')
    if len(llegadas) == 0:
        messagebox.showinfo('Error', 'No arrivals found')
        return
    else:
        messagebox.showinfo('Success', 'Arrivals loaded successfully')
    return llegadas

arrivals_management=tk.LabelFrame(ventana, text = 'Arrivals management', bg='white')
arrivals_management.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.W + tk.S)
arrivals_management.columnconfigure(0, weight = 1)
arrivals_management.rowconfigure(0, weight = 1)
arrivals_management.rowconfigure(1, weight = 1)
arrivals_management.rowconfigure(2, weight = 1)
arrivals_management.rowconfigure(3, weight = 1)




#Botón para cargar las arrivals
load_airports_frame=tk.LabelFrame(arrivals_management, text = 'Arrivals')
load_airports_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
load_airports_frame.columnconfigure(0, weight = 1)
load_airports_frame.rowconfigure(0, weight = 1)

load_airports_button=tk.Button(load_airports_frame, text='Load Arrivals', command= LoadArrivals_interface, bg='light blue')
load_airports_button.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.W + tk.S)

#Botón para hacer el plot de llegadas por aerolinea
def PlotArrivals_INT():
    global llegadas
    global canvas_picture

    if len(llegadas) == 0:
        messagebox.showinfo('Error', 'First load the airports')
        return
    fig = PlotAirports(llegadas)
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    if 'canvas_picture' in globals():
        canvas_picture.grid_forget()

    canvas_picture = canvas.get_tk_widget()
    canvas_picture.config(width=500, height=500)
    canvas_picture.grid(row=0, column=0, padx=5, pady=5, sticky= tk.N + tk.E + tk.W + tk.S)

frame_arrivals_plot = tk.LabelFrame(ventana, text='Arrivals by Airline', bg='light green')
frame_arrivals_plot.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

##Aprición de la función en la interface
button_airlines_plot_frame = tk.LabelFrame(arrivals_management, text='Airlines Information')
button_airlines_plot_frame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_airlines_plot_frame.columnconfigure(0, weight=1)
button_airlines_plot_frame.rowconfigure(0, weight=1)
button_airlines_plot = tk.Button(button_airlines_plot_frame, text='Show arrivals by Airline',command=PlotArrivals_INT, bg='pink')
button_airlines_plot.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Función visualización plot cantidad de vuelos provenientes del espacio schengen.
def PlotFlightsType_INT():
    global llegadas
    if len(llegadas)==0:
        messagebox.showinfo('Error', 'No airports found')
        return
    fig = PlotFlightsType(llegadas)
    canvas = FigureCanvasTkAgg(fig, master=frame_arrivaltype)
    canvas.draw()


    canvas_picture = canvas.get_tk_widget()
    canvas.get_tk_widget().pack(fill="both", expand=True)

frame_arrivaltype = tk.LabelFrame(ventana, text='Arrival type', bg='pink')
frame_arrivaltype.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")




button_type_plot_frame = tk.LabelFrame(arrivals_management, text='Schengen Information')
button_type_plot_frame.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_type_plot_frame.columnconfigure(0, weight=1)
button_type_plot_frame.rowconfigure(0, weight=1)
button_type_plot = tk.Button(button_type_plot_frame, text='Show arrival type',command=PlotFlightsType_INT, bg='pink')
button_type_plot.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Función map flight aircfats visualización de rutas que llegan a bcn:
def MapFlights_INT():
    global llegadas

    if not llegadas:
        messagebox.showinfo('Error', 'Primero carga las llegadas')
        return
    MapFlights(llegadas)

    frame_rutas = tk.LabelFrame(ventana, text='Routes visualization', bg='lemon chiffon')
    frame_rutas.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

    mapa_rutas_widget = tkintermapview.TkinterMapView(frame_rutas, corner_radius=0)
    mapa_rutas_widget.pack(fill="both", expand=True)

    #Usamos Barcelona (BCN) como destino fijo
    lat_bcn, lon_bcn = 41.2974, 2.0833
    for fl in llegadas:
        mapa_rutas_widget.set_marker(fl.latitude, fl.longitude, text=fl.icao)
        punto_origen = (fl.latitude, fl.longitude)
        punto_destino = (lat_bcn, lon_bcn)
        mapa_rutas_widget.set_path([punto_origen, punto_destino])
    mapa_rutas_widget.set_position(41.2974, 2.0833)
    mapa_rutas_widget.set_zoom(4)

#Integración de la función en la interface.
button_routes_frame = tk.LabelFrame(arrivals_management, text='Routes visualization')
button_routes_frame.grid(row=3, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
button_routes_frame.columnconfigure(0, weight=1)
button_routes_frame.rowconfigure(0, weight=1)
button_routes = tk.Button(button_routes_frame, text='Show routes',command=MapFlights_INT, bg='dark green')
button_routes.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

ventana.mainloop()