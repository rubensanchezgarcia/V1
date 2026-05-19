from airport import *
from aircraft import *
import matplotlib.pyplot as plt


class BarcelonaAP:
    def __init__(self, code):
        self.code = code
        self.terminal = []
class Terminal:
    def __init__(self, name):
        self.name = name
        self.BoardingArea = []
        self.airlines = []
class BoardingArea:
    def __init__(self, name):
        self.name = name
        self.schengen = False
        self.gate = []
class Gate:
    def __init__(self, name):
        self.name = name
        self.occupancy = False
        self.aircraft_id = ""


def SetGates(area, init_gate, end_gate, prefix):
    # Si end_gate no es mayor que init_gate, devolvemos error
    if end_gate <= init_gate:
        return -1

    # Borramos la lista anterior de gates del área
    area.gate = []

    # Creamos todas las gates desde init_gate hasta end_gate
    for num in range(init_gate, end_gate + 1):
        name_gate = prefix + str(num)
        new_gate = Gate(name_gate)
        area.gate.append(new_gate)

    return 0







def LoadAirlines (Terminal, t_name):
    filename = t_name + "_Airlines.txt" #Esto crea el file que leerá la función
    airlines_terminal = []
    f = open (filename, 'r')
    linea = f.readlines()

    for i in range (len(linea)): #Recorre todas las líneas.
        parts = linea[i].split(" ")  #Separa la línea en partes cuando encuentra un espacio en blanco.
        if len(parts) == 2:
            airline_name = parts[0]
            airline_icao_code = parts[1]
            airlines_terminal.append(airline_name)
        else:
            return "Error | Linea con formato erróneo"

    if len(airlines_terminal) == 0:
        return "Error | Fichero vacío o inexistente"
    else:
        Terminal.airlines=airlines_terminal
        return Terminal

def LoadAirportStructure(filename):

    try:
        f = open(filename, 'r')
        lineas = f.readlines()
        f.close()
    except:
        return "Error | File not found"

    if len(lineas) == 0:
        return "Error | Empty file"

    # Primera línea: LEBL 2 terminals
    parts = lineas[0].split()

    if len(parts) < 2:
        return "Error | Wrong file format"

    code = parts[0]

    # Creamos el aeropuerto de Barcelona
    bcn = BarcelonaAP(code)

    current_terminal = None

    # Recorremos todas las líneas menos la primera
    for i in range(1, len(lineas)):

        parts = lineas[i].split()

        if len(parts) > 0:

            # Línea tipo: Terminal T1 5 boarding areas
            if parts[0] == "Terminal":

                nombre_terminal = parts[1]

                # Creamos la terminal
                current_terminal = Terminal(nombre_terminal)

                # Cargamos las aerolíneas de esta terminal
                LoadAirlines(current_terminal, nombre_terminal)

                # Añadimos la terminal al aeropuerto
                bcn.terminal.append(current_terminal)

            # Línea tipo: Area A Schengen Gates 1 - 11
            elif parts[0] == "Area":

                if current_terminal == None:
                    return "Error | Area without terminal"

                nombre_area = parts[1]
                tipo_area = parts[2]

                gate_init = int(parts[4])
                gate_final = int(parts[6])

                # Creamos el nombre completo de la zona
                nombre_completo_area = current_terminal.name + "BA" + nombre_area

                # Creamos el área de embarque
                area = BoardingArea(nombre_completo_area)

                # Decidimos si es Schengen o no Schengen
                if tipo_area == "Schengen":
                    area.schengen = True
                else:
                    area.schengen = False

                # Creamos el prefijo de las gates
                prefix = nombre_completo_area + "G"

                # Creamos las gates de esta zona
                result = SetGates(area, gate_init, gate_final, prefix)

                if result == -1:
                    return "Error | Wrong gate numbers"

                # Añadimos el área a la terminal actual
                current_terminal.BoardingArea.append(area)

    return bcn



