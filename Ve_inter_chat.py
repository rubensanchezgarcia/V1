#Importamos lo que necesitamos para enseñar el maps.
import folium
from tkinterweb import HtmlFrame

#Importamos las librerias que necesitamos.
import tkinter as tk
from tkinter import messagebox
import os
from PIL import ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from airport import *
from aircraft import *
from LEBL import *

#Creamos una lista de aeropuertos para usarla de lista global.
Airports_list= []
Arrivals_list = []
Bcn_structure = None

#Creamos la ventana principal.
pady_number=2
ventana = tk.Tk()
ventana.geometry('1000x600')
ventana.title('Airport Manager | By: Managing Airports SA™')
ventana.configure(bg='white')
#Configuramos la ventana para que tenga dos columnas y varias filas, una para "sección de acción" donde pondremos los botones.
ventana.columnconfigure(0, weight=1, minsize=260) # Columna de botones.
ventana.columnconfigure(1, weight=10, minsize=720) #Ponemos un wight de 10 porque será mucho mças grande que la columande botones
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)

#Ahora creamos y organizamos los botones que va a tener esta Interface.
#Primero creamos un apartado de esta primera columna que será donde el usuario tenga la posibiliad de hacer todo lo relacionado con añadir y quitar aeropurtos.
airport_management_frame = tk.LabelFrame(ventana, text='Airport Management')
airport_management_frame.grid(row=0, column=0, padx=5, pady=pady_number, sticky = tk.N+tk.S+tk.E+tk.W)
#Hacemos espacio para que en este frame quepan todos los botons que queremos añadir.
airport_management_frame.rowconfigure(0, weight=1)
airport_management_frame.rowconfigure(1, weight=3)
airport_management_frame.rowconfigure(2, weight=1) # 3Columnas para: Load Airports/Add Airports/Remove Airports

airport_management_frame.columnconfigure(0, weight=1)



#Ponemos el botón Load Airports
#Creamos la función:
def Load_Airports_INT():
    global Airports_list
    Airports_list = LoadAirports('Airports.txt')
    if len(Airports_list)>0:
        messagebox.showinfo('Message','Airports Loaded Successfully')
    else:
        messagebox.showinfo('Message','No Airports Found')

load_airports_button = tk.Button(airport_management_frame, text="Load Airports", command = Load_Airports_INT)
load_airports_button.grid(column=0, row=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)

#Creamos el frame de añadir aeropuertos.
add_airport_frame = tk.LabelFrame(airport_management_frame, text='Add Airport')
add_airport_frame.grid(column=0, row=1, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)
add_airport_frame.rowconfigure(0, weight=1)
add_airport_frame.rowconfigure(1, weight=1)
add_airport_frame.rowconfigure(2, weight=1)
add_airport_frame.columnconfigure(0, weight=1)

#Creamos un frame para cada entrada de texto, latitud, longitud y el ICAO.
ICAO= tk.LabelFrame(add_airport_frame, text='ICAO')
ICAO.grid(column=0, row=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)
ICAO.rowconfigure(0, weight=1)
ICAO.columnconfigure(0, weight=1)
#Seguimos con el cuadro donde se escribirá el texto.
ICAO_entry= tk.Entry(ICAO)
ICAO_entry.grid(column=0, row=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)

Lat = tk.LabelFrame(add_airport_frame, text='Latitude')
Lat.grid(column=0, row=1, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)
Lat.columnconfigure(0, weight=1)
Lat.rowconfigure(0, weight=1)
#Cuadro de entrada de texto
Lat_entry= tk.Entry(Lat)
Lat_entry.grid(column=0, row=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)

Lon = tk.LabelFrame(add_airport_frame, text='Longitude')
Lon.grid(column=0, row=2, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)
Lon.columnconfigure(0, weight=1)
Lon.rowconfigure(0, weight=1)
#Cuadro de entrada de texto
Lon_entry= tk.Entry(Lon)
Lon_entry.grid(column=0, row=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)
#Añadimos el botón de añadir aeropuerto con su respectiva función.
def Add_Airport_INT():
    global Airports_list
    if len(Airports_list)<=0:
        messagebox.showinfo('Message','Load the Airports')
        return
    ICAO = ICAO_entry.get()
    latitude = Lat_entry.get()
    longitude = Lon_entry.get()
    added_airport= Airport(ICAO, latitude, longitude)
    resultado = AddAirport(Airports_list, added_airport)
    if resultado == 'Error|El aeropuerto ya existe' :
        messagebox.showinfo('Message','Error | Airport already exists')
    else:
        messagebox.showinfo('Message','Airport Added Successfully')

