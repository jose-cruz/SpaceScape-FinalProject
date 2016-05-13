#Jose Alejandro Cruz, 09368
#Roberto Moreno, 09868
#16-11-10
#Programacion Orientada a Objetos
#Proyecto 3

#Importamos todos los modulos que necesitamos para este proyecto. 
from Tkinter import* #Este modulo nos sirve para los graficos del proyecto.
from math import * #Este modulo nos sirve para todas las operaciones matematicas que no incluye python stock.
import time #Importamos el tiempo, el cual nos permite las operaciones que incluyen algo realcionado con tiempo.
from tkMessageBox import * #Este modulo nos sirve para los mensajes en las cajas.
from random import * #Importamos random para los 'power-ups' del proyecto.

    
#Definimos las variables que necesitamos.
aceleracion = 0
velocidad = 0
angulo = 0
vidas = 5
nivel = 1
count = 0.0
puntos = 0
deltaA = 0
j = True
color_timer = True
chose_token = 0
ficha = 0
highscore=0
validez=True

#Esta funcion nos sirve para crear la pantalla del juego, instancear
#los objetos (el fondo y la nave).
def empezar_juego():
    #Globalizamos las variables necesarias en esta funcion.
    global pantalla, nave, fondo, label, vidas_l, puntos_l
    #Removemos los objetos instanceados en el programa principal (el menu).
    menu.pack_forget()
    titulo.pack_forget()
    start.pack_forget()

    inst.pack_forget()
    #Y creamos los nuevos objetos para la pantalla de juego.
    #Para empezar importamos las imagenes necesarias, la nave el fondo.
    nave=PhotoImage(file='nave.gif')
    fondo=PhotoImage(file='fondo.gif')
    #Luego para darle el tamaño correcto al canvas donde tendremos a la
    #nave y el fondo, implementamos el metodo "width()" y "height()".
    imagenx = fondo.width()
    imageny = fondo.height()
    #Instanceamos la pantalla de juego, como un canvas q esta dentro de
    #la pantalla principal. Usamos el tamaño de la imagen para el tamaño
    #del cavas .
    pantalla = Canvas(window, height=imageny, width=imagenx, bg='black')
    #Implementamos el label del contador de tiempo. Empezando con 10.0,
    #debido a que se tienen 10 segundos en el primer nivel.
    label = Label(window, height=800, width=5, text='10.0', bg='black', fg='white', font=("Helvetica", 30))
    #Implementamos el contador de vidas, empezando con 5 vidas.
    vidas_l = Label(window, height= 800, width=5, text=str(vidas), bg='black', fg='white', font=("Helvetica", 30))
    #Implementamos el contador de puntos, empezando con 0.
    puntos_l = Label(window, width=57, text = str(puntos), bg='black', fg='white')
    #Los llamamos para que aparezcan en la ventana principal
    label.pack(side=LEFT)
    vidas_l.pack(side=RIGHT)
    puntos_l.pack(side=TOP)
    pantalla.pack()
    #Y por ultimo, usamos el metodo creado "jugar()" para empezar el juego.
    validez=True
    jugar()

#Creamos el menu de instrucciones con esta funcion. 
def instrucciones():
    #Primero hacemos que olvide las instancias de los objetos creados
    #en el menu principal.
    menu.pack_forget()
    titulo.pack_forget()
    start.pack_forget()
    inst.pack_forget()

    #Luego instanceamos los objetos para el menu de instrucciones.
    inst_menu.pack()
    read_me.pack()
    botones.pack()
    botones.create_image(0, 0, image=img_bot, anchor=NW)
    back_menu.pack(side=LEFT)    

#Esta definicion la utilizamos para regresar del menu de instrucciones
#al menu principal.
def inst_to_menu():
    #Primero hacemos que olvide las instancias del menu de instrucciones.
    inst_menu.pack_forget()
    read_me.pack_forget()
    botones.pack_forget()
    back_menu.pack_forget()
    #Luego instanceamos los objetos del menu principal.
    menu.pack()
    titulo.pack()
    start.pack(side=LEFT)
    inst.pack(side=RIGHT)

