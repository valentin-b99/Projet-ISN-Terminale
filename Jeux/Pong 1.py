import pygame
from pygame.locals import *
from math import *
from random import *

pygame.init()

#ouverture fenetre

fenetre = pygame.display.set_mode((300,200 ))

#Titre
pygame.display.set_caption("Borne d'Arcade | Pong 1 Joueur")
v0 = 2

#Chargement et affichage de l'écran d'accueil
taille_ecran = fenetre.get_width()
accueil = pygame.image.load("Images/fond pong.jpg").convert()
fenetre.blit(accueil, (0,0))
barre = pygame.image.load("Images/raquette.png")
position_barre = barre.get_rect()
balle = pygame.image.load("Images/balle.png")
fenetre.blit(barre,(150,180))
pos_x = 150
pos_y = 180
balle_x = 150
balle_y = 100
continuer = 1

alpha = int(random()*360)
if alpha == 90:
    alpha = int(random()*360)
if alpha == 180 :
    alpha = int(random()*360)
if alpha == 270:
    alpha = int(random()*360)
if alpha == 0:
    alpha = int(random()*360)
if alpha == 360:
    alpha = int(random()*360)

alpha = (alpha/360)*2*pi
while continuer:
    pygame.time.Clock().tick(30)
    #Chargement et affichage de l'écran d'accueil
    fenetre.blit(accueil, (0,0))
    fenetre.blit(barre,(pos_x, pos_y))
    fenetre.blit(balle,(balle_x, balle_y))

    #déplacement de la balle
    balle_x = v0 * cos(alpha) + balle_x
    balle_y = v0 * sin(alpha) + balle_y
                 
    #Rafraichissement
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            
            if event.key == K_d:
                pos_x = pos_x + 10
                if pos_x > taille_ecran - 20 :
                    pos_x = taille_ecran - 20
                    
            if event.key == K_q:
                pos_x = pos_x - 5
                if pos_x < 0:
                    pos_x = 0
            if event.key == K_ESCAPE:
                continuer = 0


    #collisions balle
    if balle_x >= 300 :
        alpha = pi - alpha
    if balle_x <= 0:
        alpha = pi - alpha

    if balle_y <= 0:
        v0 = -v0
        alpha = pi - alpha
    if 180 >balle_y >175 :
        if pos_x <= balle_x <= pos_x + 20:
            v0 = -v0
            alpha = pi - alpha
    if balle_y > 200:
        continuer = 0
    #Rafraichissement
    pygame.display.flip()
    
fin = pygame.image.load("Images/fin.jpg").convert()
fenetre.blit(fin, (0,0))
pygame.display.flip()

