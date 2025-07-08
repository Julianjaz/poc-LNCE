class SolarPotencial:
    def __init__(self):
        pass

    def calculate(self, a, g_t, g, t2m):
        t_amb = t2m - 273.15
        s_potencial = 1
        noct = 45
        y = -0.410/100 # en la foto estaba en porcentaje
        h_mod = 16.48
        h_sis = 0.8
        t_cell=t_amb+((noct - 20 )/ 800 ) * g
        f_t=1 + y *( t_cell - 25 )
        s_potencial = a * g_t * 365 * h_mod * h_sis * f_t

        return s_potencial