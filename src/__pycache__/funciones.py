import pygame
from random import randrange

def get_color(lista_de_colores):
    return lista_de_colores[randrange(len(lista_de_colores))]

def get_new_color():    
    r=randrange(256)
    g=randrange(256)
    b=randrange(256)
    return (r,g,b)

def build_rect(left=150, top=150, width=50, height=50, color=(250,250,250), dir=3, border=0, radius=-1):
    
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"dir":dir, "borde":border, "radio":radius}

def detectar_colision(rect_1, rect_2):
    
    for r1,r2 in [(rect_1, rect_2),(rect_2, rect_1)]:
        return punto_en_rectangulo(r1.topleft, r2) or \
        punto_en_rectangulo(r1.topright, r2) or \
        punto_en_rectangulo(r1.bottomleft, r2) or \
        punto_en_rectangulo(r1.bottomright, r2)

def punto_en_rectangulo(punto, rect):
    x, y=punto
    return x>=rect.left and x<=rect.right and y>=rect.top and y<=rect.bottom
