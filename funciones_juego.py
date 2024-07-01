import sys 
import pygame
from bala import Bala 
from alien import Alien

def verificar_eventos_keydown(event,ai_configuraciones, pantalla, nave, balas):
    #responde a las pulsaciones de teclas
     if event.key == pygame.K_RIGHT:
        nave.moving_right = True
     elif event.key == pygame.K_LEFT:
        nave.moving_left = True
     elif event.key == pygame.K_SPACE:
         fuego_bala(ai_configuraciones, pantalla, nave, balas)
     elif event.key == pygame.K_q:
         sys.exit()

def verificar_eventos_keyup(event, nave):
    #responde a las pulsaciones de teclas
     if event.key == pygame.K_RIGHT:
        nave.moving_right = False
     elif event.key == pygame.K_LEFT:
        nave.moving_left = False

def verificar_eventos(ai_configuraciones,pantalla, nave, balas):
    #responde a las pulsaciones y teclas y los eventos del raton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("saliendo")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
           verificar_eventos_keydown(event,ai_configuraciones,pantalla, nave, balas)       
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)
        

def actualizar_pantalla(ai_configuraciones, pantalla, nave, aliens, balas):
    #actualiza las imagenes en la pantalla y pasa a la nueva pantalla
    # Volver a dibujar la pantalla durante cada pasada por el bucle while
    pantalla.fill(ai_configuraciones.bg_color)
    #Vuelve a dibujar todas las balas detras de la nave y de los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    aliens.draw(pantalla)
    
    #hacer visible la pntalla dibujada mas reciente
    pygame.display.flip()

def update_bala(balas):
    #actualiza la poscion de las balas y elimina las antiguas
    #Actualiza las posciiones de las balas
    balas.update()
    #deshace las balas que han desaparecido
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)    

def fuego_bala(ai_configuraciones, pantalla, nave, balas):
    #dispara bala si aun no alcanza el limite
    #crea una bala y agregala al grupo de balas
    if len(balas) < ai_configuraciones.balas_allowed:
        nueva_bala = Bala(ai_configuraciones, pantalla, nave)
        balas.add(nueva_bala)

def get_number_aliens_x(ai_configuraciones, alien_width):
    #determina el numero de alienigenas que caben en una fila
    available_space_x = ai_configuraciones.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_configuraciones, nave_height, alien_height):
    #determina el numero de filas de alienigenas que caben en la pantalla
    available_space_y = (ai_configuraciones.screen_height - 
                         (3 * alien_height) - nave_height)
    number_rows =int(available_space_y / (2 * alien_height))
    return number_rows

def crear_alien(ai_configuraciones, pantalla, aliens, alien_number, row_number):
    #crea un alien y lo coloca en la fila
    alien = Alien(ai_configuraciones, pantalla)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def crear_flota(ai_configuraciones, pantalla,nave, aliens):
    #crea una flota de alienigenas
    #crea un alien y encuentra el numero de aliens seguidos
    #el espacio entrew cada alien es igual al ancho de cada alien
    alien = Alien(ai_configuraciones, pantalla)
    number_aliens_x = get_number_aliens_x(ai_configuraciones, alien.rect.width)
    number_rows = get_number_rows(ai_configuraciones, nave.rect.height, alien.rect.height)
    

    #crea la flota de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            crear_alien(ai_configuraciones, pantalla, aliens, alien_number, row_number)

def update_aliens(aliens):
    #actualiza la posicion de todos los alienigenas
    aliens.update()
