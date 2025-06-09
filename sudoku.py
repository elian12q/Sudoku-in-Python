#!/usr/bin/python3

import sys
import pygame
import random

'''
Elián Jiménez Quesada C13983

El programa es un juego de sudoku, la idea de este juego es que
sean nueve numeros diferenciados del 1 al 9, que no se deben
repetir en una misma fila, columna o subcuadricula.
Cada plantilla se crea automaticamente y de manera aleatoria una
vez seleccionado el nivel de dificultad.
El jugador o la jugadora debe de completar el sudoku siguiendo
las reglas mencionadas, cuando lo haya llenado completamente,
debera presionar el boton 'Revisar Sudoku', para revisar si lo
completo correctamente, de ser asi habra ganado la partida,
en caso contrario habra perdido la partida.
'''


class Sudoku:

    '''
    Clase que se encarga de crear las casillas del sudoku.
    '''

    def __init__(self, x, y, w, h, text, id):

        '''
        Constructor de la clase.

        :param self: Referencia al propio objeto dentro de la clase.
        :param int x: Coordenada en x de la casilla.
        :param int y: Coordenada en y de la casilla.
        :param int w: Ancho de la casilla.
        :param int h: Alto de la casilla.
        :param str text: Numero de la casilla.
        :param int id: id de la casilla
        '''

        # Crea el cuadrado de la casilla, con tamano y coordenas.
        self.rect = pygame.Rect(x, y, w, h)

        self.color = 'black'  # Color de la casilla.

        self.id = id  # id de la casilla.

        self.text = text  # Numero de la casilla.

        # Lo que se muestra en pantalla
        # El numero, que sea suave y color en RGB.
        self.numero = fuente2.render(text, True, (42, 22, 11))

        # Indicara si la casilla esta seleccionada o no.
        self.active = False

    def cuadros(self, screen):

        '''
        Funcion que dibuja las casillas en la pantalla.

        :param self: Referencia al propio objeto dentro de la clase.
        :param pygame.surface.Surface screen: Pantalla del juego.
        '''

        # Dibuja el cuadro en la pantalla de color blanco.
        pygame.draw.rect(screen, 'white', self.rect)

        # Proyecta el numero de la casilla en l cuadro dibujado,
        # centrado con ayuda de las coordenas, calculando que estuviera
        # en el centro.
        screen.blit(self.numero, (self.rect.x+12, self.rect.y+2))

        # Dibuja el borde el cuadro en la pantalla, color negro y de grosor 3.
        pygame.draw.rect(screen, self.color, self.rect, 3)

    def numeros(self, event):

        '''
        Funcion que permite seleccionar casillas para eventualemte agregarles
        un numero.

        :param self: Referencia al propio objeto dentro de la clase.
        :param Event-KeyDown event: Evento actual en el juego.
        '''

        # La funcion mouse.get_pos() devuelve las coordenadas (x, y)
        # actuales del cursor del mouse en la ventana del juego.
        posicion_mouse = pygame.mouse.get_pos()

        # Este if verifica si el tipo de evento actual
        # es pygame.MOUSEBUTTONDOWN.
        # .MOUSEBUTTONDOWN es un evento que Pygame registra cuando
        # se presiona un boton del mouse.
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Si la casilla en toda su superficie es presionada.
            # El estado de la casilla cambia a activo, sino
            # se mantiene inactivo.
            if self.rect.collidepoint(posicion_mouse):
                self.active = True
            else:
                self.active = False

            # Si la casilla esta activa, se pone de color azul, sino
            # continua siendo negra.
            if self.active:
                self.color = 'blue'
            else:
                self.color = 'black'

        # Este if verifica si el tipo de evento actual
        # es pygame.KEYDOWN.
        # .KEYDOWN es un evento que Pygame registra cuando
        # se presionan teclas del teclado.
        if event.type == pygame.KEYDOWN:

            # Si la casilla esta activa.
            if self.active:
                # Si se presiona la tecla de borrar, se borra el numero.
                # y se actualiza en pantalla.
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]  # Eliminar el ultimo caracter
                    self.numero = fuente2.render(self.text, True, 'black')

                # Si la casilla esta en blanco, y se presiona cualquier numero,
                # se escribe el numero en pantalla, en la casilla activa.
                elif event.unicode.isdigit() and len(self.text) < 1:
                    self.text += event.unicode
                    self.numero = fuente2.render(self.text, True, (47, 65,
                                                                   125))


