from scipy.stats import weibull_min
import numpy as np


class WindPotencial:
    def __init__(self):
        pass

    def calculate(self, ps, t2m, v_wind, altura_buje, alpha,coef_friccion):

        ###### Organizar unidades ######
        k_ps = ps/1000

        ###### Corregir ######
        ps_corregida = k_ps / 101 #parametro es 101
        t2m_corregida= 288.1/t2m
        #altura_buje # ingresado por el usuario
        #alpha #opciones para que el usuario seleccione
        altura_medicion = 10 # hay dos tipos de alturas 10 y 50, dada en los datos
        correcion_por_altura = v_wind*(altura_buje/altura_medicion)**coef_friccion

        ###### distribucion de weibull ######
        beta = correcion_por_altura
        velocidades = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        potencias = [0.0, 0.0, 0.0, 0.004, 0.035, 0.072, 0.113, 0.151, 0.184, 0.21, 0.23, 0.244, 0.246, 
                     0.246, 0.251, 0.256, 0.26, 0.268, 0.27, 0.27, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                     0.0, 0.0, 0.0]# Ficha tecnica
        pdf = weibull_min.pdf(velocidades, c=alpha, scale=beta)

        ###### Calcular X #######
        suma_total = 0
        for i in range(len(pdf)):
          x = pdf[i]*potencias[i]
          suma_total += x 
        e_e = suma_total*8760

        print("==="*30)
        print("Variables wind")
        print("==="*30)
        print("k_ps:", k_ps)
        print("ps_corregida:", ps_corregida)
        print("t2m_corregida:", t2m_corregida)
        print("altura_medicion:", altura_medicion)
        print("correcion_por_altura o beta:", correcion_por_altura)
        print("pdf:", pdf)
        print("-----variables de entrada----")
        print("ps:", ps)
        print("t2m:", t2m)
        print("v_wind:", v_wind)
        print("altura_buje:", altura_buje)
        print("alpha:", alpha)
        print("coef_friccion:", coef_friccion)
        print("    ---Resultado----")
        print("    e_e:", e_e)
        print("----"*30)
        return e_e