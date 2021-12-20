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
    turtle.exitonclick()
    
if __name__ == '__main__':
    n = int(input("Numero de puntas de la estrella: "))
    generar_estrella(n)