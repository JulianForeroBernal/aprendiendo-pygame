import pygame 
from personaje import Personaje
cuadrito1 = Personaje(80,80)
pygame.init() #metodo para inicializar pygame si no pues como monda va a funcionar
tamaño= (800,800)
 
ventana = pygame.display.set_mode((tamaño)) #pa mostrar la ventana pa! esa monda traduce algo como pygame pantalla modo pa poner pantalla "pyg.pantalla.modo de ajuste"
# doble parantesis por que yes 
#la pantalla pues toca guardala en una variable xd por que aja todo tiene que estar en algun lao funciona si no pero pa 
#trabajar con la pantalla es mejor tenerla guardada en algun lado 

pygame.display.set_caption("Aprendiendo pygame") # pa ponerle nombre a la ventana (traduce algo asi como pyg.pantalla.modo de captura o modo de nombre de juego, pa los compas)

mover_arriba = False
mover_izquierda = False # variables para que al apretar una tecla se vuelvan verdaderas y haga una accion 
mover_derecha = False
mover_abajo = False
time = pygame.time.Clock()
 #toca hace run while para que no se cierre insofacto la ventana 
run = True
while run: #la variable evento pues almacenara los eventos que pasen en el jueguito namas
    ventana.fill((0,0,20))
    time.tick(60)
    delta_x = 0 # variables para la cantidad de pixeles que se va a mover toca en el run pa que todo el tiempo se reinicie la cuneta
    delta_y = 0
    if mover_arriba == True :
        delta_y = -5
    if mover_izquierda == True:
        delta_x = -5
    if mover_derecha == True :               # segun que variable pase a ser verdadera se suma o resta a delta_tin pa que despues se mueva cuadrito
        delta_x = 5
    if mover_abajo == True :
        delta_y = 5
    cuadrito1.move(delta_x,delta_y)  
    cuadrito1.draw(ventana) 
    print(F"{delta_x}, {delta_y}")

    for event in pygame.event.get(): # para cada evento que pase en el registro de pygame.event.get() (metodo para garrar los eventos)
         # osease por evento se refiere a cualquier accion dentro de la pagina sea un clic una tecla etc. 
        if event.type == pygame.QUIT : # si el tipo de evento sea cual sea es igual a un evento que cierra el juego (a eso se refiere pygame.QUIT 
             #con QUIT en grande) 
            run = False #tons run se vuelve falso y deja de funcionar el el ciclo osea se cierra la pagina  
        if event.type == pygame.KEYDOWN : #denuevo, si el tipo de evento que agarra es de tipo oprimir tecla (pygame.keydown) tons...
            # event.key agarra que tecla apreto (ya se sabe que lo que va a agarrar son eventos de tipo letra, tons ahora toca que letra fue {que codigo de letra por eso key})
            if event.key == pygame.K_UP :
                mover_arriba = True
            if event.key == pygame.K_LEFT :  
                mover_izquierda = True
            if event.key == pygame.K_RIGHT :          #segun que letra se oprime cierta variable pasa a ser verdadera
                mover_derecha = True
            if event.key == pygame.K_DOWN :           
                mover_abajo = True
        if event.type == pygame.KEYUP: # si el tipo de evento es soltar tecla (pygame.keyup) tons...
            if event.key == pygame.K_UP :
                mover_arriba = False
            if event.key == pygame.K_LEFT :  
                mover_izquierda = False
            if event.key == pygame.K_RIGHT :          #segun que letra se oprime cierta variable pasa a ser verdadera
                mover_derecha = False
            if event.key == pygame.K_DOWN :           
                mover_abajo = False
  
    pygame.display.update() # actualiza los cambios que se hacen como en este caso dibujar a cuadradito 
    #sino pues e queda en la parte de arriba donde creamos la ventana pero no hace mas, ahora con esta funcion agarra las
    #cosas nuevas que le dijimos que hiciera y pues la hace xd      
pygame.quit() #esta funcion con quit chiquito es simplemente pa finalilzar pygame