#En esta definicion regresamos al menu principal, del juego, ya sea que
#Haya ganado o perdido el usuario.
def regresar_menu():
    #Desligamos las teclas de las funciones para evitar errores.
    window.unbind('<Up>')
    window.unbind('<Down>')
    window.unbind('<Right>')
    window.unbind('<Left>')
    #Primero borramos las imagenes importadas en para el juego.
    pantalla.delete('nave')
    pantalla.delete('mundo')
    #Luego hacemos que olvide las instancias del juego.
    pantalla.pack_forget()
    label.pack_forget()
    vidas_l.pack_forget()
    puntos_l.pack_forget()
    #Y por ultimo instanceamos los objetos del menu principal. 
    menu.pack()
    titulo.pack()
    start.pack(side=LEFT)
    inst.pack(side=RIGHT)

def reiniciar():
    #Primero borramos las imagenes importadas en para el juego.
    pantalla.delete('nave')
    pantalla.delete('mundo')
    #Luego hacemos que olvide las instancias del juego.
    #Desligamos las teclas de las funciones para evitar errores.
    window.unbind('<Up>')
    window.unbind('<Down>')
    window.unbind('<Right>')
    window.unbind('<Left>')
    jugar()
    
#Con esta funcion empezamos el timer del juego. 
def start_timer():
    #Globalizamos las variables necesarias para esta funcion.
    global count, color_timer
    #Cambiamos el texto de "label" por el tiempo que queda.
    label['text'] = str(count)
    #Para hacer mas dinamico el reloj, implementamos un cambio de color,
    #de rojo a blanco, cada milesima que el tiempo avanza.
    if color_timer == True:
        #Cambiamos el color del texto a rojo.
        label.config(fg='red')
        #Cambiamos el valor de "color_timer" a falso para la el siguiente
        #cambio de color.
        color_timer = False
    else:
        #Cambiamos el color del texto a rojo.
        label.config(fg='white')
        #Cambiamos el valor de "color_timer" a falso para la el siguiente
        #cambio de color. 
        color_timer = True
    #Damos un tiempo de sleep, de 0.1 seg, para actualizar despues el nuevo
    #tiempo.
    time.sleep(0.1)
    window.update()
    count -= 0.1
    #Entramos en esta definision para evaluar que el tiempo no se a
    #acabado.
    time_over()

#En esta definicion subimos la aceleracion de la nave.
def subir_ace(event):
    #Globalizamos todas las variables necesarias en esta funcion.
    global aceleracion, deltaA
    #Definimos los cambios de aceleracion segun los power-ups.
    if deltaA == 0:
        if aceleracion < 10:
            aceleracion += 2
    elif deltaA == 1:
        if aceleracion < 10:
            aceleracion += 3
    elif deltaA == 2:
        if aceleracion < 10:
            aceleracion += 1
    #Y por ultimo llamamos a la funcion "move()", para que la nave avanze.
    move()

#Con esta funcion bajamos la aceleracion de la nave.
def bajar_ace(event):
    #Globalizamos todas las variables necesarias en esta funcion.
    global aceleracion, chose_token
    #Bajamos la aceleracion de la nave por 1. 
    if aceleracion > 0:
        aceleracion -=1
    #Y por ultimo llamamos a la funcion "move()" para actualizar el
    #movimiento de la nave.
    move()

#Con esta funcion hacemos que la nave gire sobre su eje a la derecha,
#y de esta manera, cambia el movimiento de ella.
def girar_derecha(event):
    #Globalizamos todas las variables necesarias en esta funcion.
    global angulo, nave
    #Le sumamos 1/12*pi, para cambiar el angulo.
    angulo += (1/12.0)*pi
    #Utilizamos el metodo "coords()" de Tkinter para obtener las
    #coordenadas de la nave. Este metodo nos devuelve una lista con las
    #dos coordenadas.
    c = pantalla.coords('nave')
    #Asignamos una variable a cada una de estas coordenadas.
    x = c[0]
    y = c[1]
    #Para que la nave se mueva segun su angulo, debemos definir el seno
    # coseno de este para incluirlo en la velocidad en 'x' y en 'y' de
    #la nave. Para esto importamos el modulo de matematica.
    coseno = round(cos(angulo), 3)
    seno = round(sin(angulo), 3)
    #Por ultimo, llamamos al metodo que corregira la posicion de la figura
    #de la nave.
    lado_nave(coseno, seno, x, y)

