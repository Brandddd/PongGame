from tkinter import font
import turtle

#VENTANA:
ventana = turtle.Screen() #Declaracion de la variable tipo ventana
ventana.title("Pong Game por Brandon David Palacio Alvarez. ") #Nombre del titulo de la ventana
ventana.bgcolor("black") #Color del fondo 
ventana.setup(width= 800, height= 600) #Tamaño de ventana
ventana.tracer(0) #Hace que se vea todo más fluido

#Marcador:
marcador1 = 0
marcador2 = 0

#Jugador 1:
jugador1 = turtle.Turtle() #Crear Figura en el modulo Turtle
jugador1.speed(0)   #Aparece de manera instantanea
jugador1.shape("square")   #Forma del jugador u objeto
jugador1.color("white")    #Color del jugador u objeto
jugador1.penup()           #Evitar que se cree una linea en el rastro del objeto
jugador1.goto(-350,0)      #Posicion inicial del jugador 1
jugador1.shapesize(stretch_wid=5,stretch_len=0.5)   #Tamaño del jugador u objeto

#Jugador 2:
jugador2 = turtle.Turtle() #Crear Figura en el modulo Turtle
jugador2.speed(0)   #Aparece de manera instantanea
jugador2.shape("square")   #Forma del jugador u objeto
jugador2.color("white")    #Color del jugador u objeto
jugador2.penup()           #Evitar que se cree una linea en el rastro del objeto
jugador2.goto(350,0)      #Posicion inicial del jugador 2
jugador2.shapesize(stretch_wid=5,stretch_len=0.5)   #Tamaño del jugador u objeto

#Pelota:
pelota = turtle.Turtle() #Crear Figura en el modulo Turtle
pelota.speed(0)   #Aparece de manera instantanea
pelota.shape("circle")   #Forma del jugador u objeto
pelota.color("red")    #Color del jugador u objeto
pelota.penup()           #Evitar que se cree una linea en el rastro del objeto
pelota.goto(0,0)      #Posicion inicial del objeto
pelota.shapesize(stretch_wid=0.75,stretch_len=0.75)   #Tamaño del jugador u objeto
#Mover pelota:
pelota.dx = 0.5        #Cambio en X cada 3 pixeles.
pelota.dy = 0.5        #Cambio en y cada 3 pixeles. 

#Linea de la mitad:
division = turtle.Turtle() #Crea figura en el modulo turtle
division.color("white")    #Color de la figura
division.goto(0,400)       #Posicion
division.goto(0,-400)      #Posicion

#Texto de jugadores:
pen = turtle.Turtle()
pen.speed(0)
pen.color ("lightgrey")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0                  Player 2: 0 ", align="center", font=("Lucida Console", 20, "normal"))

#Funciones para dar movimiento a los jugadores
def jugador1Arriba ():     #Funcion que me va mover jugador hacia arriba
    y = jugador1.ycor()    #Obtencion de la coordeanada del jugador
    y += 20                #Cada que se aumenta la Y en positivo se va hacia arriba
    jugador1.sety(y)       #Actualiza la coordenada en el eje Y

def jugador1Abajo ():     #Funcion que me va mover jugador hacia arriba
    y = jugador1.ycor()    #Obtencion de la coordeanada del jugador
    y -= 20                #Cada que se aumenta la Y en positivo se va hacia arriba
    jugador1.sety(y)       #Actualiza la coordenada en el eje Y

def jugador2Arriba ():     #Funcion que me va mover jugador hacia arriba
    y = jugador2.ycor()    #Obtencion de la coordeanada del jugador
    y += 20                #Cada que se aumenta la Y en positivo se va hacia arriba
    jugador2.sety(y)       #Actualiza la coordenada en el eje Y

def jugador2Abajo ():     #Funcion que me va mover jugador hacia arriba
    y = jugador2.ycor()    #Obtencion de la coordeanada del jugador
    y -= 20                #Cada que se aumenta la Y en positivo se va hacia arriba
    jugador2.sety(y)       #Actualiza la coordenada en el eje Y

#Conectar teclado al programa:
ventana.listen()      #Escucha que esta pasando dentro de ella (Eventos)
ventana.onkeypress(jugador1Arriba, "w")   #Evento que captura al momento de presionar la tecla.
ventana.onkeypress(jugador1Abajo, "s") 
ventana.onkeypress(jugador2Arriba, "Up") 
ventana.onkeypress(jugador2Abajo, "Down") 

while True:   #Bucle principal para evitar que la ventana se cierre automaticamente tan pronto se ejecute e juego
    ventana.update()

    pelota.setx(pelota.xcor() + pelota.dx)     #Aumentando coordenada X de la pelota por los 3 pixeles definidos arriba
    pelota.sety(pelota.ycor() + pelota.dy)     #Aumentando coordenada X de la pelota por los 3 pixeles definidos arriba


    #Bordes:
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1
    
    #Bordes derecha/izquierda:
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1         #Hace que la pelota cuando pierde se vaya en direcciones invertidas
        marcador1 += 1
        pen.clear()             #Evita que se sobreescriba los datos impresos en pantalla
        pen.write("Player 1: {}                  Player 2: {} ".format(marcador1,marcador2), align="center", font=("Lucida Console", 20, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1         #Hace que la pelota cuando pierde se vaya en direcciones invertidas
        marcador2 += 1
        pen.clear()             #Evita que se sobreescriba los datos impresos en pantalla
        pen.write("Player 1: {}                  Player 2: {} ".format(marcador1,marcador2), align="center", font=("Lucida Console", 20, "normal"))

    #Condiciones para el choque con las barras jugador 1 y jugador 2:
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < jugador2.ycor() + 50 and pelota.ycor() > jugador2.ycor() - 50):
        pelota.dx *= -1

    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < jugador1.ycor() + 50 and pelota.ycor() > jugador1.ycor() - 50):
        pelota.dx *= -1
