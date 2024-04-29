import pygame 
from personaje import Personaje
cuadrito1 = Personaje(80,80)
cuadrito2 = Personaje(237,80)
cuadrito3 = Personaje(394,80)
pygame.init() #metodo para inicializar pygame si no pues como monda va a funcionar
tamaño= (800,800)
ventana = pygame.display.set_mode((tamaño)) #pa mostrar la ventana pa! esa monda traduce algo como pygame pantalla modo pa poner pantalla "pyg.pantalla.modo de ajuste"
# doble parantesis por que yes 
#la pantalla pues toca guardala en una variable xd por que aja todo tiene que estar en algun lao funciona si no pero pa 
#trabajar con la pantalla es mejor tenerla guardada en algun lado 
pygame.display.set_caption("Aprendiendo pygame") # pa ponerle nombre a la ventana (traduce algo asi como pyg.pantalla.modo de captura o modo de nombre de juego, pa los compas)

 #toca hace run while para que no se cierre insofacto la ventana 
run = True
while run: #la variable evento pues almacenara los eventos que pasen en el jueguito namas
    cuadrito1.draw(ventana)  
    cuadrito2.draw(ventana)
    cuadrito3.draw(ventana)
    for event in pygame.event.get(): # para cada evento que pase en el registro de pygame.event.get() (metodo para garrar los eventos)
         # osease por evento se refiere a cualquier accion dentro de la pagina sea un clic una tecla etc. 
        if event.type == pygame.QUIT : # si el tipo de evento sea cual sea es igual a un evento que cierra el juego (a eso se refiere pygame.QUIT 
             #con QUIT en grande) 
            run = False #tons run se vuelve falso y deja de funcionar el el ciclo osea se cierra la pagina  
    pygame.display.update() # actualiza los cambios que se hacen como en este caso dibujar a cuadradito 
    #sino pues e queda en la parte de arriba donde creamos la ventana pero no hace mas, ahora con esta funcion agarra las
    #cosas nuevas que le dijimos que hiciera y pues la hace xd      
pygame.quit #esta funcion con quit chiquito es simplemente pa finalilzar pygame

#------------------------- hora si viene lo chido (toca ponerlo en el while xd) ------------------------------