#Con esta funcion hacemos que la nave gire sobre su eje a la izquierda,
#y de esta manera, cambia el movimiento de ella.
def girar_izquierda(event):
    #Globalizamos todas las variables necesarias en esta funcion.
    global angulo, nave
    #Le restamos 1/12*pi, para cambiar el angulo.
    angulo -= (1/12.0)*pi
    #Utilizamos el metodo "coords()" de Tkinter para obtener las
    #coordenadas de la nave. Este metodo nos devuelve una lista con las
    #dos coordenadas.
    c = pantalla.coords('nave')
    #Asignamos una variable a cada una de estas coordenadas.
    x = c[0]
    y = c[1]
    #Para que la nave se mueva segun su angulo, debemos definir el seno
    # coseno de este para incluirlo en la velocidad en 'x' y en 'y' de
    #la nave. Para esto importamos el modulo de matematica.
    coseno = round(cos(angulo), 3)
    seno = round(sin(angulo), 3)
    #Por ultimo, llamamos al metodo que corregira la posicion de la figura
    #de la nave. 
    lado_nave(coseno, seno, x, y)#Usamos el coseno, seno, y las 2
                                 #coordenadas que tenemos como parametros

#Esta funcion compone la figura de la nave segun su movimiento.
def lado_nave(coseno, seno, x, y):
    #Globalizamos todas las variables necesarias en esta funcion.
    global angulo, nave, pantalla
    #Utilizamos el seno y el coseno para definir que imagen de la nave
    #utilizar. Ya hay imagenes de la nave en todos los angulos definidos.
    #y con las coordenadas obtenidas anteriormente, asignamos a la nueva
    #imagen de la nave en la misma posicion. Para esto usamos el metodo
    #"delete()" para borrar la nave, y de esta manera importamos la 
    #imagen correspondiente como la nave.
    if coseno == 1.0 and seno == 0.0:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.966 and seno == 0.259:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_15.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.866 and seno == 0.5:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_30.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.707 and seno == 0.707:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_45.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.5 and seno == 0.866:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_60.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.259 and seno == 0.966:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_75.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.0 and seno == 1.0:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_90.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.259 and seno == 0.966:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_105.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.5 and seno == 0.866:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_120.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.707 and seno == 0.707:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_135.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.866 and seno == 0.5:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_150.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.966 and seno == 0.259:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_165.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -1.0 and seno == 0.0:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_180.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.966 and seno == -0.259:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_195.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.866 and seno == -0.5:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_210.gif')
        pantalla.delete('nave')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.707 and seno == -0.707:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_225.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.5 and seno == -0.866:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_240.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == -0.259 and seno == 0.966:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_255.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.0 and seno == -1.0:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_270.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.259 and seno == -0.966:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_285.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.5 and seno == -0.866:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_300.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.707 and seno == -0.707:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_315.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.866 and seno == -0.5:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_330.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')
    elif coseno == 0.966 and seno == -0.259:
        pantalla.delete('nave')
        nave = PhotoImage(file='nave_345.gif')
        pantalla.create_image(x, y, image=nave, tags='nave')

#En esta definicion actualizamos el movimiento de la nave, segun la
#variacion del angulo y la aceleracion.
def move():
    #Globalizamos todas las variables necesarias en esta funcion.
    global aceleracion, velocidad, angulo, nivel, j
    #Creamos la formula de la velocidad dada la aceleracion.
    velocidad= 1/2.0*(aceleracion**2)
    #Mientras que se cumpla la condicion de que "j" sea verdadera, la
    #nave seguira su movimiento. Aunque su aceleracion sea "0".
    while j == True:
        if nivel == 4:
            break
        else:
            #Usamos el modulo de matematica para definir su movimiento
            y = velocidad*(cos(angulo))
            x = velocidad*(sin(angulo))
            #Movemos a la nave segun las variables que definimos anteriormente.
            pantalla.move('nave', x, -y)
            pantalla.after(20)
            pantalla.update()
            #Empezamos el tiempo.
            start_timer()
            #Evaluamos si la nave sigue dentro del laberinto.
            test()
