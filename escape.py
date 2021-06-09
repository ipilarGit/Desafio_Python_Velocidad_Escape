import sys
import math

print("\n               Gravedad y radio de los Planetas")
print("-----------------------------------------------------------------------")
print("Planeta Tierra   : (gravedad) g = 9.8   m/s^2  y (radio) r = 6371    km")
print("Planeta Mercurio : (gravedad) g = 3.7   m/s^2  y (radio) r = 2439.7  km")
print("Planeta Marte    : (gravedad) g = 3.721 m/s^2  y (radio) r = 3397.2  km")
print("Planeta Urano    : (gravedad) g = 8.87  m/s^2  y (radio) r = 25559   km")
print("Planeta Venus    : (gravedad) g = 8.87  m/s^2  y (radio) r = 6051.8  km")
print("Planeta Saturno  : (gravedad) g = 10.44 m/s^2  y (radio) r = 60268   km")
print("Planeta Jupiter  : (gravedad) g = 24.79 m/s^2  y (radio) r = 71492   km")
print("Planeta Neptuno  : (gravedad) g = 11.15 m/s^2  y (radio) r = 24746   km")
print("Planeta Plutón   : (gravedad) g = 0.62  m/s^2  y (radio) r = 1160    km")
print("-----------------------------------------------------------------------\n")

argumentos=len(sys.argv)
if argumentos == 3:
    gravedad = float(str(sys.argv[1]))
    radio = float(str(sys.argv[2]))
    radio = 1000 * radio # conversion de 1 km = 1000 metros
    velocidad_escape = math.sqrt(2 * gravedad * radio ) 
    print ("La velocidad de escape es: {0:.2f} m/s aprox.".format(velocidad_escape))
else:
    print("ERROR: Intodujo (1) ó (2) argumentos.")
    print("SOLUCION: Intoduce los argumentos correctamente.")
    print("\nPara determinar la Velocidad de Escape, escribe por consola:")
    print("$ python escape.py valor_gravedad valor_radio")
