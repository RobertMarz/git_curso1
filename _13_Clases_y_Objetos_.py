print("PROGRAMACION ORIENTADA A OBJETOS-CLASES Y OBJETOS     ")
print("*******************************************************/n")

class Persona:
    # atributos
    nombre = "Robert"
    edad = 24
    
    # metodos
    def camina(self):
        print(self.nombre + " está caminando")
        
    def duerme(self):
        print(self.nombre + " esta durmiendo")
        
        
 # A partir de una clase se pueden crear tantas objetos como se desee.
 # Los objetos de una clase se conocen como instancias
 #  Cada objeto contiene los atributos y métodos de la clase y podrá asignara esos atributos unos valores concretos. 
 # Esto se conoce como el estado de un objeto.  
 
p1 = Persona() # la variable p1 contiene un objeto de la clase Persona
p2 = Persona() # la variable p1 contiene un objeto de la clase Persona
p1.camina()
p2.duerme()
print(p1.nombre)
print(p2.nombre)
#print(p1.edad)
print("=========================EJERCICIO ANTERIOR Rob camina=========================")
PARAR = input("Presiona la tecla enter")
# Una función dentro de una clase se conoce como método 
# método especial _init__ conocido como constructor 
# y que sirve para inicializar un objeto.

class Persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        
    def camina(self):
        print(self.nombre + " "+ self.apellidos+ " está caminando muy rapido")
        
        
p1 = Persona("Robert", "Marziliano", 62)
p1.camina()
print(p1.nombre)
print(p1.apellidos)
print(p1.edad)

print("=========================EJERCICIO ANTERIOR Rob Apell =========================")
PARAR = input("Presiona la tecla enter")
# Atributos de clase vs Atributos de instancia
# Los atributos definidos dentro del constructor se conocen como atributos de instancia
# los atributos definidos dentro de la clase pero fuera del constructor se llaman como Atributes de clase.
# La principal diferencia es que un atributto de clase puede ser accedido aunque no existan instancias
# de la clase. Además, si se modifica su valor, se modificará el valor en todas las instancias existentes
# de dicha clase

class Demo:
    atrib_estatico = 123 # compartido por todos los objetos atributo de clase se puede modificar
    def __init__(self,numero):
        self.atrib_instancia = numero # específico de cada objeto
        
c1 = Demo(456)
c2 = Demo(789)

print("C1: Estatico {0} - Instancia: {1}".format(c1.atrib_estatico, c1.atrib_instancia))
# output: C1: Estatico 123 - Instancia: 456
print("C2: Estatico {0} - Instancia: {1}".format(c2.atrib_estatico, c2.atrib_instancia))
# output: C2: Estatico 123 - Instancia: 789

Demo.atrib_estatico = -1
print("C2: Estatico {0} - Instancia: {1}".format(c2.atrib_estatico, c2.atrib_instancia))

# output: C2: Estatico -1 - Instancia: 456
print("C2: Estatico {0} - Instancia: {1}".format(c2.atrib_estatico, c2.atrib_instancia))

# output: C2: Estatico -1 - Instancia: 789
c1.atrib_instancia = 999
print("C1: Estatico {0} - Instancia: {1}".format(c1.atrib_estatico, c1.atrib_instancia))
# output: C1: Estatico -1 - Instancia: 999

print("C2: Estatico {0} - Instancia: {1}".format(c2.atrib_estatico, c2.atrib_instancia))
# output: C2: Estatico -1 - Instancia: 789  
            
print("===========EJERCICIO ANTERIOR Aributo de clasess y A de Instancia================")
PARAR = input("Presiona la tecla enter")             
# Private y protected -----------------------
# A diferencia de otros lenguajes de Programación Orientada a Objetos, todos los métodos y atributos
# en Python son públicos. Es decir, no es posible definir una variable como private o protected

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre # atributo protected
        self.__edad = edad # atributo privat
        
# Herencia
# La herencia es una técnica de OOP 
# clase hija o subclase - hereda todos los métodos y propiedades 
# de otra clase (conocida como padre o clase base)
# Veamos

print("EJEMPLO DE HERENCIA")

print("===========EJERCICIO ANTERIOR Private y protected ================")
PARAR = input("Presiona la tecla enter")

class Dispositivo:
    def __init__(self,identificador,marca,tipo):
        self.identificador = identificador
        self.marca = marca
        self.tipo = tipo
    def conectar(self):
        print("¡Conectado!")
              


# la clase base se indica entre paréntesis
class Teclado(Dispositivo):
    def __init__(self,identificador,marca,tipo):
        # llamada al constructor del padre
        Dispositivo.__init__(self,identificador,marca,tipo)
        self.marca = marca
        self.tipo = tipo
        # metodo de la subclase
    def pulsar_tecla(self,tecla):
        print(tecla)

t1 = Teclado("0001", "Logitech", "AZERTY")
t1.conectar()
t1.pulsar_tecla("a")

# Herencia múltiple
# Python soporta la herencia múltiple, es decir, heredad métodos y atributos de más de un padr

# en caso de conflicto Dispositivo tendrá prioridad sobre Periférico
class Periferico:
    def __init__(self,identificador,marca):
        self.identificador = identificador
        self.marca = marca
    def conectar(self):
        print("¡Conectado!")
        
        
#class Teclado(Dispositivo, Periferico):
    # cuerpo de la clase
    
print("===========EJERCICIO ANTERIOR HERENCIA ================")
#PARAR = input("Presiona la tecla enter")