add_airport_button=tk.Button(add_airport_frame, command = Add_Airport_INT, text='Add Airport', bg='light blue')
add_airport_button.grid(row=3, column=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)

#Ahora añadimos la función quitar aeropuerto.
remove_frame = tk.LabelFrame(airport_management_frame, text='Removal of Airports')
remove_frame.grid(column=0, row= 2, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)
remove_frame.rowconfigure(0, weight=1)
remove_frame.rowconfigure(1, weight=1)
remove_frame.columnconfigure(0, weight=1)

#Introducción del ICAO del aeropuerto que queremos quitar.
remove_ICAO = tk.LabelFrame(remove_frame, text='ICAO')
remove_ICAO.grid(row=0, column=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)
remove_ICAO.rowconfigure(0, weight=1)
remove_ICAO.columnconfigure(0, weight=1)
#Introducción de texto
remove_ICAO_entry= tk.Entry(remove_ICAO)
remove_ICAO_entry.grid(row=0, column=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)
#Añadimos el botón que hará efectiva la eliminación del aeroperto. Con su respectiva función
def Remove_Airport_INT():
    global Aiports_list
    if len(Airports_list)<=0:
        messagebox.showinfo('Message','Load the Airports')
        return
    ICAO_removal = remove_ICAO_entry.get()
    resultado = RemoveAirport(Airports_list, ICAO_removal)
    if resultado == 'Error|Aeropuerto no encontrado':
        messagebox.showinfo('Message','Error | Airport not found')
    else:
        messagebox.showinfo('Message','Airport Removed Successfully')

remove_ICAO_button=tk.Button(remove_ICAO, text="Remove", command=Remove_Airport_INT, bg='red')
remove_ICAO_button.grid(row=1, column=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)

#Ahora vamos a añadir la función de enseñar el gráfico por pantalla. Para eso, creamos un canvas donde meter ese gráfico.
#Creamos el frame donde estará ese canvas.
canvas_frame = tk.LabelFrame(ventana, text='Advanced Visualization System®', bg='light blue')
canvas_frame.grid(row=0, column=1, rowspan = 10, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N + tk.S)
canvas_frame.rowconfigure(0, weight=1)
canvas_frame.columnconfigure(0, weight=1)
#Creamos el canvas (contenedor de la imagen)|Siendo la imagen un gráifco no hace falta este canvas porque después ya se crea con una de las funciones más adelnta, pero esteticamente queda mejor.
canva = tk.Canvas(canvas_frame, width=200, height=400)
canva.grid(row=0, column=0, rowspan=5, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N + tk.S)

#Creamos una función que se encargue de borrar los gráficos ya existentes en el mapa para que el siguiente se coloque correctamente sin problemas.
def Clear_Canvas():
    for widget in canvas_frame.winfo_children():
        widget.destroy()
#Creamos el botón que active la función de enseñar el gráfico. Con su respectiva función
def Schengen_Plot_INT():
    global Airports_list

    if len(Airports_list)<=0:
        messagebox.showinfo('Message','Load the Airports')
        return

    #Añadimos la función clear canvas para que el gráfico que anteriormente habia en el canvas desaparezca y este nuevo aparezca de manera correcta y en solitario.
    Clear_Canvas()
    #Usamos la función para definir que aeropuerto son y no son schengen.
    SetSchengen(Airports_list)
    #Sacamos lo que es la figura que es lo que devuelve la función, no devuelve un gráfico.
    fig = PlotAirports(Airports_list)
    #Coge la fig de matplotlib y la mete dentro de un “canvas compatible con tkinter” para poder verla en la interfaz
    canvas = FigureCanvasTkAgg(fig, master = canvas_frame)
    #Dibujamos el canva con la figura/imagen del gráfico.
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)
    if 'canva' in globals():
       canva.grid_forget()
schengen_plot_button = tk.Button(ventana, text='Plot Schengen Airports', command= Schengen_Plot_INT, bg='Blue')
schengen_plot_button.grid(column=0, row=1, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N + tk.S)

#Añadir boton que abra google earth con la localización de cada aeropuerto. Con su respectiva función
#Función:
def open_maps():

    global Airports_list
    if len(Airports_list)<=0:
        messagebox.showinfo('Message','Load the Airports')
        return
    MapAirports(Airports_list)
    os.startfile('mapAirports.kml')

open_maps_button=tk.Button(ventana,  text="Show map", bg='green' , command = open_maps)
open_maps_button.grid(row=2, column=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N)