class Botones:

    '''
    Clase que se encarga de crear los botones graficos que se usaran
    en el juego.
    '''

    def __init__(self, imagen, x_pos, y_pos, texto_input):

        '''
        Constructor de la clase.

        :param self: Referencia al propio objeto dentro de la clase.
        :param pygame.surface.Surface imagen: Imagen de los botones de nivel.
        :param int x_pos: Coordenada en x del boton.
        :param int y_pos: Coordenada en y del boton.
        :param str texto_input: Texto que se mostrara en el boton.
        '''

        self.imagen = imagen  # Almacena la imagen del boton.
        self.x_pos = x_pos  # Almacena la posicion x del boton.
        self.y_pos = y_pos  # Almacena la posicion y del boton.

        # Almacena el texto que se mostrara en el boton.
        self.texto_input = texto_input

        # El metodo render() se utiliza para renderizar el texto.
        # Texto, True para bordes suaves, color del texto.
        self.texto = fuente.render(self.texto_input, True, "black")

        # Si no se quiere usar una imagen especifica, se utiliza
        # solamente el texto como boton.
        if self.imagen is None:
            self.texto = fuente.render(self.texto_input, True, "white")
            self.imagen = self.texto
        else:
            # El metodo render() se utiliza para renderizar el texto.
            # Texto, True para bordes suaves, color del texto.
            self.texto = fuente.render(self.texto_input, True, "black")

        # Crea un rectangulo que envuelve la imagen del boton.
        # El rectangulo esta centrado en las coordenadas x_pos, y_pos.
        self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))

        # Crea un rectangulo que envuelve el texto del boton.
        # El rectangulo esta centrado en las coordenadas x_pos, y_pos.
        self.texto_rect = self.texto.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):

        '''
        Este metodo actualiza la aparicion del boton en la pantalla.

        :param self: Referencia al propio objeto dentro de la clase.
        '''

        # Esto dibuja la imagen del boton en la pantalla, en la posicion
        # especificada por self.rect
        # screen.blit se utiliza para copiar la imagen del texto a la pantalla.
        screen.blit(self.imagen, self.rect)

        # Esto dibuja el texto del boton en la pantalla, en la posicion
        # especificada por self.texto_rect
        screen.blit(self.texto, self.texto_rect)

        # screen.blit se utiliza para copiar la imagen y el texto a
        # la pantalla.

    def clickeos_mouse(self, posicion):

        '''
        Este metodo se utiliza para verificar si se ha hecho
        click en el boton, dado un par de coordenadas de posicion.

        :param self: Referencia al propio objeto dentro de la clase.
        :param tuple position: Coordenadas (x, y) del mouse.

        return bool True: Si se ha hecho click en el boton.
        return bool False: Si no se ha hecho click en el boton.
        '''

        # Si el mouse en la coordenada x hace click en el rango
        # derecha-izquierda del boton, se detecta el click y
        # retorna verdadero.
        # Si el mouse en su la coordenada y hace click en el rango
        # arriba-abajo del boton, se detecta el click y retorna
        # verdadero.
        if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom): # noqa
            return True
        return False

    def animacion_boton(self, posicion):

        '''
        Este metodo se utiliza para verificar si se ha hecho
        click en el boton, dado un par de coordenadas de posicion.

        :param self: Referencia al propio objeto dentro de la clase.
        :param tuple position: Coordenadas (x, y) del mouse.
        '''

        # Si el mouse en su la coordenada x se situa en el rango
        # derecha-izquierda del boton, cambia el color de la letra.
        # Si el mouse en su la coordenada y se situa en el rango
        # arriba-abajo del boton, cambia el color de la letra.
        # Sino, no cambia el color.
        # El primer if condiciona los botones que tienen imagen y los que no.
        if self.imagen == self.texto:
            if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom): # noqa
                self.texto = fuente.render(self.texto_input, True, "red")
            else:
                self.texto = fuente.render(self.texto_input, True, "white")
        else:
            if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom): # noqa
                self.texto = fuente.render(self.texto_input, True, "red")
            else:
                self.texto = fuente.render(self.texto_input, True, "black")


