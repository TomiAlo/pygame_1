import pygame
from sys import exit
from config import *
from aleatorios import *
from random import randint, randrange

pygame.init()

clock=pygame.time.Clock()
#configuro la pantalla principal
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Primer juego")

fuente = pygame.font.Font(None,36)

texto = fuente.render("hola mundo", True, red)
rec_texto=texto.get_rect()

rec_texto.center=center_screen

is_running=True

while is_running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    #-->actualizar elementos
    
    
    #dibujar pantalla
    screen.fill(black)
    
    screen.blit(texto, rec_texto)
            
    #actualizar pantalla        
    pygame.display.flip()
    
pygame.quit()