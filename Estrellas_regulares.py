import turtle

def generar_estrella(n):
    
    def calcular_angulo():
        angulo = 0
        if n % 4 == 0:
            angulo = 180 - (360/n)   # Angulo si n es multiplo de 4
        elif n % 3 == 0:
            angulo = (360/n) + 120   # Angulo si n es multiplo de 3
        else:
            pass   # El angulo es 0 si ninguna de las condiciones es cierta, por lo que se dibujara una linea recta
        return angulo

    turtle.speed(0)       # Incrementamos la velocidad
    for _ in range (n):   # Con este bucle se nos genera la estrella
        turtle.right(calcular_angulo())  
        turtle.forward(200)
    turtle.done()   # De esta manera no se cierra el archivo al acabar la ejecucion del programa

if __name__ == '__main__':
    n = int(input("Numero de puntas de la estrella: "))
    generar_estrella(n)