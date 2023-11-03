import pygame
from sys import exit
from config import *
from funciones import *
from random import randint, randrange

pygame.init()

clock=pygame.time.Clock()

#configuro la pantalla principal
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Primer juego")

width_coin=20
height_coin=20
gravedad_y=True
gravedad_x=True

is_running=True

#configuro la direccion
UpRight=9
DownRight=3
DownLeft=1
UpLeft=7
direcciones=(UpRight,UpLeft,DownLeft,DownRight)

coins=[]
count_coins=20

blocks=[]
count_blocks=1

for block in range(count_blocks):
    blocks.append(build_rect(randint(0,width-rect_w),randint(0,height-rect_h),rect_w,rect_h,get_new_color(),UpRight,randrange(31),randint(-1,25)))    

for coin in range(count_coins):
    coins.append(build_rect(randint(0,width-width_coin),randint(0,height-height_coin),width_coin,height_coin,yellow,0,0,height_coin//2))

while is_running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    #-->actualizar elementos
    
    #verifico si el bloque choca contra los limites de la pantalla
    #actualizo su direccion
    for block in blocks:
        if block["rect"].right >= width:
            #choco derecha
            if block["dir"]==DownRight:
                block["dir"]=DownLeft
            elif block["dir"]==UpRight:
                block["dir"]=UpLeft
                block["color"]=get_new_color()    
        
        elif block["rect"].left <= 0:
            #choco izquierda
            if block["dir"] == UpLeft:
                block["dir"]=UpRight
            elif block["dir"]==DownLeft:
                block["dir"]=DownRight
            block["borde"]=randrange(31)
        
        elif block["rect"].top <= 0:
            #choco arriba
            if block["dir"] == UpLeft:
                block["dir"]=DownLeft
            elif block["dir"]==UpRight:
                block["dir"]=DownRight
        
        elif block["rect"].bottom >= height:
            #choco abajo
            if block["dir"] == DownRight:
                block["dir"]=UpRight
            elif block["dir"]==DownLeft:
                block["dir"]=UpLeft
            block["radio"]=randint(-1,25)
    
    
    
    #muevo el bloque de acuerdo a su direccion
    for block in blocks:
        if block["dir"]==DownRight:
            block["rect"].top+=speed
            block["rect"].left+=speed
            
        elif block["dir"]==DownLeft:
            block["rect"].top+=speed
            block["rect"].left-=speed
            
        elif block["dir"]==UpLeft:
            block["rect"].top-=speed
            block["rect"].left-=speed
            
        elif block["dir"]==UpRight:
            block["rect"].top-=speed
            block["rect"].left+=speed


    for coin in coins[:]: ##coins.copy():
        if detectar_colision(coin["rect"],block["rect"]):
            coins.remove(coin)
    
    #dibujar pantalla
    screen.fill(black)
    for block in blocks:
        pygame.draw.rect(screen,block["color"],block["rect"],block["borde"], block["radio"])         
        
    for coin in coins:
        pygame.draw.rect(screen,coin["color"],coin["rect"],coin["borde"], coin["radio"])
            
    #actualizar pantalla        
    pygame.display.flip()
    
pygame.quit()