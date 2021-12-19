import turtle

def generar_estrella(n):
    angulo = 180 - (360/n)
    for _ in range (n):
        turtle.right(angulo)
        turtle.forward(200)

if __name__ == '__main__':
    n = int(input("Numero de puntas de la estrella: "))
    generar_estrella(n)