#En esta funcion definimos segun el nivel, los lugares donde hay pared y la
#meta.
def jugar():
    #Globalizamos todas las variables necesarias en esta funcion.    
    global nave, fondo, aceleracion, velocidad, angulo, pantalla, chose_token, ficha, j, nivel, count, puntos
    #Hacemos el bind de las teclas a los metodos.
    window.bind('<Up>', subir_ace)
    window.bind('<Down>', bajar_ace)
    window.bind('<Right>', girar_derecha)
    window.bind('<Left>', girar_izquierda)
    if nivel == 1:
        #Hacemos el random para los power-ups.
        i = randint(1, 3)
        #Importamos las imagenes.
        nave=PhotoImage(file='nave.gif')
        fondo=PhotoImage(file='fondo.gif')
        #Segun el random, se escoge que power-up se colocara en el campo.
        if i == 1:
            ficha = PhotoImage(file='barril_2.gif')
            chose_token = 0
        elif i == 2:
            ficha = PhotoImage(file='power_coin.gif')
            chose_token = 1
        elif i == 3:
            ficha = PhotoImage(file='barril_1.gif')
            chose_token = 2
        #Creamos los objetos del nivel.
        pantalla.create_image(200, 710, image=nave, tags='nave')
        pantalla.create_image(200, 400, image=fondo, tags='mundo')
        pantalla.create_image(150, 500, anchor=NW, image=ficha, tags='token')
        pantalla.lower('mundo')
        pantalla.lift('nave')
        pantalla.lift('token')
        j = True
        #Inicializamos el contador de tiempo.
        count = 10.0
    elif nivel == 2:
        #Hacemos el random para los power-ups.
        i = randint(1, 3)
        #Borramos la nave y fondo del nivel 1, para poner el siguente nivel.
        pantalla.delete('nave')
        pantalla.delete('mundo')
        #Importamos las imagenes.
        nave=PhotoImage(file='nave.gif')
        fondo=PhotoImage(file='fondo_2.gif')
        #Segun el random, se escoge que power-up se colocara en el campo.
        if i == 1:
            ficha = PhotoImage(file='barril_2.gif')
            chose_token = 0
        elif i == 2:
            ficha = PhotoImage(file='power_coin.gif')
            chose_token = 1
        elif i == 3:
            ficha = PhotoImage(file='barril_1.gif')
            chose_token = 2
        #Creamos los objetos del nivel.
        pantalla.create_image(200, 710, image=nave, tags='nave')
        pantalla.create_image(200, 400, image=fondo, tags='mundo')
        pantalla.create_image(200, 400, anchor=NW, image=ficha, tags='token')
        pantalla.lower('mundo')
        pantalla.lift('nave')
        j = True
        #Inicializamos el contador de tiempo.
        count = 20.0
    elif nivel == 3:
        #Hacemos el random para los power-ups.
        i = randint(1, 3)
        #Borramos la nave y fondo del nivel 2, para poner el siguente nivel.
        pantalla.delete('nave')
        pantalla.delete('mundo')
        #Importamos las imagenes.
        nave=PhotoImage(file='nave.gif')
        fondo=PhotoImage(file='fondo_3.gif')
        #Segun el random, se escoge que power-up se colocara en el campo.
        if i == 1:
            ficha = PhotoImage(file='barril_2.gif')
            chose_token = 0
        elif i == 2:
            ficha = PhotoImage(file='power_coin.gif')
            chose_token = 1
        elif i == 3:
            ficha = PhotoImage(file='barril_1.gif')
            chose_token = 2
        #Creamos los objetos del nivel.
        pantalla.create_image(200, 710, image=nave, tags='nave')
        pantalla.create_image(200, 400, image=fondo, tags='mundo')
        pantalla.create_image(200, 300, anchor=NW, image=ficha, tags='token')
        pantalla.lower('mundo')
        pantalla.lift('nave')
        j = True
        #Inicializamos el contador de tiempo.
        count = 40.0
    elif nivel == 4:
        #En caso de que la variable de nivel sea 4, el juego se acaba.
        #Siguendo estos pasos para poder volver a jugar (desde 0) de nuevo.
        showinfo('','Ha ganado, FELICITACIONES!')
        vidas = 5
        nivel = 1
        count = 0.0
        #La variable de juego se hace falsa
        j = True
        validez=False
        #Seguimos a la funcion "regresar_menu"
        regresar_menu()

