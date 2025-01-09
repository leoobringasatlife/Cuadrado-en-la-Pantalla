import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ventana de Juego")

NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

reloj = pygame.time.Clock()

# Tamaño y posición del cuadrado
lado_cuadrado = 50
x, y = 100, 100  # Coordenadas iniciales
vel_x, vel_y = 5, 5  # Velocidad del cuadrado

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el cuadrado
    x += vel_x
    y += vel_y

    # Detectar colisiones con los bordes
    if x <= 0 or x + lado_cuadrado >= 800:
        vel_x = -vel_x
    if y <= 0 or y + lado_cuadrado >= 600:
        vel_y = -vel_y

    # Dibujar en la pantalla
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, ROJO, (x, y, lado_cuadrado, lado_cuadrado))

    # Actualizar la pantalla
    pygame.display.flip()
    reloj.tick(60)
