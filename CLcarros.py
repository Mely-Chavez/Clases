class carros:
    Placa="AAA-2636"
    Marca="Chebrolet"
    Modelo="219A"
    Velocidad="2km/h"
    Tamaño="Mediano"

    def correr(self):
        print("Carro encendido")
    def prender(self):
        print("No esta prendido")
    def color(self):
        return self.Modelo
    def el_color_es(self):
        if self.Modelo == "72367C":
            print("El color es negro")
        elif self.Modelo== "2":
            print("El color es azul")
        elif self.Modelo=="3":
            print("El color es Rojo")
automotris= carros()
automotris.modelo=="1872B"
automotris.color="Amarillo"
automotris.el_color_es()