def GateOccupancy (bcn):
    lista = []
    Gate.occupancy = False
    t = 0
    while t < len(bcn.terminal):   #recorremos las terminales
        terminal = bcn.terminal[t]
        t = t+1 #pasamos a la siguiente terminal
        a = 0

        while a < len(terminal.BoardingArea): #recorremos las áreas de embarque
            area = terminal.BoardingArea[a]
            a = a+1 #pasamos a la siguiente zona de embarque
            g = 0

            while g < len(area.gate):  #recorremos las gates
                gate = area.gate[g]
                g = g+1  #pasamos a la siguiente gate

                #comprobamos el estado actual de esa gate:
                status = "free"
                if gate.occupancy == True:
                    status = "occupied"

                #guardamos los datos de esa gate en una variable:
                info_gate = [gate.name, status, gate.aircraft_id]
                lista.append (info_gate)

    return lista

def PlotGateOccupancy (bcn):
    info_gates = GateOccupancy (bcn) #llamamos la función anterior para tener una lista con todas las gates

    #creo dos contadores para saber el estado de las gates (libres o ocupdas)
    gates_free = 0
    gates_occupied = 0
    for i in range (len(info_gates)):
        gates = info_gates[i] #guarda los datos de la gate
        status = gates[1] #el estado de la gate se encuentra en la posición 1 de gates

        if status == "free":
            gates_free = gates_free + 1

        if status == "occupied":
            gates_occupied = gates_occupied + 1

    status = ["free", "occupied"]
    total = [gates_free, gates_occupied]
    colors = ['green', 'red']  #verde para las gates libres, rojo para las ocupadas

    fig, ax = plt.subplots(figsize=(18, 6))
    ax.clear()  #limpiamos por si había otro gráfico anterior
    ax.set_title ('Gate Occupancy - LEBL')
    ax.set_xlabel ('Gate Status')
    ax.set_ylabel ('Total Gates')
    ax.bar(status, total, color=colors)

    return fig

def IsAirlineInTerminal (terminal, name):
    found = False
    i = 0
    if name == "": #si el nombre de la aerolínea está vacío
        found = False
    while not found and i < len(terminal.airlines):
        if terminal.airlines[i] == name:
            found = True
        i = i + 1 #revisamos la siguiente aerolinea de la lista
    return found

def SearchTerminal (bcn, name):
    found = False
    t = 0
    terminal_name = ""
    while not found and t<len(bcn.terminal): #recorremos la lista
        terminal = bcn.terminal[t]
        if IsAirlineInTerminal(terminal, name):  #llamamos a la función anterior para saber si la aerolinea se encuentra en esta terminal
            found = True
            terminal_name = terminal.name #guardamos el nombre
        else:
            t = t+1

    return terminal_name

def AssignGate(bcn, aircraft):
    is_schengen = False
    if len(aircraft.ICAO) >= 2:
        dos_primers_digits = aircraft.ICAO[0] + aircraft.ICAO[1]

        #recorremos la lista
        s = 0
        while not is_schengen and s < len(lista_aerpuertos_schengen):
            if lista_aerpuertos_schengen[s] == dos_primers_digits:
                is_schengen = True
            else:
                s = s + 1

    #buscamos el nombre de la terminal donde opera la aerolínea
    t_name = SearchTerminal(bcn, aircraft.airline)
    if t_name == "":
        return "Error | No airline found"  #la aerolinea no opera en el aeropuerto

    #buscamos el objeto terminal que coincide con la aerolínea
    found = False
    t = 0
    while not found and t < len(bcn.terminal):
        if bcn.terminal[t].name == t_name:
            terminal_obj = bcn.terminals[t]
            found = True
        t = t + 1

    #buscamos una gate libre en las zonas de embarque de esa terminal
    occupied = False
    a = 0
    #recorremos las zonas de embarque de la terminal
    while not occupied and a < len(terminal_obj.boarding_areas):
        area = terminal_obj.boarding_areas[a]
        a = a + 1
        if area.type_area == is_schengen: #si la zona de embarque coincide con el tipo de vuelo
            g = 0
            #recorremos las gates de esa zona
            while not occupied and g < len(area.gates):
                gate = area.gates[g]

                #si la gate está libre, la asignamos
                if gate.occupancy == False:
                    gate.occupancy = True
                    gate.aircraft_id = aircraft.id
                    occupied = True
                else:
                    g = g + 1

    if occupied == True:
        return 0
    else:
        return "Error | No free gates found" #si no queda ninguna gate libre, retorna el error



