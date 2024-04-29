import pygame 

class Personaje: #ora si papa!!! pygame con clases (POO)
    def __init__(self, x , y): # variables x y y pa pocisionar el prota si no pues donde aparece ese men
        self.shape = pygame.Rect(0,0,150,150) # en la veriable self.shape va a haber un rectangulo que aprece en la 
        #posicion 0,0 de tamaño 20px x 20px (eso hace el metodo Rect)
        self.shape.center = (x,y) # la variable ya creada de shape en 0,0 la vamos a poner centradita donde le digamos que es x,y
    def draw(self, interfaz):
         pygame.draw.rect(interfaz, (255,0,0), self.shape)
         #bueno a ver creo que : esa funcion dice :
         #pygame.dibujar.el rectagulito (donde monda dibujo? (una  interfaz o ventanita xd),
         # de que color e?, y que dibujo? (la forma que ya cree))
    def move(self, delta_x, delta_y):
        self.shape.x += delta_x            #funcion para mover a cuadrito 5 px hacia algun lado segun las variables deta_tin
        self.shape.y += delta_y            