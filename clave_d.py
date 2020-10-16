import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""
number1 = 2
number2 = 4
number3 = 3

# start-->
def multiplicar():
    result = number1 * number2 * number3
    return result


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""

# start-->
def sumaDivTresYCincoPlus():
    result = 0
    i = 1000
    while 1000<=i<=2000:
        if (i % 3 == 0) and (i % 5 == 0):
            result += i
            i+=1 
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->

def definicionOrtoedro(self):
        OrtoedroDic = {"area":obtenerArea(), "volumen":obtenerVolumen()}
        result = OrtoedroDic
        return result


longitud = 10
latitud = 6
altura = 5

def obtenerArea():
    result = float((2)*((longitud*latitud)+(longitud*altura)+(latitud*altura)))
    return result


def obtenerVolumen():
    result = float(longitud*latitud*altura)
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def __init__(self,longitud,latitud,altura):
        self.longitud = longitud
        self.latitud = latitud
        self.altura = altura

    def definicionOrtoedro(self):
        OrtoedroDic = {"area":area(), "volumen":volumen()}
        result = OrtoedroDic
        return result

    def area(self):
        result = float(2*((longitud*latitud)+(longitud*altura)+(latitud*altura)))
        return result

    def volumen(self):
        result = float(longitud*latitud*altura)
        return result

"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def __init__(self):
        self.computadora = []

    def orden(self,procesador,ram,tarjeta_grafica,ssd,costo):
           self.orden

    def totalProcesadorIntel(self):
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/Elida2000/Examen_parcial.git"