#En esta funcion evaluamos el movimiento de la nave, si no toca algun punto
#importante de la pantalla como las paredes o la meta. 
def test():
    #Globalizamos todas las variables necesarias en esta funcion.
    global nave, fondo, vidas, aceleracion, chose_token, velocidad, angulo, nivel, j, ficha, deltaA, puntos
    if nivel == 1:
        #Creamos los limites del labrito, al igual que la meta.
        lado1 = pantalla.find_overlapping(0, 0, 131, 800)
        lado2 = pantalla.find_overlapping(269, 0, 400, 800)
        meta = pantalla.find_overlapping(139, 0, 262, 122)
        ficha1 = pantalla.find_overlapping(150, 500, 180, 530)
        tl1 = lado1.__len__()
        tl2 = lado2.__len__()
        tm = meta.__len__()
        tf1 = ficha1.__len__()
        #Evaluamos que la nave no toque estos limites.
        if tl1 == 2 or tl2 == 2:
            aceleracion = 0
            velocidad = 0
            angulo = 0
            j = False
            perder()
        #Evaluamos que la nave no haya llegado ya a la meta.
        if tm == 2:
            nivel+=1
            aceleracion = 0
            velocidad = 0
            angulo = 0
            pantalla.delete('token')
            j = False
            showinfo('','Ha pasado este nivel, FELICITACIONES! Continue al nivel 2')
            subir_puntos()
            jugar()
        #Evaluamos que no toque el power-up.
        if tf1 == 3:
            if chose_token == 0:
                deltaA = 0
            elif chose_token == 1:
                deltaA = 1
            elif chose_token == 2:
                deltaA = 2
            pantalla.delete('token')
            puntos += 5000
            puntos_l['text'] = str(puntos)
    elif nivel == 2:
        #Creamos los limites del labrito, al igual que la meta y el power-up.
        lado1 = pantalla.find_overlapping(0, 800, 131, 678)
        lado2 = pantalla.find_overlapping(0, 678, 61, 361)
        lado3 = pantalla.find_overlapping(0, 361, 261, 243)
        lado4 = pantalla.find_overlapping(0, 263, 131, 0)
        lado5 = pantalla.find_overlapping(267, 800, 400, 600)
        lado6 = pantalla.find_overlapping(140, 599, 400, 480)
        lado7 = pantalla.find_overlapping(338, 480, 400, 0)
        lado8 = pantalla.find_overlapping(269, 0, 400, 122)
        meta = pantalla.find_overlapping(139, 0, 262, 120)
        ficha1 = pantalla.find_overlapping(200, 400, 230, 430)
        tl1 = lado1.__len__()
        tl2 = lado2.__len__()
        tl3 = lado3.__len__()
        tl4 = lado4.__len__()
        tl5 = lado5.__len__()
        tl6 = lado6.__len__()
        tl7 = lado7.__len__()
        tl8 = lado8.__len__()
        tm = meta.__len__()
        tf1 = ficha1.__len__()
        #Evaluamos que la nave no toque estos limites.
        if tl1 == 2 or tl2 == 2 or tl3 == 2 or tl4 == 2 or tl5 == 2 or tl6 == 2 or tl7 == 2 or tl8 == 2:
            aceleracion = 0
            velocidad = 0
            angulo = 0
            j = False
            perder()
        #Evaluamos que la nave no haya llegado ya a la meta.
        if tm == 2:
            nivel+=1
            aceleracion = 0
            velocidad = 0
            angulo = 0
            j = False
            pantalla.delete('token')
            showinfo('','Ha pasado este nivel, FELICITACIONES! Continue al nivel 3!')
            subir_puntos()
            jugar()
        #Evaluamos que no toque el power-up.
        if tf1 == 3:
            if chose_token == 0:
                deltaA = 0
            elif chose_token == 1:
                deltaA = 1
            elif chose_token == 2:
                deltaA = 2
            pantalla.delete('token')
            puntos += 5000
            puntos_l['text'] = str(puntos)
    elif nivel == 3:
        #Creamos los limites del labrito, al igual que la meta.
        lado1 = pantalla.find_overlapping(0, 800, 131, 678)
        lado2 = pantalla.find_overlapping(0, 678, 38, 122)
        lado3 = pantalla.find_overlapping(38, 422, 285, 385)
        lado4 = pantalla.find_overlapping(265, 385, 287, 329)
        lado5 = pantalla.find_overlapping(0, 122,136, 0)
        lado6 = pantalla.find_overlapping(264, 0, 400, 218)
        lado7 = pantalla.find_overlapping(264, 219, 106, 169)
        lado8 = pantalla.find_overlapping(106, 219, 136, 322)
        lado9 = pantalla.find_overlapping(400, 218, 350, 540)
        lado10 = pantalla.find_overlapping(400, 540, 263, 800)
        lado11 = pantalla.find_overlapping(263, 608, 137, 540)
        lado12 = pantalla.find_overlapping(137, 540, 195, 490)
        meta = pantalla.find_overlapping(139, 0, 262, 120)
        ficha1 = pantalla.find_overlapping(200, 300, 230, 330)
        tl1 = lado1.__len__()
        tl2 = lado2.__len__()
        tl3 = lado3.__len__()
        tl4 = lado4.__len__()
        tl5 = lado5.__len__()
        tl6 = lado6.__len__()
        tl7 = lado7.__len__()
        tl8 = lado8.__len__()
        tl9 = lado9.__len__()
        tl10 = lado10.__len__()
        tl11 = lado11.__len__()
        tl12 = lado12.__len__()
        tm = meta.__len__()
        tf1 = ficha1.__len__()
        #Evaluamos que la nave no toque estos limites.
        if tl1 == 2 or tl2 == 2 or tl3 == 2 or tl4 == 2 or tl5 == 2 or tl6 == 2 or tl7 == 2 or tl8 == 2 or tl9 == 2 or tl10 == 2 or tl11 == 2 or tl12 == 2:
            aceleracion = 0
            velocidad = 0
            angulo = 0
            j = False
            perder()
        #Evaluamos que la nave no haya llegado ya a la meta.
        if tm == 2:
            nivel+=1
            aceleracion = 0
            velocidad = 0
            angulo = 0
            j = False
            pantalla.delete('token')
            subir_puntos()
            jugar()
        #Evaluamos que no toque el power-up.
        if tf1 == 3:
            if chose_token == 0:
                deltaA = 0
            elif chose_token == 1:
                deltaA = 1
            elif chose_token == 2:
                deltaA = 2
            pantalla.delete('token')
            puntos += 5000
            puntos_l['text'] = str(puntos)

