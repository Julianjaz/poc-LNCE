class BiomassPotencial:
    def __init__(self):
        pass

    def calculate(self, a_cultivo, rendimiento):


        n_e = 0.30*100 # constante del 30%
        pci = 14600 # TODO: este solo es el caso del aguacate, luego toca generar tabla de referencias
        fgr_agricola = 0.3 #TODO: solo para el aguacate, luego toca generar tabla de referencias
        mb = a_cultivo * rendimiento * fgr_agricola
        b_potencial = mb * pci * n_e
        return b_potencial