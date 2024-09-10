import math
import time
import matplotlib.pyplot as plt

#A MODO DE ACLARACION: EN LA PRIMERA PARTE DE ESTE CODIGO SE IMPLEMENTAN SOLUCIONES FUNCIONALES PERO NO TAN EFICIENTES (COMO SE PRETENDÍA EN LA TAREA)
#LUEGO, COMO COMENTO EN EL CODIGO, IMPLEMENTO UNA SOLUCION CON LA CLASE DINAMICA Y EL DECORADOR. 

class CaminosPCB:

    def __init__(self, n, m):
        self.n = n
        self.m = m

    def contar_caminos_combinatoria(self):
    
        #calculamos el número de caminos usando combinatoria pues organizamos la manera en que distribuimos n-1 pasos en vertical y m-1 pasos en horizontal
        return math.comb(self.n + self.m - 2, self.n - 1)
    
    def contar_caminos_recursivo(self, i=0, j=0):

        #Si llegamos a la esquina inferior derehca, hemos encontrado un camino retornando "1" como camino encontrado
        if i == self.n - 1 and j == self.m - 1:
            return 1
        
        #si estamos fuera de los límites de la grilla, simplemente retornamos 0 para seguir con la recursión
        if i >= self.n or j >= self.m:
            return 0
        
        #Moverse hacia abajo o hacia la derecha
        return self.contar_caminos_recursivo(i + 1, j) + self.contar_caminos_recursivo(i, j + 1)
    
    def medir_tiempo_combinatoria(self):

        #Definimos localmente tiempo final y tiempo inicial y a través de .time() calculamos el tiempo del algoritmo (resta de tiempo final con el inicial)
        tiempo_inicial = time.perf_counter()
        resultado = self.contar_caminos_combinatoria()
        tiempo_final = time.perf_counter()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        return resultado, tiempo_ejecucion
    
    def medir_tiempo_recursivo(self):

        tiempo_inicial = time.perf_counter()
        resultado = self.contar_caminos_recursivo()
        tiempo_final = time.perf_counter()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        return resultado, tiempo_ejecucion

#Leyendo las instrucciones 2, 3, y 4, entendemos que programar metodos dentro de las clases para medir tiempo, claramente no es una manera 
#eficiente de conseguir lo pedido. Por lo que, considerando lo pedido en el punto 4, se implementa el sgte decorador:

#decorador para medir y almacenar el tiempo de ejecución
def medir_tiempo_y_almacenar(func):
    def wrapper(self, *args, **kwargs):
        tiempo_inicial = time.perf_counter()
        resultado = func(self, *args, **kwargs)
        tiempo_final = time.perf_counter()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        self.tiempos[func.__name__] = tiempo_ejecucion
        return resultado
    return wrapper

#Usando la misma clase que al inicio, realizaremos las modificaciones para agregar el método dinámico: 

class CaminosPCB:

    def __init__(self, n, m):
        self.n = n
        self.m = m

        #Creamos un diccionario para almacenar los tiempos
        self.tiempos = {}  

    @medir_tiempo_y_almacenar
    def contar_caminos_combinatoria(self):
        return math.comb(self.n + self.m - 2, self.n - 1)

    @medir_tiempo_y_almacenar
    def contar_caminos_recursivo(self, i=0, j=0):
        if i == self.n - 1 and j == self.m - 1:
            return 1
        if i >= self.n or j >= self.m:
            return 0
        return self.contar_caminos_recursivo(i + 1, j) + self.contar_caminos_recursivo(i, j + 1)

#Implementamos el método dinámico para recibir o el metodo combinatoria o recursivo. En caso de haber más soluciones, este metodo igualmente deberia funcionar
    def calcular_caminos(self, metodo='combinatoria'):
        if metodo == 'combinatoria':
            return self.contar_caminos_combinatoria()
        elif metodo == 'recursivo':
            return self.contar_caminos_recursivo()
        else:
            raise ValueError("Método no válido. Use 'combinatoria' o 'recursivo'.")

#implementamos un metodo para medir tiempo
    def imprimir_tiempos(self):
        for metodo, tiempo in self.tiempos.items():
            print(f"Tiempo de ejecución de {metodo}: {tiempo:.6f} segundos (con decorador)")


    #Creamos un metodo para graficar desempeño
    def tiempo_algoritmos(self, n_valores):
        #creamos lista para almacenar tiempos
        combinatoria_tiempos = []
        recursivo_tiempos = []

        for n, m in n_valores:
            self.n = n
            self.m = m
            #calculamos tiempo de la solucion combinatoria 
            self.calcular_caminos('combinatoria')
            combinatoria_tiempos.append(self.tiempos['contar_caminos_combinatoria'])

            #calculamos el tiempo de la solucion recursiva solo hasta 12x12 (le puse 16x16 y tardó mucho así que fui probando hacia abajo y hasta el 12x12 me parece que tiene tiempo
            #de ejecución razonable)
            if n <= 12 and m <= 12:
                self.calcular_caminos('recursivo')
                recursivo_tiempos.append(self.tiempos['contar_caminos_recursivo'])
            else:
                recursivo_tiempos.append(None)  

        #graficamos el desempeño
        #Ademas, consideramos que N y M aumentan por igual el tiempo de ejecución del algoritmo por lo que en notación Big(O) se tiene que n = N+M
        n_labels = [f"{n}x{m}" for n, m in n_valores]
        plt.plot(n_labels, combinatoria_tiempos, label='Combinatoria (O(1))')
        plt.plot(n_labels, recursivo_tiempos, label='Recursiva (O(2^(N+M)))', linestyle='--', marker='o')
        plt.xlabel('Tamaño de la grilla (NxM)')
        plt.ylabel('Tiempo de ejecución (segundos)')
        plt.title('Comparación de eficiencic entre soluciones (Notación O)')
        plt.legend()
        plt.tight_layout()
        # Guardar en formato SVG
        plt.savefig('CURVAS.svg', format='svg')
        plt.show()

    #creamos un metodo para imprimir resultados y tiempos (con decorador)
    def imprimir_resultados_y_tiempos(self):
        caminos_comb = self.calcular_caminos('combinatoria')
        print(f"Solución Combinatoria: {caminos_comb} (con metodo dinámico)")
        
        caminos_rec = self.calcular_caminos('recursivo')
        print(f"Solución Recursiva: {caminos_rec} (con metodo dinámico)")
        
        # Imprimir tiempos calculados con el decorador
        self.imprimir_tiempos()

#pruebas:

#consideramos el objeto con una cuadrícula 9x12
pcb = CaminosPCB(9, 12)

# Imprimir resultados y tiempos
pcb.imprimir_resultados_y_tiempos()

#Prueba con los tamaños definidos para el gráfico
n_valores = [(5, 5), (8, 8), (10, 10), (12, 12), (15, 15)]
pcb.tiempo_algoritmos(n_valores)

# Guardar en formato SVG
#plt.savefig('CURVAS.svg', format='svg')


#EL RISAS






