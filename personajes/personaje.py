class Personaje:
    def __init(self,nombre,salud):
        self.nombre = nombre
        self.salud = salud

    def recibir_danio(self,cantidad):
        self.salud-=cantidad
        print(f"{self.nombre} ha recibidp {cantidad} de daño. salud restante: {self.salud}")