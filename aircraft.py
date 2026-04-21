from airport import *
import matplotlib.pyplot as plt
import math
lista_aerpuertos_schengen=['LO', 'EB', 'LK', 'LC', 'EK', 'EE', 'EF', 'LF', 'ED', 'LG', 'EH', 'LH',
'BI','LI', 'EV', 'EY', 'EL', 'LM', 'EN', 'EP', 'LP', 'LZ', 'LJ', 'LE', 'ES',
'LS']
class aircraft:
    def __init__(self, id, airline, ICAO, arrivaltime):
        self.id=id
        self.airline=airline
        self.ICAO=ICAO
        self.arrivaltime=arrivaltime


def LoadArrivals (filename):
    f = open(filename, 'r')
    lista_arrivals = []
    lineas = f.readlines()
    for i in range(1, len(lineas)):
        arrivals_por_lineas = lineas[i]
        elementos_arrivals = arrivals_por_lineas.split()
        id = elementos_arrivals[0]
        ICAO = elementos_arrivals[1]
        time = elementos_arrivals[2]
        airline= elementos_arrivals[3]

        arrival = aircraft(id, airline, ICAO, time)

        lista_arrivals.append(arrival)
    if len(lista_arrivals)==0:
        return "Error | No airports found"
    else:
        return lista_arrivals

def PlotArrivals (aircrafts):
    x_lista_airlines=[]
    y_contador_vuelos=[]
    encontrado = False
    b=0
    contador = 0
    for a in range(len(aircrafts)):
        airline_base=aircrafts[a].airline
        while not encontrado and b<len(x_lista_airlines):
            if x_lista_airlines[b]==airline_base:
                encontrado = True
            b+=1
        if not encontrado:
            x_lista_airlines.append(airline_base)
            for c in range(len(aircrafts)):
                airline=aircrafts[c].airline
                if airline==airline_base:
                    contador+=1
            y_contador_vuelos.append(contador)
        encontrado = False
        b=0
        contador = 0

    fig, ax = plt.bar(figsize=(18, 6))
    ax.set_title('Flights by airline')
    ax.set_xlabel('Airline')
    ax.set_ylabel('Number of flights')
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.bar(x_lista_airlines, y_contador_vuelos)

    return fig

def SaveFlights(aircrafts, filename):
    if len (aircrafts)==0:
        print("Error | No airports found")
        return
    f = open(filename, 'w')
    f.write('AIRCRAFT ORIGIN ARRIVAL AIRLINE\n')
    for i in range(0, len(aircrafts)):
        elemento_lista = aircrafts[i]
        f.write(elemento_lista.id + ' ' + elemento_lista.ICAO + ' ' + elemento_lista.arrivaltime + ' ' + elemento_lista.airline + '\n')
        #Falta hacer que si queda algún hueco vacío lo rellene con un 0 o un -(guión)
def PlotAirlines (aircrafts):
    x_lista_airlines=[]
    y_contador_vuelos=[]
    encontrado = False
    b=0
    contador = 0
    for a in range(len(aircrafts)):
        airline_base=aircrafts[a].airline
        while not encontrado and b<len(x_lista_airlines):  #Revisamos a ver si esta aerolinea está ya en la lista de aerolineas.
            if x_lista_airlines[b]==airline_base:
                encontrado = True
            b+=1
        if not encontrado:
            x_lista_airlines.append(airline_base)
            for c in range(len(aircrafts)):
                airline=aircrafts[c].airline
                if airline==airline_base:
                    contador+=1
            y_contador_vuelos.append(contador)
        encontrado = False
        b=0
        contador = 0

    plt.figure(figsize=(18, 6))
    plt.title('Flights by airline')
    plt.xlabel('Airline')
    plt.ylabel('Number of flights')
    plt.xticks(rotation=90, fontsize=8)
    plt.bar(x_lista_airlines, y_contador_vuelos)
    plt.tight_layout()
    plt.show()


