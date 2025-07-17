class WaterPotencial:
    def __init__(self):
        pass

    def calculate(self, q, nivel):
        p = 1000 # Densidad del agua 
        g = 9.81 # Aceleración de la gravedad
        #q # Caudal ingresado por el usuario
        #hg # usuario opciones
        h_hydr = 0.02 #Pérdidas hidráulicas(CONSTANTE YA DEFINIDA SE TOMA VALOR MEDIO)
        h_tail = 0.75 # Pérdidas  descarga (CONSTANTE YA DEFINIDA SE TOMA VALOR MEDIO)
        et = 0.845 #TODO: DEBE SER PORCENTAJE #Eficiencia de la turbina (CONSTANTE YA DEFINIDA SE TOMA VALOR MEDIO)
        eg = 0.945 #TODO: DEBE SER PORCENTAJE #Eficiencia de la generador (CONSTANTE YA DEFINIDA SE TOMA VALOR MEDIO)
        t_trans = 0.0075 #Pérdidas del transformador  (CONSTANTE YA DEFINIDA SE TOMA VALOR MEDIO)
        l_para = 0.075 #Pérdidas por parada o inactividad de la planta (CONSTANTE YA DEFINIDA SE TOMA VALOR MEDIO)

        if nivel =="muy_baja":
            hg = 1
        elif nivel == "baja":
            hg = 5
        elif nivel == "media":
            hg = 15
        elif nivel == "alta":
            hg = 20

        print("caudal",q)

        e_gen =  p*g*q*(hg-(h_hydr+h_tail))*et*eg*(1-t_trans)*(1-l_para)*8760

        return e_gen/1000
    