def verificar(sudoku, fila, columna, numero):

    '''
    Esta funcion se encarga de verificar que los numeros generados por la
    funcion rellenar celda no se encuentre ya en la misla fila, columna o
    cuadrante del sudoku.

    param list sudoku: Lista de listas que contiene los numeros del
                       sudoku a generase.
    param int fila: Especifica la fila actual del sudoku.
    param int columna: Especifica la columna actual del sudoku.
    param int numero: Especifica el numero presente en la casilla.

    return bool True: Si el numero no se encuentra ya en la misla fila,
                      columna o cuadrante del sudoku.
    return bool False: Si el numero ya se encuentra en la misla fila,
                      columna o cuadrante del sudoku.
    '''

    # Itera sobre cada fila de toda una columna
    # y verifica que el numero no este en la misma columna.
    for i in range(9):
        if sudoku[i][columna] == numero:
            return False
    # Itera sobre cada columna de toda una fila
    # y verifica que el numero no este en la misma fila.
    for i in range(9):
        if sudoku[fila][i] == numero:
            return False

    # Calcula la celda de la esquina superior izquierda
    # de la submatriz 3x3 a la que pertenece la
    # celda analizada (fila, columna).
    fila2 = (fila // 3) * 3
    columna2 = (columna // 3) * 3

    # Estos dos for recorren la matriz 3x3 y con el if
    # se verifica si el numero ya esta presente en ese
    # cuadrante.
    for i in range(3):
        for j in range(3):
            if sudoku[fila2 + i][columna2 + j] == numero:
                return False
    return True


def rellenar_casilla(i, j, sudoku, numeros):

    '''
    Esta funcion se encarga de rellenar todas las casillas del sudoku,
    utilizando la funcion verificar() verifica que el numero que va a colocar
    en la casilla no se encuentre ya en la misma fila, columna o cuadrante.
    Al hacerlo podria llegar a un punto en el que no tenga ningun numero
    posible a colocar en la casilla, por lo tanto el sudoku quedaria
    incompleto en cierto punto. Para esto se utiliza una recursion en la que
    la funcion se llama a si misma en para que dado caso que llegue a un punto
    muerto pueda devolverse unas cuantas casillas y tomar otro camino,
    generando asi un sudoku completamente validado.

    param int i: Fila de la casilla.
    param int j: Columna de la casilla.
    param list sudoku: Lista de 9 listas con 9 elementos iguales a 0 cada una.
    param list numeros: Lista de numeros del 1 al 9 en desorden.

    return bool True: Si todas las casillas han sido rellenadas correctamente.
    return bool False: Si no se lograron rellenar todas las casillas con
                       ese camino.
    '''

    # Se comprueba si ya se ha llegado a la ultima fila del sudoku.
    if i == 9:
        return True

    # Se actualizan los indices next_i y next_j para la proxima celda que se va
    # a rellenar. Si se esta la ultima columna avanza a la siguiente fila y
    # comienza desde la primera columna. En caso contrario, avanza a la
    # siguiente columna de la misma fila.
    next_i = i + 1 if j == 8 else i
    next_j = 0 if j == 8 else j + 1

    # Verifica si la celda actual ya esta llena. Si la celda esta llena,
    # la funcion se llama a si misma para rellenar la siguiente celda.
    if sudoku[i][j] != 0:
        return rellenar_casilla(next_i, next_j, sudoku, numeros)

    # Este for itera sobre cada numero en la lista numeros.
    for num in numeros:

        # Llama a la funcion verificar() para verificar si el numero
        # puede ser colocado en la casilla.
        if verificar(sudoku, i, j, num):
            sudoku[i][j] = num

            # La funcion se llama a si misma para rellenar la siguiente celda,
            # si retorna True significa que todas las casillas han sido
            # rellenadas correctamente.
            # En el caso contrario se rellena con 0 y se sigue probando
            # con otros numeros.
            if rellenar_casilla(next_i, next_j, sudoku, numeros):
                return True
            sudoku[i][j] = 0
    return False


def rellenar_sudoku(sudoku):

    '''
    Esta funcion se encarga de rellenar el sudoku con valores entre 1 y 9
    casilla por casilla haciendo uso de la funcion rellenar_casilla().

    param list sudoku: Lista de 9 listas con 9 elementos iguales a 0 cada una.

    return function rellenar_casilla(): Retorna esta funcion para que rellene
                                        todas las casillas.
    '''

    # Lista con numeros posibles del sudoku, es decir del 1 al 9.
    numeros = list(range(1, 10))

    # random.shuffle desordena la lista numeros.
    random.shuffle(numeros)
    return rellenar_casilla(0, 0, sudoku, numeros)


def generar_sudoku():

    '''
    Genera el sudoku final, creando una lista de 9 listas con
    9 elementos y usando la funcion rellenar_sudoku lo completa.

    return list sudoku: Retorna el sudoku completo y validado.
    '''

    # [0] * 9 crea una lista con 9 elementos iguales a 0.
    # 9 for i in range(9) genera 9 listas de las que tienen 9 elementos
    # iguales a 0
    # Por lo tanto sudoku es una lista de 9 listas con 9 elementos cada una.
    sudoku = [[0] * 9 for i in range(9)]

    # Llama la funcion rellenar_sudoku().
    rellenar_sudoku(sudoku)
    return sudoku


def general_nivel(boton_menu, boton_terminar, n, win_sound, gameover_sound):

    '''
    Esta funcion se encarga de generar el nivel segun corresponda,
    dependiendo del nivel al que haga click el usuario, generara
    otra ventana con su respectivo sudoku, un boton para regresar al menu
    principal y un boton para revisar el sudoku cuando el usuario lo complete.

    param Boton boton_menu: Boton para regresar al menu principal.
    param Boton boton_terminar: Boton para ir a revisar la solucion del sudoku.
    param int n: Numero para especificar el nivel de dificultad,
                 1 para principiante,2 para intermedio y 3 para avanzado.
    param pygame.mixer.Sound win_sound: Sonido que se escuchara si el sudoku
                                        tiene la solucion correcta.
    param pygame.mixer.Sound gameover_sound: Sonido que se escuchara si el
                                             sudoku tiene la solucion
                                             incorrecta.
    '''

    # Llama la funcion generar_sudoku().
    sudoku = generar_sudoku()

    # Copia del sudoku.
    sudoku_copia = sudoku

    # Con estos dos for los numeros del sudoku se guardan en una lista
    # de manera convencional, en fila, no como una lista de listas.
    numeros_sudoku = [str(numero) for fila in sudoku for numero in fila]

    # Si el nivel es principiante se eliminan 38 numeros del sudoku para que
    # el usuario lo complete.
    if n == 1:
        # Crea una lista de tuplas donde cada tupla representa un par de
        # indices (i, j) correspondientes a una casilla en el Sudoku.
        indices = [(i, j) for i in range(9) for j in range(9)]

        # Selecciona aleatoriamente 38 indices unicos.
        indices_a_eliminar = random.sample(indices, 38)

        # Borra el numero de las celdas seleccionadas.
        for i, j in indices_a_eliminar:
            sudoku_copia[i][j] = ''

    elif n == 2:
        # Crea una lista de tuplas donde cada tupla representa un par de
        # indices (i, j) correspondientes a una casilla en el Sudoku.
        indices = [(i, j) for i in range(9) for j in range(9)]

        # Selecciona aleatoriamente 48 indices unicos.
        indices_a_eliminar = random.sample(indices, 48)

        # Borra el numero de las celdas seleccionadas.
        for i, j in indices_a_eliminar:
            sudoku_copia[i][j] = ''

    elif n == 3:
        # Crea una lista de tuplas donde cada tupla representa un par de
        # indices (i, j) correspondientes a una casilla en el Sudoku.
        indices = [(i, j) for i in range(9) for j in range(9)]

        # Selecciona aleatoriamente 64 indices unicos.
        indices_a_eliminar = random.sample(indices, 64)

        # Borra el numero de las celdas seleccionadas.
        for i, j in indices_a_eliminar:
            sudoku_copia[i][j] = ''

    # Este valor de numeros a eliminar es muy facil de
    # modificar para futuros proyectos en los quieran mas niveles de sudokus.

    # Anchura del cuadro del sudoku.
    ancho = 50

    # Altura del cuadro del sudoku.
    alto = 50

    # Lista para almacenar los objetos de las casillas.
    casillas = []

    # id que identificara a cada casilla.
    id = 1

    # Estos dos for generan las 81 casillas mostradas en pantalla.
    for i in range(9):
        for j in range(9):

            # Itera sobre cada numero dentro del sudoku generado.
            numero = sudoku[i][j]
            # Convierte cada numero en string.
            numero = str(numero)

            # Crea los objetos, con sus coordenadas en (x, y), un
            # espacio de 5 entre casa casilla, ancho y alto de la casilla,
            # el numero que lleva la casilla y el id de la casilla.
            casilla = Sudoku(270+(i*(ancho+5)), 40+(j*(alto+5)),
                             alto, ancho, numero, id)

            # Agrega los objetos a una lista.
            casillas.append(casilla)

            # Aumenta el numero de id para que cada casilla tenga un id
            # diferente.
            id += 1

    while True:

        # La funcion mouse.get_pos() devuelve las coordenadas (x, y)
        # actuales del cursor del mouse en la ventana del juego.
        posicion_mouse = pygame.mouse.get_pos()

        # Llama el metodo animacion_boton().
        boton_menu.animacion_boton(posicion_mouse)
        boton_terminar.animacion_boton(posicion_mouse)

        # Lineas para separar los 9 cuadrantes.
        # (pantalla, color, punto_inicio, punto_final, grosor).
        pygame.draw.line(screen, 'black', (266, 40), (266, 529), 10)
        pygame.draw.line(screen, 'black', (431, 40), (431, 529), 10)
        pygame.draw.line(screen, 'black', (596, 40), (596, 529), 10)
        pygame.draw.line(screen, 'black', (762, 40), (762, 529), 10)

        pygame.draw.line(screen, 'black', (262, 36), (767, 36), 10)
        pygame.draw.line(screen, 'black', (262, 201), (767, 201), 10)
        pygame.draw.line(screen, 'black', (262, 366), (767, 366), 10)
        pygame.draw.line(screen, 'black', (262, 531), (767, 531), 10)

        # Este for itera sobre cada evento que ocurre en pygame.
        # pygame.event.get() devuelve una lista de todos los eventos que
        # han ocurrido desde la ultima vez que se llamo.
        for event in pygame.event.get():

            # Este if verifica si el tipo de evento actual es pygame.QUIT.
            # .QUIT se genera cuando el usuario intenta cerrar
            # la ventana pygame.
            # En caso True, se cierra pygame con pygame.quit() y se finaliza
            # la ejecucion del
            # programa con sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Para objeto de la lista casillas, llama la funcion numeros().
            for box in casillas:
                box.numeros(event)

            # Este if verifica si el tipo de evento actual
            # es pygame.MOUSEBUTTONDOWN.
            # .MOUSEBUTTONDOWN es un evento que Pygame registra cuando
            # se presiona un boton del mouse.
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Estos dos if utilizan el metodo clickeos_mouse() para
                # ejecutar la funcion que implica presionar el boton
                # menu o el boton terminar.
                if boton_menu.clickeos_mouse(posicion_mouse):
                    main_menu(imagen_boton, imagen_fondo_menu,
                              principiante_sound, intermedio_sound,
                              avanzado_sound)

                if boton_terminar.clickeos_mouse(posicion_mouse):
                    lista_a_ravisar = []

                    # Para todos los numeros del sudoku final del usuario
                    # los agrega a una lista vacia.
                    for box in casillas:
                        lista_a_ravisar.append(box.text)

                    # Si dicha lista es igual a la lista original del sudoku
                    # significa que el usuario completo el sudoku correctamente
                    # en el caso contrario significa que el usuario completo
                    # el sudoku incorrectamente.
                    if lista_a_ravisar == numeros_sudoku:

                        # Detiene la musica de fondo.
                        pygame.mixer.music.stop()

                        # Reproduce el sonido para el nivel avanzado.
                        win_sound = win_sound.play()

                        # El metodo render() se utiliza para renderizar
                        # el texto.
                        # Texto, True para bordes suaves, color del texto.
                        win1 = fuente.render('Felicidades :D', True, 'white')
                        win2 = fuente.render('sudoku conseguido!', True,
                                             'white')

                        # Crea un rectangulo que envuelve el texto del boton.
                        # El rectangulo esta centrado en las coordenadas
                        # indicadas.
                        win1_rect = win1.get_rect(center=(550, 580))
                        win2_rect = win2.get_rect(center=(550, 610))

                        # Esto ciclo se ejecuta en el tiempo que dure el
                        # sonido para cuando se gana.
                        # get_busy() verifica si el programa esta
                        # actualmente reproduciendo algun sonido.
                        # Devuelve True si el programa esta reproduciendo
                        # algun sonido y False en caso contrario.
                        while win_sound.get_busy():
                            # Esto dibuja el texto en la pantalla, en la
                            # posicion especificada por win1_rect y
                            # win2_rect.
                            screen.blit(win1, win1_rect)
                            screen.blit(win2, win2_rect)

                            # Esta funcion actualiza la pantalla
                            # constantemente.
                            pygame.display.update()

                        # Espera 1 segundo para regresar al menu principal.
                        pygame.time.delay(1000)
                        main_menu(imagen_boton, imagen_fondo_menu,
                                  principiante_sound, intermedio_sound,
                                  avanzado_sound)
                    else:
                        # Detiene la musica de fondo.
                        pygame.mixer.music.stop()

                        # Reproduce el sonido para el nivel avanzado.
                        gameover_sound = gameover_sound.play()

                        # El metodo render() se utiliza para renderizar
                        # el texto.
                        # Texto, True para bordes suaves, color del texto.
                        gameover = fuente.render('GAME OVER D:', True, 'white')

                        # Crea un rectangulo que envuelve el texto del boton.
                        # El rectangulo esta centrado en las coordenadas
                        # indicadas.
                        gameover_rect = gameover.get_rect(center=(550, 600))

                        # Esto ciclo se ejecuta en el tiempo que dure el
                        # sonido para cuando se pierde.
                        # get_busy() verifica si el programa esta
                        # actualmente reproduciendo algun sonido.
                        # Devuelve True si el canal esta reproduciendo algun
                        # sonido y False en caso contrario.
                        while gameover_sound.get_busy():
                            # Esto dibuja el texto en la pantalla, en
                            # la posicion especificada por gameover_rect.
                            screen.blit(gameover, gameover_rect)

                            # Esta funcion actualiza la pantalla
                            # constantemente.
                            pygame.display.update()

                        # Espera 2 segundos para regresar al menu principal.
                        pygame.time.delay(2000)
                        main_menu(imagen_boton, imagen_fondo_menu,
                                  principiante_sound, intermedio_sound,
                                  avanzado_sound)

        # Para objeto de la lista casillas, llama la funcion numeros().
        for box in casillas:
            box.cuadros(screen)

        # Llama el metodo update().
        boton_menu.update()
        boton_terminar.update()

        # Esta funcion actualiza la pantalla constantemente.
        pygame.display.update()


def boton_nivel(imagen_boton, imagen_fondo, n, sonido):

    '''
    Esta funcion ejecuta el proceso que implica presionar con el mouse
    un boton de nivel, la animacion de la musica, la animacion de cargando
    y la deteccion del nivel que fue seleccionado.

    param pygame.surface.Surface imagen_boton: Imagen de los botones de nivel.
    param pygame.surface.Surface imagen_fondo: Imagen del fondo de los niveles.
    param int n: Numero para especificar el nivel de dificultad,
                 1 para principiante,2 para intermedio y 3 para avanzado.
    param pygame.mixer.Sound sonido: Sonido que se escuchara cuando se abra
                                     un nivel en especifico.
    '''

    # Detiene la musica de fondo.
    pygame.mixer.music.stop()

    # Reproduce el sonido para el nivel avanzado.
    sonido = sonido.play()

    # El metodo render() se utiliza para renderizar el texto.
    # Texto, True para bordes suaves, color del texto.
    cargando = fuente.render('Cargando . . .', True, 'white')

    # Crea un rectangulo que envuelve el texto del boton.
    # El rectangulo esta centrado en las coordenadas indicadas.
    cargando_rect = cargando.get_rect(center=(500, 350))

    # Esto ciclo se ejecuta en el tiempo que dure el sonido para
    # el nivel elegido.
    # get_busy() verifica si el programa esta actualmente reproduciendo
    # algun sonido. Devuelve True si el programa esta reproduciendo
    # algun sonido y False en caso contrario.
    while sonido.get_busy():

        # Esto dibuja el texto en la pantalla, en la posicion
        # especificada por cargando_rect
        screen.blit(cargando, cargando_rect)

        # Esta funcion actualiza la pantalla constantemente.
        pygame.display.update()

    # Reproduce la musica de fondo.
    # -1 para que sea un bucle infinito.
    pygame.mixer.music.play(-1)

    # Este while mantiene el juego en funcionamiento continuamente
    while True:

        # Se escribe el nivel de dificultad, dependiendo del valor de n.
        if n == 1:
            nivel = 'Principiante'
        elif n == 2:
            nivel = 'Intermedio'
        elif n == 3:
            nivel = 'Avanzado'

        # Se pone el fondo de la imagen cargada.
        screen.blit(imagen_fondo, (0, 0))

        # El metodo render() se utiliza para renderizar el texto.
        # Texto, True para bordes suaves, color del texto.
        nivel_texto = fuente.render('Nivel', True, 'black')
        nivel = fuente.render(nivel, True, 'black')

        # Crea un rectangulo que envuelve el texto del boton.
        # El rectangulo esta centrado en las coordenadas indicadas.
        nivel_texto_rect = nivel_texto.get_rect(center=(125, 85))
        nivel_rect = nivel.get_rect(center=(125, 110))

        # Esto dibuja el texto en la pantalla, en la posicion
        # especificada por nivel_rect
        screen.blit(nivel_texto, nivel_texto_rect)
        screen.blit(nivel, nivel_rect)

        # Crea el objeto del boton menu.
        boton_menu = Botones(imagen_boton, 150, 600, 'Menu Principal')
        boton_terminar = Botones(imagen_boton, 130, 350, 'Revisar Sudoku')

        # Se ingresa al nivel presionado con el mouse.

        # Nivel principiante.
        if n == 1:
            general_nivel(boton_menu, boton_terminar, n,
                          win_sound, gameover_sound)

        # Nivel intermedio.
        elif n == 2:
            general_nivel(boton_menu, boton_terminar, n,
                          win_sound, gameover_sound)

        # Nivel avanzado.
        elif n == 3:
            general_nivel(boton_menu, boton_terminar, n,
                          win_sound, gameover_sound)


def quit():

    '''
    Funcion que se encarga de cerrar el juego.
    '''

    # Utiliza pygame.quit() para cerrar el modulo de Pygame.
    pygame.quit()
    # Utiliza sys.exit() para salir del programa.
    sys.exit()


def main_menu(imagen_boton, imagen_fondo_menu, principiante_sound,
              intermedio_sound, avanzado_sound):

    '''
    Esta funcion genera el menu principal del juego, con 4 botones,
    3 botones de nivel de juego y un boton para salir.

    param pygame.surface.Surface imagen_boton: Imagen de los botones de nivel.
    param pygame.surface.Surface imagen_fondo_menu: Imagen del fondo del menu.
    param pygame.mixer.Sound principiante_sound: Sonido para nivel
                                                 principiante.
    param pygame.mixer.Sound intermedio_sound: Sonido para nivel intermedio.
    param pygame.mixer.Sound avanzado_sound: Sonido para nivel avanzado.
    '''

    # Se define un numero para cada nivel.
    p = 1
    i = 2
    a = 3

    # Reproduce la musica de fondo.
    # -1 para que sea un bucle infinito.
    pygame.mixer.music.play(-1)

    # Este while mantiene el juego en funcionamiento continuamente
    while True:

        # La funcion mouse.get_pos() devuelve las coordenadas (x, y)
        # actuales del cursor del mouse en la ventana del juego.
        posicion_mouse = pygame.mouse.get_pos()

        # Crea el objeto del boton Principiante.
        boton_principiante = Botones(imagen_boton, 170, 300, "PRINCIPIANTE")

        # Crea el objeto del boton Intermedio.
        boton_intermedio = Botones(imagen_boton, 170, 450, "INTERMEDIO")

        # Crea el objeto del boton Avanzado.
        boton_avanzado = Botones(imagen_boton, 170, 600, "AVANZADO")

        # Crea el objeto del boton Avanzado.
        boton_quit = Botones(imagen=None, x_pos=730,
                             y_pos=620, texto_input="Quit.")

        # Este for ejecuta la animacion del boton a los 4 botones creados,
        # utilizando el metodo creado animacion_boton y utilizando
        # pygame.mouse.get_pos() que se guarda en posicion_mouse.
        for boton in [boton_principiante, boton_intermedio,
                      boton_avanzado, boton_quit]:
            boton.animacion_boton(posicion_mouse)

        # Este for itera sobre cada evento que ocurre en pygame.
        # pygame.event.get() devuelve una lista de todos los eventos que
        # han ocurrido desde la ultima vez que se llamo.
        for event in pygame.event.get():

            # Este if verifica si el tipo de evento actual es pygame.QUIT.
            # .QUIT se genera cuando el usuario intenta cerrar
            # la ventana pygame.
            # En caso True, se cierra pygame con pygame.quit() y se finaliza
            # la ejecucion del programa con sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Este if verifica si el tipo de evento actual
            # es pygame.MOUSEBUTTONDOWN.
            # .MOUSEBUTTONDOWN es un evento que Pygame registra cuando
            # se presiona un boton del mouse.
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Estos tres if utilizan el metodo clickeos_mouse() para
                # ejecutar la funcion que implica presionar un boton
                # en especifico.
                if boton_principiante.clickeos_mouse(posicion_mouse):
                    boton_nivel(imagen_boton, imagen_fondo, p,
                                principiante_sound)
                if boton_intermedio.clickeos_mouse(posicion_mouse):
                    boton_nivel(imagen_boton, imagen_fondo, i,
                                intermedio_sound)
                if boton_avanzado.clickeos_mouse(posicion_mouse):
                    boton_nivel(imagen_boton, imagen_fondo, a,
                                avanzado_sound)
                if boton_quit.clickeos_mouse(posicion_mouse):
                    quit()

        # Se pone el fondo de la imagen cargada.
        screen.blit(imagen_fondo_menu, (0, 0))

        # Llama el metodo update().
        boton_principiante.update()
        boton_intermedio.update()
        boton_avanzado.update()
        boton_quit.update()

        # Esta funcion actualiza la pantalla constantemente.
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()  # Inicializa pygame.
    screen = pygame.display.set_mode((800, 700))  # Genera la pantalla.
    pygame.display.set_caption("sudoku.py")
    # fuente de letra a utilizar.
    fuente = pygame.font.Font("WaHandwriting-Regular.ttf", 37)
    # fuente de letra a utilizar para los numeros.
    fuente2 = pygame.font.Font("WaHandwriting-Regular.ttf", 60)

    # Carga la imagen de los botones para el nivel
    # de dificultad.
    imagen_boton = pygame.image.load("boton.png")

    # Ajusta el tamano de los botones para el nivel de dificultad.
    imagen_boton = pygame.transform.scale(imagen_boton, (268, 150))

    # Carga la imagen de fondo del menu.
    imagen_fondo_menu = pygame.image.load("fondo_menu.jpg")

    # Carga la imagen de fondo general.
    imagen_fondo = pygame.image.load("fondo.jpg")

    # Carga la musica de fondo.
    pygame.mixer.music.load("20200317.wav")

    # Carga el sonido para el nivel principiante.
    principiante_sound = pygame.mixer.Sound("principiante_sound.mp3")

    # Carga el sonido para el nivel intermedio.
    intermedio_sound = pygame.mixer.Sound("intermedio_sound.mp3")

    # Carga el sonido para el nivel avanzado.
    avanzado_sound = pygame.mixer.Sound("avanzado_sound.mp3")

    # Carga el sonido para victorias.
    win_sound = pygame.mixer.Sound("win_sound.mp3")

    # Carga el sonido para derrotas.
    gameover_sound = pygame.mixer.Sound("gameover_sound.mp3")

    # Llama al menu principal.
    main_menu(imagen_boton, imagen_fondo_menu, principiante_sound,
              intermedio_sound, avanzado_sound)
