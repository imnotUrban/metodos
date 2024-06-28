class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
    
    def acelerar (self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        self.velocidad -= decremento

    def obtener_velocidad(self):
        return self.velocidad


mi_auto = Auto("Ford", "Mustang", "Rojo")
print(f"Marca: {mi_auto.marca}, Modelo: {mi_auto.modelo}, Color: {mi_auto.color}")

mi_auto.acelerar( 20)
print(f"Velocidad actual: {mi_auto.obtener_velocidad()} km/h")

mi_auto.frenar(10 )
print(f"Velocidad actual: {mi_auto.obtener_velocidad()} km/h")
