from scipy.stats import weibull_min
import numpy as np


class WindPotencial:
    def __init__(self):
        pass

    def calculate(self, ps, t2m, v_wind, altura_buje, alpha,coef_friccion):

        ###### Organizar unidades ######
        k_ps = ps/1000

        ###### Corregir ######
        ps_corregida = k_ps / 101
        t2m_corregida= 288.1/t2m
        #altura_buje # ingresado por el usuario
        #alpha #opciones para que el usuario seleccione
        altura_medicion = 10 # hay dos tipos de alturas 10 y 50, dada en los datos
        correcion_por_altura = v_wind*(altura_buje/altura_medicion)**coef_friccion

        ###### distribucion de weibull ######
        beta = correcion_por_altura
        velocidades = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        potencias = [0.000, 0.000 ,0.000, 16.000, 113.000, 261.000, 
                     448.000, 741.000, 1119.000, 1577.000, 1901.000, 
                     1986.000, 2000.000, 2000.000, 2000.000, 2000.000, 
                     2000.000, 2000.000, 2000.000, 2000.000, 2000.000, 
                     2000.000, 2000.000, 0.000, 0.000, 0.000] # Ficha tecnica
        pdf = weibull_min.pdf(velocidades, c=alpha, scale=beta)

        ###### Calcular X #######
        suma_total = 0
        for i in range(len(pdf)):
          x = pdf[i]*potencias[i]
          suma_total += x 
        e_e = suma_total*8760
        return e_e