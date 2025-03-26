from guerrero import Gerrero
from hechicero import Hechicero
from espada import Espada
from conjuro import Conjuro


#crear personajes
guerrero = Gerrero("Thorg",50)
hechicero = Hechicero("Merlin", 50)

#crear objetos 
espada = Espada("Espada de valor", 100)
conjuro = Conjuro("bola de fuego", 100)

#equipar objetos
guerrero.equipar_arma(espada)
hechicero.aprender_conjuro(conjuro)

#acciones del juego
guerrero.atacar(hechicero)
hechicero.lanzar_conjuro(guerrero)