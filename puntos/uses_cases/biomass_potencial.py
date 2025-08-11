class BiomassPotencial:
    def __init__(self):
        pass

    def agricultural_calculate(self, a_cultivo, rendimiento):


        n_e = 0.30 # constante del 30%
        pci = 14600 # TODO: este solo es el caso del aguacate, luego toca generar tabla de referencias
        fgr_agricola = 0.3 #TODO: solo para el aguacate, luego toca generar tabla de referencias
        mb = a_cultivo * rendimiento * fgr_agricola
        b_potencial = mb * pci * n_e
        print("==="*30)
        print("Variables biomasa")
        print("==="*30)
        print("n_e:", n_e)
        print("pci:", pci)
        print("fgr_agricola:", fgr_agricola)
        print("mb:", mb)
        print("-----variables de entrada----")
        print("a_cultivo:", a_cultivo)
        print("rendimiento:", rendimiento)
        print("  ---Resultado----")
        print("   b_potencial:", b_potencial)
        print("----"*30)
        return b_potencial
    

    def pecuario_calculate(self, cabezas):

        n_e = 0.30 # constante del 30%
        pci = 18895 # TODO: este solo es el caso de los bovinos, luego toca generar tabla de referencias
        fgr_pecuario = 7.99 #TODO: solo para bovinos, luego toca generar tabla de referencias
        mb = cabezas * fgr_pecuario
        b_potencial = mb * pci * n_e
        print("==="*30)
        print("Variables biomasa pecuario")
        print("==="*30)
        print("n_e:", n_e)
        print("pci:", pci)
        print("fgr_pecuario:", fgr_pecuario)
        print("mb:", mb)
        print("-----variables de entrada----")
        print("cabezas:", cabezas)
        print("  ---Resultado----")
        print("   b_potencial:", b_potencial)
        print("----"*30)
        return b_potencial