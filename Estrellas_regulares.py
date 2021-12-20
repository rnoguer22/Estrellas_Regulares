import turtle

def generar_estrella(n):

    def mcm(num1,num2):  # Funcion para calcular el minimo comun multiplo de dos numeros
        multiplos_num1=[]  
        multiplos_num2=[]
        multiplos_comunes = [] 
        for i in range(1, num1*num2+1):  
            multiplos_num1.append(i*num1)  # Añadimos a la lista todos los multiplos del primer numero
            multiplos_num2.append(i*num2)  # Añadimos a la lista todos los multiplos del segundo numero
        for num in multiplos_num1:
            if num in multiplos_num2:           # Para cada numero en multiplos_num1, si esta tambien en
                multiplos_comunes.append(num)   # multiplos_num2, lo añadimos a la lista multiplos_comunes
        return min(multiplos_comunes)   # Devuelve el numero mas pequeño de los multiplos comunes

    def calcular_angulo(n):
        angulo = 0   # Definimos el angulo, el cual cambiaremos a continuacion
        for i in range (n // 2,1,-1):
            if mcm(n, i) == n*i:
                angulo = (360/n) * i   # Formula para el angulo de giro
        return angulo

    if n == 5:
        turtle.title("Estrella del Winter Soldier")
    else:
        turtle.title("Estrella de {} puntas".format(n))   # Titulo del archivo

    turtle.speed(5)       # Incrementamos la velocidad
    turtle.hideturtle()   # De esta manera desaparece el puntero
    turtle.color("red", "red")   
    turtle.begin_fill()
    
    for _ in range (n):   # Con este bucle se nos genera la estrella
        turtle.right(calcular_angulo(n))  
        turtle.forward(200)

    turtle.end_fill()
    turtle.exitonclick()  # Salimos haciendo un simple click
    
if __name__ == '__main__':
    
    # Introducimos un bucle para que el codigo tenga sentido
    while True:   
        n = input("Numero de puntas de la estrella: ")
        try:
            n = int(n)
            if n <= 4:
                print ("Solo hay estrellas de 5 o mas puntas tonto")
            else:
                break
        except:
            print("Introduce un numero entero por favor")
            pass
    
    generar_estrella(n)