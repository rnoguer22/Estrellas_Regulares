import turtle

def generar_estrella(n):
    angulo = 180 - (360/n)# Esto solo nos vale si n es multiplo de 4  :(
    turtle.speed(0)       # Incrementamos la velocidad
    for _ in range (n):   # Con este bucle se nos genera la estrella
        turtle.right(angulo)  
        turtle.forward(200)
    turtle.done()   # De esta manera no se cierra el archivo al acabar la ejecucion del programa

if __name__ == '__main__':
    n = int(input("Numero de puntas de la estrella: "))
    generar_estrella(n)