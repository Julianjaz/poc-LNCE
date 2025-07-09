class SolarPotencial:
    def __init__(self):
        pass

    def calculate(self, a, g_t, g, t2m):
        t_amb = t2m - 273.15 # t2m viene en k, se pasa a C
        noct = 45 # (CONSTANTE FICHA TECNICA)
        y = -0.410/100 # en la foto (CHAT DE MANU) estaba en porcentaje # (CONSTANTE FICHA TECNICA)
        h_mod = 16.48 # (CONSTANTE FICHA TECNICA)
        h_sis = 0.8 # (CONSTANTE FICHA TECNICA)
        t_cell=t_amb+((noct - 20 )/ 800 ) * g
        f_t=1 + y *( t_cell - 25 )
        s_potencial = a * g_t * 365 * h_mod * h_sis * f_t

        return s_potencial