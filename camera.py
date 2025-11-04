# Módulo de cámara para seguir al jugador
import pygame
from settings import *
vec = pygame.math.Vector2

class Camera(object):
    """Clase que maneja la cámara del juego para seguir al sprite del jugador"""

    def __init__(self, width, height):
        # Inicializa la posición de la cámara en el origen (0,0)
    	self.pos = vec(0,0)

    def update(self, sprite):
        """
        Actualiza la posición de la cámara para seguir al sprite

        Args:
            sprite: El sprite del jugador a seguir
        """
        # Si el sprite puede moverse, la cámara sigue su posición en X
    	if sprite.canMove:
    		self.pos.x = -sprite.pos.x

    	# Limita el movimiento de la cámara al límite izquierdo
    	if self.pos.x >= LEFT_BOUND:
    		self.pos.x = LEFT_BOUND
    	# Limita el movimiento de la cámara al límite derecho
    	elif self.pos.x <= RIGHT_BOUND:
    		self.pos.x = RIGHT_BOUND

    	# Movimiento vertical deshabilitado (comentado)
    	#self.pos.y = min(-sprite.pos.y+HEIGHT/2,0)
    	#print(self.pos.x)

# Instancia global de la cámara con las dimensiones de la pantalla
camera = Camera(WIDTH, HEIGHT)
        