#Añadimos un frame en el que van a ir todos los botones y entradas relacionados con los arrivals
arrivals = tk.LabelFrame(ventana, text="Arrivals", bg='light yellow')
arrivals.grid(row=3, column=0, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N)
arrivals.columnconfigure(0, weight=1)
arrivals.columnconfigure(1, weight=1)
arrivals.rowconfigure(0, weight=1)
arrivals.rowconfigure(1, weight=1)


#Añadimos el botón load arrivals con su respectiva función.
def Load_Arrivals_INT():
    global Arrivals_list
    Arrivals_list = LoadArrivals('Arrivals.txt')
    if len(Arrivals_list) <= 0:
        messagebox.showinfo('Message', 'No arrivals found in the File.')
        return
    else:
        messagebox.showinfo('Message', 'Arrivals loaded successfully.')
#Añadimos el botón
load_arrivals_button = tk.Button(arrivals, text='Load Arrivals', command=Load_Arrivals_INT, bg='beige')
load_arrivals_button.grid(row=0, column=0, padx=5, pady=pady_number, rowspan=2,  sticky = tk.W + tk.E + tk.N + tk.S)

#Añadimos la función de Plot arrivals y después su respectivo botón.

#Añadimos la función de Plot arrivals y después su respectivo botón.
def Plot_Arrivals_INT():
    global Arrivals_list

    if len(Arrivals_list) <= 0:
        messagebox.showinfo('Message', 'Load arrivals first.')
        return

    #Añadimos la función clear canvas para que aparezca correctamente el plot nuevo sin problemas.
    Clear_Canvas()
    fig = PlotAirlines(Arrivals_list)

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()

    canvas.get_tk_widget().grid(row=0,column=0,padx=5,pady=pady_number,sticky=tk.W + tk.E + tk.N + tk.S)

    if 'canva' in globals():
        canvas.grid_forget()



plot_arrivals_button = tk.Button(arrivals, text='Plot Arrivals by Airline', command=Plot_Arrivals_INT, bg='beige')
plot_arrivals_button.grid(row=0, column=1, padx=5, pady=pady_number, sticky=tk.W + tk.E + tk.N + tk.S)



#Ahora hacemos lo mismo con el toro plot. Añadimos el botón y su respectiva función.
def PlotFlightsType_INT():
    global Arrivals_list
    if len(Arrivals_list)<=0:
        messagebox.showinfo('Message','Load arrivals first.')
        return
    fig = PlotFlightsType(Arrivals_list)
    Clear_Canvas()

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()

    canvas.get_tk_widget().grid(row=0,column=0,padx=5,pady=pady_number,sticky=tk.W + tk.E + tk.N + tk.S)

    if 'canva' in globals():
        canvas.grid_forget()

#Creamos el botón
plot_type_button=tk.Button(arrivals, command=PlotFlightsType_INT, bg='beige', text='Plot Flights by type')
plot_type_button.grid(column=1, row=1, padx=5, pady=pady_number, sticky = tk.W + tk.E + tk.N+ tk.S)


####################### Escrivimos el código perteneciente a la Versión 3 #############

# Frame para gestionar las terminales, gates y ocupación
gates_frame = tk.LabelFrame(ventana, text='Airports Gates Management', bg='light green')
gates_frame.grid(row=4, column=0, padx=5, pady=pady_number, sticky=tk.W + tk.E + tk.N + tk.S)

gates_frame.columnconfigure(0, weight=1)
gates_frame.rowconfigure(0, weight=1)
gates_frame.rowconfigure(1, weight=1)
gates_frame.rowconfigure(2, weight=1)
gates_frame.rowconfigure(3, weight=1)
gates_frame.rowconfigure(4, weight=1)


# Función para cargar la estructura del aeropuerto LEBL
def LoadAirport_Structure_INT():
    global Bcn_structure

    Bcn_structure = LoadAirportStructure('Terminals.txt')

    if Bcn_structure == "Error | File not found":
        messagebox.showinfo('Message', 'Error | File not found')
        return

    if Bcn_structure == "Error | Empty file":
        messagebox.showinfo('Message', 'Error | Empty file')
        return

    if Bcn_structure == "Error | Wrong file format":
        messagebox.showinfo('Message', 'Error | Wrong file format')
        return

    if Bcn_structure == "Error | Area without terminal":
        messagebox.showinfo('Message', 'Error | Area without terminal')
        return

    if Bcn_structure == "Error | Wrong gate numbers":
        messagebox.showinfo('Message', 'Error | Wrong gate numbers')
        return

    messagebox.showinfo('Message', 'LEBL airport structure loaded successfully.')


load_airport_structure = tk.Button(
    gates_frame,
    text='Load Airport Structure',
    command=LoadAirport_Structure_INT
)
load_airport_structure.grid(row=0, column=0, padx=5, pady=pady_number, sticky=tk.W + tk.E + tk.N + tk.S)


