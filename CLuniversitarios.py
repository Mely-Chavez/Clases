class Universitario:
    ID = 10001
    edad=20
    carrera="Tics"
    promedio=9
    grupo="A"

    def asistencia(self):
        print("Si asiste a clases")
    def atencion_a_clase(self):
        print("Muy estudiosa")
    def que_promedio_lleva(self):
        return self.promedio
    def aprobo_o_reprobo(self):
        if self.promedio > 7:
            print("Aprobo la materia")
        else: 
            print("Reprobo")
paola=Universitario()
paola.asistencia()
paola.edad=22
print(paola.edad)
paola.promedio=5