#Cada ves que pasamos algun nivel, se suben puntos segun el tiempo.
def subir_puntos():
    global puntos, count
    puntos = count*2000
    puntos_l['text'] = str(puntos)

#En caso de que el tiempo se acabe, uno pierde, esta funcion se asegura que el
#tiempo no se acabe, y si en dado caso se acaba, llama a la funcion "perder"
def time_over():
    if count <= 0:
        perder()

#Esta funcion realiza los pasos que debemos en cadenar en caso de perder 1 vida.
def perder():
    #Globalizamos todas las variables necesarias en esta funcion.
    global nave, fondo, label_l, count, nivel,j, validez
    j = False
    #Usamos las coordenadas del choque al momento de perder.
    while j==False:
        c = pantalla.coords('nave')
        #Creamos variables con las coordenadas.
        x = c[0]
        y = c[1]
        #Borramos la nave.
        pantalla.delete('nave')
        #Importamos la imagen de la explosion.
        explosion = PhotoImage(file='explosion.gif')
        pantalla.create_image(x, y, image=explosion, tags='nave')
        #Damos un delay de 1 segundo para ver la explosion.
        pantalla.after(50)
        pantalla.update()
        time.sleep(1)
        #Borramos la explosion
        pantalla.delete('nave')
        #Importamos denuevo la imagen de la nave.
        nave=PhotoImage(file='nave.gif')
        #La inicilizamos en el punto inicial.
        pantalla.create_image(200, 710, image=nave, tags='nave')
        #Regresamos todos el valor del contador de tiempo segun el nivel
        if nivel == 1:
            count = 10.0
        elif nivel == 2:
            count = 20.0
        elif nivel == 3:
            count = 40.0
        #Llamamos a la funcion "perder_vidas".
        perder_vidas()

