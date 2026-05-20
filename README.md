Video Versión 3: https://drive.google.com/file/d/1ILEaptebG5OZb5kcPvKmAzumrrlfNOuu/view?usp=sharing
# Airport Manager

Este proyecto es una aplicación en Python para gestionar información relacionada con aeropuertos, vuelos y gates del aeropuerto de Barcelona-El Prat (**LEBL**).

La idea empezó siendo bastante sencilla: cargar aeropuertos desde un archivo y trabajar con sus datos. Poco a poco el proyecto ha ido creciendo hasta convertirse en una herramienta con interfaz gráfica, gráficos, mapas y gestión básica de terminales y puertas de embarque.

---

## ¿Qué hace el proyecto?

Airport Manager permite cargar y analizar información de aeropuertos y vuelos de llegada a Barcelona.

Actualmente se pueden hacer cosas como:

- Cargar una lista de aeropuertos.
- Añadir y eliminar aeropuertos.
- Saber si un aeropuerto pertenece a la zona Schengen.
- Ver gráficos sobre aeropuertos y vuelos.
- Abrir mapas en Google Earth usando archivos KML.
- Cargar vuelos de llegada a LEBL.
- Ver cuántos vuelos hay por aerolínea.
- Diferenciar vuelos Schengen y no Schengen.
- Calcular vuelos de larga distancia.
- Cargar la estructura del aeropuerto de Barcelona.
- Gestionar terminales, zonas de embarque y gates.
- Buscar en qué terminal opera una aerolínea.
- Asignar gates automáticamente a los vuelos.

---

## Progreso del proyecto

### Primera parte: aeropuertos

Al principio creamos la base del proyecto con la clase `Airport`.

Cada aeropuerto guarda:

- Código ICAO
- Latitud
- Longitud
- Si es Schengen o no

También añadimos funciones para cargar aeropuertos desde un archivo, convertir coordenadas, añadir y eliminar aeropuertos, guardar aeropuertos Schengen y mostrar gráficos.

Esta parte fue importante porque nos sirvió para aprender a organizar mejor el código usando clases, listas y funciones.

---

### Segunda parte: vuelos

Después añadimos los vuelos de llegada a Barcelona.

Creamos una clase para representar cada avión, guardando:

- Identificador del avión
- Aerolínea
- Aeropuerto de origen
- Hora de llegada

Con esto el programa ya no solo trabajaba con aeropuertos, sino también con vuelos reales de un día completo.

Añadimos gráficos para ver los vuelos por aerolínea y para comparar vuelos procedentes de aeropuertos Schengen y no Schengen.

También añadimos el cálculo de distancias con la fórmula de Haversine, que sirve para detectar vuelos largos de más de 2000 km.

---

### Tercera parte: terminales y gates

En la versión más reciente hemos empezado a gestionar la estructura del aeropuerto de Barcelona-El Prat.

Ahora el programa puede trabajar con:

- Terminales
- Zonas de embarque
- Gates
- Aerolíneas asignadas a cada terminal

El objetivo de esta parte es que el programa pueda asignar automáticamente una gate a cada vuelo según la aerolínea, la terminal correspondiente y si el vuelo viene de una zona Schengen o no Schengen.

También hemos añadido una visualización de ocupación de gates para ver cuántas están libres y cuántas ocupadas.

---

## Interfaz gráfica

El proyecto tiene una interfaz hecha con **Tkinter** para que sea más fácil usar el programa.

Desde la interfaz se pueden cargar archivos, pulsar botones, ver mensajes y mostrar gráficos directamente en la ventana principal.

La interfaz está dividida en varias zonas:

- Gestión de aeropuertos
- Gestión de llegadas
- Visualizaciones
- Gestión de gates y terminales

La idea es que el usuario pueda usar el programa sin tener que tocar directamente el código.

---

T1_Airlines.txt         # Aerolíneas de la T1
T2_Airlines.txt         # Aerolíneas de la T2
mapAirports.kml         # Mapa generado para Google Earth