# Función para mostrar la ocupación de las gates
def PlotGateOccupancy_INT():
    global Bcn_structure

    if Bcn_structure == None:
        messagebox.showinfo('Message', 'Load airport structure first.')
        return

    Clear_Canvas()

    fig = PlotGateOccupancy(Bcn_structure)

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()

    canvas.get_tk_widget().grid(
        row=0,
        column=0,
        padx=5,
        pady=5,
        sticky=tk.W + tk.E + tk.N + tk.S
    )

    if 'canva' in globals():
        canvas.grid_forget()


plot_Gate_Occupancy_button = tk.Button(
    gates_frame,
    text='Plot Gate Occupancy',
    command=PlotGateOccupancy_INT
)
plot_Gate_Occupancy_button.grid(row=1, column=0, padx=5, pady=pady_number, sticky=tk.W + tk.E + tk.N + tk.S)


# Frame para buscar la terminal de una aerolínea
search_terminal_frame = tk.LabelFrame(gates_frame, text='Search Terminal', bg='sea green')
search_terminal_frame.grid(row=3, column=0, padx=5, pady=pady_number, sticky=tk.W + tk.E + tk.N + tk.S)

search_terminal_frame.columnconfigure(0, weight=1)
search_terminal_frame.rowconfigure(0, weight=1)
search_terminal_frame.rowconfigure(1, weight=1)

airline_entry_frame = tk.LabelFrame(search_terminal_frame, text='Airline ICAO', bg='sea green')
airline_entry_frame.grid(row=0, column=0, padx=5, pady=pady_number, sticky=tk.W + tk.E + tk.N + tk.S)

airline_entry_frame.columnconfigure(0, weight=1)
airline_entry_frame.rowconfigure(0, weight=1)

airline_entry = tk.Entry(airline_entry_frame)
airline_entry.grid(row=0, column=0, padx=5, pady=pady_number, sticky=tk.W + tk.E + tk.N + tk.S)


def SearchTerminal_INT():
    global Bcn_structure

    if Bcn_structure == None:
        messagebox.showinfo('Message', 'Load airport structure first.')
        return

    airline = airline_entry.get()

    if airline == "":
        messagebox.showinfo('Message', 'Write an airline ICAO code.')
        return

    terminal_name = SearchTerminal(Bcn_structure, airline)

    if terminal_name == "":
        messagebox.showinfo('Message', 'Airline not found in any terminal.')
    else:
        messagebox.showinfo('Message', airline + ' operates in ' + terminal_name)


search_terminal_button = tk.Button(
    search_terminal_frame,
    text='Search Terminal',
    command=SearchTerminal_INT
)
search_terminal_button.grid(row=1, column=0, padx=5, pady=pady_number, sticky=tk.W + tk.E + tk.N + tk.S)


# Frame para asignar una gate a un aircraft
def AssaignGate_INT():
    global Bcn_structure
    global Arrivals_list

    if Bcn_structure == None:
        messagebox.showinfo('Message', 'Load airport structure first.')
        return

    if len(Arrivals_list) <= 0:
        messagebox.showinfo('Message', 'Load arrivals first.')
        return

    assigned_counter = 0
    error_counter = 0
    already_assigned_counter = 0

    for i in range(len(Arrivals_list)):

        aircraft = Arrivals_list[i]

        # Comprobamos si este avión ya tiene una gate asignada
        already_assigned = False
        info_gates = GateOccupancy(Bcn_structure)

        g = 0
        while not already_assigned and g < len(info_gates):
            if info_gates[g][2] == aircraft.id:
                already_assigned = True
            else:
                g = g + 1

        if already_assigned == True:
            already_assigned_counter = already_assigned_counter + 1

        else:
            result = AssignGate(Bcn_structure, aircraft)

            if result == 0:
                assigned_counter = assigned_counter + 1
            else:
                error_counter = error_counter + 1

    messagebox.showinfo(
        'Message',
        'Gate assignment finished.\n' +
        'Assigned aircrafts: ' + str(assigned_counter) + '\n' +
        'Already assigned aircrafts: ' + str(already_assigned_counter) + '\n' +
        'Not assigned aircrafts: ' + str(error_counter)
    )
assaign_gate_button = tk.Button(
    gates_frame,
    text='Assign Gates',
    command=AssaignGate_INT,
    bg='aquamarine'
)

assaign_gate_button.grid(
    row=2,
    column=0,
    padx=5,
    pady=pady_number,
    sticky=tk.W + tk.E + tk.N + tk.S
)

ventana.mainloop()