def PlotFlightsType (aircrafts):
    if len (aircrafts)==0:
        return "Error | No airports found"
    #Definimos que vuelos tienen un origen schenghen:
    contadorSchengen=0
    contadorNoSchengen=len(aircrafts)
    x=[]
    y=[]
    for i in range (0, len(aircrafts)):
        es_schengen = False
        num = 0
        # Las dos primeras letras del ICAO del aeropuerto son:
        lista_ICAO = aircrafts[i].ICAO
        if len(lista_ICAO) < 2:
            return 'Error | Index '
        dos_primeros_digitos = lista_ICAO[0] + lista_ICAO[1]
        while es_schengen == False and num < len(lista_aerpuertos_schengen):
            if lista_aerpuertos_schengen[num] == dos_primeros_digitos:
                es_schengen = True
            else:
                num += 1
        if es_schengen:
            contadorSchengen+=1

    contadorNoSchengen= contadorNoSchengen-contadorSchengen
    y.append(contadorSchengen)
    y.append(contadorNoSchengen)
    x.append('Schengen')
    x.append('Non Schengen')
    plt.bar(x,y)
    plt.title('Flights from Schengen Airports')
    plt.ylabel('Number of Airports')
    plt.show()



def MapFlights(aircrafts):
    Airports = LoadAirports('Airports.txt')
    kml = open('routes.kml', 'w')
    kml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    kml.write('<Document>\n')

    for i in range(len(aircrafts)):
        ICAO = aircrafts[i].ICAO
        kml.write(' <Placemark>\n')
        kml.write(f' <name>Route {ICAO} - LEBL</name>\n')
        kml.write('   <LineString>\n')
        kml.write('    <altitudeMode>clampToGround</altitudeMode>\n')
        kml.write('    <extrude>1</extrude>\n')
        kml.write('    <tessellate>1</tessellate>\n')
        kml.write('    <coordinates>\n')

        encontrado = False
        n = 0
        while not encontrado and n < len(Airports):
            airport_name = Airports[n].ICAO
            airport_longitude = Airports[n].longitude
            airport_latitude = Airports[n].latitude
            if airport_name == ICAO:
                encontrado = True
            else:
                n += 1

        kml.write(f'    {airport_longitude},{airport_latitude}\n')
        kml.write('    2.0783333333,41.2969444444\n')
        kml.write('    </coordinates>\n')
        kml.write('   </LineString>\n')
        kml.write(' </Placemark>\n')

    kml.write('</Document>\n')
    kml.write('</kml>\n')
    kml.close()
    #Falta hacer que cambien de colores los que vienen de aeropuerto schengen y los que vienen de aeropuerto no schengen.

def HaversineDistance(lat1, lon1, lat2, lon2):
    radio_tierra = 6371

    # Pasamos de grados a radianes
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    lambda1 = math.radians(lon1)
    lambda2 = math.radians(lon2)

    # Diferencias
    delta_phi = abs(phi1 - phi2)
    delta_lambda = abs(lambda1 - lambda2)

    # Fórmula de Haversine
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radio_tierra * c

    return d

def LongDistanceArrivals(aircrafts):
    Airports = LoadAirports('Airports.txt')
    Long_flights = []
#Calculamos la distancia con la longitud y la latitud.
    for i in range(len(aircrafts)):
        aircraft= aircrafts[i]
        encontrado = False
        ICAO = aircrafts[i].ICAO
        n = 0
        while not encontrado and n < len(Airports):
            airport_name = Airports[n].ICAO
            airport_longitude = Airports[n].longitude
            airport_latitude = Airports[n].latitude
            if airport_name == ICAO:
                encontrado = True
            else:
                n += 1
        if encontrado == False:
            return 'Error | Missmatch'
        distance = HaversineDistance(airport_latitude, airport_longitude, 41.2969444444, 2.0783333333)
        if distance > 2000:
            Long_flights.append(aircraft)

    return Long_flights