#En esta funcion hacemos el conteo de vidas, asi como los mensajes este y la
#reduccion de puntos con cada perdida de vidas.
def perder_vidas():
    #Globalizamos todas las variables necesarias en esta funcion.
    global vidas, j, nivel, count, puntos
    #Restamos una vida del contador de vidas.
    vidas -=1
    #Actualizamos el label de las vidas.
    vidas_l['text'] = str(vidas)
    #Escogemos el mensaje de perdida de vidas, segun la cantidad que se tiene.
    if vidas == 4:
        showwarning('', 'Solo tiene 4 vidas, CUIDADO!')
        j = True
    elif vidas == 3:
        showwarning('', 'Solo tiene 3 vidas, CUIDADO!')
        j = True
    elif vidas == 2:
        showwarning('', 'Solo tiene 2 vidas, CUIDADO!')
        j = True
    elif vidas == 1:
        showwarning('', 'Solo tiene 1 vidas, CUIDADO!')
        j = True
    #En caso de que se queden sin vidas, creamos un mensaje de "yes/no" para continuar jugando. 
    elif vidas <= 0:
        
        s = askyesno('', 'Ha perdido, desea intentarlo de nuevo?')
        #En el caso de que escoja que si, el juego vuelve a empezar.
        if s == True:
            vidas = 5
            nivel = 1
            count = 10.0
            puntos = 0
            j=True
            vidas_l['text'] = str(vidas)
            label['text'] = str(count)
            puntos_l['text'] = str(puntos)
            reiniciar()
        #En caso de que escojan que no, ponemos todos los contadores en 0 y
        #regresamos al menu principal.
        else:
            vidas = 5
            nivel = 1
            count = 0.0
            j = True
            validez=False
            regresar_menu()
    #Despues quitamos los puntos por perder una vida.
    if puntos < 10000:
        puntos = 0
    else:
        puntos -= 10000
    #Actualizamos el label de puntos.
    puntos_l['text'] = str(puntos)

        

#Llamamos a la clase de Tkinter y creamos un objeto llamado "window" como la
#base de nuestra interfaz grafica.
window = Tk()
window.title('Space Escape')
#Importamos la imagen de titulo.
img_titulo = PhotoImage(file='spacescape.gif')

#Segun su tamaño, generamos el tamaño del canvas.
titulox = img_titulo.width()
tituloy = img_titulo.height()
#Importamos la imagen de las instrucciones de los botones. 
img_bot = PhotoImage(file='botones.gif')
#Segun el tamaño de la imagen, generamos el tamaño del canvas en donde estara.
img_bot_x = img_bot.width()
img_bot_y = img_bot.height()
#Creamos el frame del menu principal.
menu = Frame(window)
#Generamos los objetos de los labels y botones necesarios.
titulo = Canvas(menu, height=tituloy, width=titulox, bg='white')
start = Button(menu, text='JUGAR', font=("Stencil", 20), command=empezar_juego)
inst = Button(menu, text='INSTRUCCIONES', font=("Stencil", 20), command=instrucciones)
inst_menu = Frame(window)
hs_menu = Frame(window)
read_me = Label(inst_menu, text='''El objetivo es escapar del laberinto guiando su nave espacial a traves
de cada nivel,
de la forma mas rapida y segura posible.
Golpear las paredes o tardarse demasiado implica una muerte segura.
Hay power-ups para ayudarle a traves de los niveles:
estos afectan la aceleracion de la nave y su puntaje.
SPACE ESCAPE!''', bg='black', fg='white')
botones = Canvas(inst_menu, width=img_bot_x, height=img_bot_y, bg='white')
back_menu = Button(inst_menu, text = 'MENU', font=("Helvetica", 20), command=inst_to_menu)

#Inicializamos los objetos que creamos anteriormente.
menu.pack(expand=1, fill=BOTH)
titulo.pack()
start.pack(side=LEFT)
inst.pack(side=RIGHT)
titulo.create_image(0, 0, image=img_titulo, anchor=NW)


#Y luego llamamos al metodo "mainloop" para que funcione correctamente nuestra
#interfaz.
window.mainloop()

