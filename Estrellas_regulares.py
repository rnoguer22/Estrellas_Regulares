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
                angulo = (360/n) * i   # Formula para el angulo
        return angulo

    turtle.speed(0)       # Incrementamos la velocidad
    for _ in range (n):   # Con este bucle se nos genera la estrella
        turtle.right(calcular_angulo(n))  
        turtle.forward(200)
    turtle.exitonclick()
    
if __name__ == '__main__':
    n = int(input("Numero de puntas de la estrella: "))
    generar_estrella(n)