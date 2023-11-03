import pygame
from pygame.locals import *
import math

pygame.init()

green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mi Juego Pygame")

altura=125
longitud=250

lado_uno=125
lado_dos=125

radio=75

base=30
cateto_uno=10
cateto_dos=10
hipotenusa=5

def finish():
    pygame.quit()
    exit()
    
def show_message(surface, text, coordenates, font_color, background, font_size):
    font=pygame.font.SysFont(None, font_size)
    sup_text= font.render(text, True, font_color, background)
    rect_text = sup_text.get_rect()
    rect_text.center = coordenates
    surface.blit(sup_text, rect_text)

def calcular_perimetro_rectangulo(altura, longitud):
    if altura < 0 or longitud < 0:
        return "Las dimensiones no pueden ser negativas"
    
    perimetro = 2 * (altura + longitud)
    return perimetro

def calcular_area_rectangulo(altura, longitud):
    if altura < 0 or longitud < 0:
        return "Las dimensiones no pueden ser negativas"
    
    area = altura * longitud
    return area

def dibujar_rectangulo(surface, rectangulo):
    pygame.draw.rect(
        surface,
        rectangulo["color"],
        (rectangulo["posicion_inicial"]["x"], rectangulo["posicion_inicial"]["y"],
        rectangulo["dimensiones"]["ancho"], rectangulo["dimensiones"]["alto"])
    )

def calcular_perimetro_cuadrado(lado):
    if lado < 0:
        return "El lado no puede ser negativo"
    
    perimetro = 4 * lado
    return perimetro

def calcular_area_cuadrado(lado):
    if lado < 0:
        return "El lado no puede ser negativo"

    area = lado ** 2
    return area

def dibujar_cuadrado(surface, cuadrado):
    pygame.draw.rect(
        surface,
        cuadrado["color"],
        (cuadrado["posicion_inicial"]["x"], cuadrado["posicion_inicial"]["y"],
        cuadrado["lado"], cuadrado["lado"])
    )

def calcular_perimetro_circulo(radio):
    if radio < 0:
        return "El radio no puede ser negativo"
    
    perimetro = 2 * math.pi * radio
    return perimetro

def calcular_area_circulo(radio):
    if radio < 0:
        return "El radio no puede ser negativo"

    area = math.pi * (radio ** 2)
    return area

def dibujar_circulo(surface, circulo):
    pygame.draw.circle(
        surface,
        circulo["color"],
        (circulo["centro"]["x"], circulo["centro"]["y"]),
        circulo["radio"]
    )

def calcular_perimetro_triangulo_rectangulo(a,b,c):
    if a < 0 or b < 0 or c < 0:
        return "Los catetos o la hipotenusa no pueden ser negativos"
    
    perimetro = a + b + c
    return perimetro

def calcular_area_triangulo_rectangulo(base, altura):
    if base < 0 or altura < 0:
        return "La base o la altura no pueden ser negativos"

    area = 0.5 * base * altura
    return area

def dibujar_triangulo_rectangulo(surface, triangulo_rectangulo):
    pygame.draw.polygon(
        surface,
        triangulo_rectangulo["color"],
        triangulo_rectangulo["vertices"]
    )

is_running = True
while is_running:
    screen.fill(black)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
    perimetro_rectangulo=calcular_perimetro_rectangulo(altura, longitud)
    area_rectangulo=calcular_area_rectangulo(altura, longitud)
    rectangulo = {
                "tipo": "rectangulo",
                "dimensiones": {"ancho": longitud, "alto": altura},
                "posicion_inicial": {"x": 100, "y": (altura)},
                "color": green 
            }           
    dibujar_rectangulo(screen, rectangulo)
    show_message(screen, f"Perimetro: {perimetro_rectangulo}, area: {area_rectangulo}", (220, altura+150), green, blue, 25)
    
    if lado_uno==lado_dos:
        perimetro_cuadrado=calcular_perimetro_cuadrado(lado_uno)
        area_cuadrado=calcular_area_cuadrado(lado_uno)
        cuadrado = {
                "tipo": "cuadrado",
                "lado": lado_uno,  # Longitud de un lado
                "posicion_inicial": {"x": 500, "y": 125},
                "color": green # Verde en formato RGB
            }
    dibujar_cuadrado(screen, cuadrado)
    show_message(screen, f"Perimetro: {perimetro_cuadrado}, area: {area_cuadrado}", (600, altura+150), green, blue, 25)

    
    perimetro_circulo=calcular_perimetro_circulo(radio)
    perimetro_circulo=round(perimetro_circulo,2)
    area_circulo=calcular_area_circulo(radio)
    area_circulo=round(area_circulo,2)
    circulo = {
            "tipo": "circulo",
            "centro": {"x": 225, "y": 400},  # Posición del centro
            "radio": radio,  # Radio del círculo
            "color": green
        }
    dibujar_circulo(screen, circulo)
    show_message(screen, f"Perimetro: {perimetro_circulo}, area: {area_circulo}", (220, 500), green, blue, 25)
    
    perimetro_triangulo_rectangulo=calcular_perimetro_triangulo_rectangulo(cateto_uno,cateto_dos,hipotenusa)
    area_triangulo_rectangulo=calcular_area_triangulo_rectangulo(base, altura)
    triangulo_rectangulo = {
                        "tipo": "triangulo_rectangulo",
                        "vertices": [(500, 480), (500, 380), (600, 480)],  # Coordenadas de los vértices
                        "color": green  # Verde en formato RGB
                    }
    dibujar_triangulo_rectangulo(screen, triangulo_rectangulo)
    show_message(screen, f"Perimetro: {perimetro_triangulo_rectangulo}, area: {area_triangulo_rectangulo}", (600, 500), green, blue, 25)

    pygame.display.flip()

pygame.quit()