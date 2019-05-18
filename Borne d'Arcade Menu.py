import pygame
from pygame.locals import *
import webbrowser
import os.path
import pickle

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        self.pos = ((pygame.display.get_surface().get_width()/2)-(self.rend.get_width()/2), #(Taille de la fenetre/2)-(Taille du texte/2)
        			self.pos[1])
        
    def get_color(self):
        if self.hovered:
            if self.get_name() == option_mainmenu_5 :
                return color_option_quit
            else :
                return color_options_hovered
        else:
            return color_options_nhovered
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def get_name(self):
    	return self.text

    def get_text_height(self):
    	return self.rend.get_height()

    def get_pos(self):
    	return self.pos

    def set_pos_y_default(self):
    	global text_options_height_total
    	return (pygame.display.get_surface().get_height()/2)-(text_options_height_total/2)

    def refresh_options(self):
    	self.set_rect()


class Titre:
    
    def __init__(self, text, pos, color):
        self.text = text
        self.pos = pos
        self.color = color
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = title_font.render(self.text, True, self.color)
        self.pos = ((pygame.display.get_surface().get_width()/2)-(self.rend.get_width()/2), #(Taille de la fenetre/2)-(Taille du texte/2)
        			self.pos[1])
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def refresh_title(self):
    	self.set_rect()

    def get_color(self):
        return self.color

    def get_name(self):
        return self.text

    def get_text_height(self):
        return self.rend.get_height()

    def get_pos(self):
        return self.pos


class About:
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = about_font.render(self.text, True, color_about)
        self.pos = ((pygame.display.get_surface().get_width()/2)-(self.rend.get_width()/2), #(Taille de la fenetre/2)-(Taille du texte/2)
        			self.pos[1])
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def refresh_about(self):
    	self.set_rect()

    def get_name(self):
        return self.text

    def get_text_height(self):
        return self.rend.get_height()

    def get_pos(self):
        return self.pos

    def set_pos_y_default(self):
        global text_desc_height_total
        return (pygame.display.get_surface().get_height()/2)-(text_desc_height_total/2)

class News:
    
    def __init__(self, text, pos, color):
        self.text = text
        self.pos = pos
        self.color = color
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = news_font.render(self.text, True, self.color)
        self.rend = pygame.transform.rotate(self.rend, 45)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def get_pos(self):
        return self.pos

    def get_width(self):
        return self.rend.get_width()


def set_key_name(key_name):
    if key_name == "left" :
        key_name = "Fleche gauche"
    elif key_name == "right" :
        key_name = "Fleche droite"
    elif key_name == "up" :
        key_name = "Fleche haut"
    elif key_name == "down" :
        key_name = "Fleche bas"
    elif key_name == "space" :
        key_name = "Espace"
    elif key_name == "print screen" :
        key_name = "Impécran."
    elif key_name == "pause" :
        key_name = "Pause"
    elif key_name == "insert" :
        key_name = "Inser"
    elif key_name == "delete" :
        key_name = "Suppr."
    elif key_name == "numlock" :
        key_name = "VerrNum."
    elif key_name == "backspace" :
        key_name = "Retour"
    elif key_name == "return" :
        key_name = "Entrée"
    elif key_name == "caps lock" :
        key_name = "VerrMaj."
    elif key_name == "left shift" :
        key_name = "Maj gauche"
    elif key_name == "right shift" :
        key_name = "Maj droite"
    elif key_name == "left ctrl" :
        key_name = "Ctrl gauche"
    elif key_name == "right ctrl" :
        key_name = "Ctrl droite"
    elif key_name == "left super" :
        key_name = "Win gauche"
    elif key_name == "right super" :
        key_name = "Win droite"
    elif key_name == "left alt" :
        key_name = "Alt gauche"
    elif key_name == "enter" :
        key_name = "Entrée"
    elif key_name == "[/]" :
        key_name = "Num. /"
    elif key_name == "[*]" :
        key_name = "Num. *"
    elif key_name == "[.]" :
        key_name = "Num. ."
    elif key_name == "[+]" :
        key_name = "Num. +"
    elif key_name == "[-]" :
        key_name = "Num. -"
    elif key_name == "[9]" :
        key_name = "Num. 9"
    elif key_name == "[8]" :
        key_name = "Num. 8"
    elif key_name == "[7]" :
        key_name = "Num. 7"
    elif key_name == "[6]" :
        key_name = "Num. 6"
    elif key_name == "[5]" :
        key_name = "Num. 5"
    elif key_name == "[4]" :
        key_name = "Num. 4"
    elif key_name == "[3]" :
        key_name = "Num. 3"
    elif key_name == "[2]" :
        key_name = "Num. 2"
    elif key_name == "[1]" :
        key_name = "Num. 1"
    elif key_name == "[0]" :
        key_name = "Num. 0"
    elif key_name == "unknown key" :
        key_name = "Touche non reconnue"
    else:
        key_name = key_name.capitalize()
    return key_name

def settings():
    if os.path.exists("Settings") == False :
        with open("DefaultSettings", "rb") as default_settings:
            file = pickle.Unpickler(default_settings)
            read_default_settings = file.load()
        with open("Settings", "wb") as settings:
            file = pickle.Pickler(settings)
            file.dump(read_default_settings)

    with open("Settings", "rb") as settings:
        file = pickle.Unpickler(settings)
        read_settings = file.load()
    options = [Option(" ", default_pos)]
    global name_options
    name_options = []
    for name in read_settings:
        name_options.append(name + "  ~  " + set_key_name(read_settings[name]))
        options.append(Option(name + "  ~  " + set_key_name(read_settings[name]), default_pos))
    options.append(Option(option_back_to_menu, default_pos))
    return options

def set_settings(name_option, new_key_name):
    with open("Settings", "rb") as settings:
        file = pickle.Unpickler(settings)
        old_read_settings = file.load()

    options = [Option(" ", default_pos)]
    global name_options
    name_options = []
    new_settings = {}
    for name in old_read_settings:
        if name == name_option:
            name_options.append(name + "  ~  " + set_key_name(new_key_name))
            options.append(Option(name + "  ~  " + set_key_name(new_key_name), default_pos))
            new_settings[name] = set_key_name(new_key_name)
        else:
            name_options.append(name + "  ~  " + set_key_name(old_read_settings[name]))
            options.append(Option(name + "  ~  " + set_key_name(old_read_settings[name]), default_pos))
            new_settings[name] = set_key_name(old_read_settings[name])
    options.append(Option(option_back_to_menu, default_pos))

    with open("Settings", "wb") as settings:
        file = pickle.Pickler(settings)
        file.dump(new_settings)
    return options

def Change_key(name_option):
	key = False
	while key == False:
		event = pygame.event.wait()
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				options = settings()
				key = True
			else:
				key_name = pygame.key.name(event.key)
				options = set_settings(name_option, key_name)
				key = True
		else:
			key = False
	return options

def set_music(name_option):
    with open("Settings",  "rb") as settings:
        file = pickle.Unpickler(settings)
        old_read_settings = file.load()

    options = [Option(" ", default_pos)]
    global name_options
    name_options = []
    new_settings = {}
    for name in old_read_settings:
        if name == name_option:
            if old_read_settings[name] == "Activée":
                name_options.append(name + "  ~  Désactivée")
                options.append(Option(name + "  ~  Désactivée", default_pos))
                new_settings[name] = "Désactivée"
            elif old_read_settings[name] == "Désactivée":
                name_options.append(name + "  ~  Activée")
                options.append(Option(name + "  ~  Activée", default_pos))
                new_settings[name] = "Activée"
        else:
            name_options.append(name + "  ~  " + set_key_name(old_read_settings[name]))
            options.append(Option(name + "  ~  " + set_key_name(old_read_settings[name]), default_pos))
            new_settings[name] = set_key_name(old_read_settings[name])
    options.append(Option(option_back_to_menu, default_pos))

    with open("Settings", "wb") as settings:
        file = pickle.Pickler(settings)
        file.dump(new_settings)
    return options



pygame.init()

#Ouverture de la fenêtre Pygame
WinSize = (889, 460)
screen = pygame.display.set_mode(WinSize, RESIZABLE)

#Chargement du titre de la fenetre
pygame.display.set_caption("Borne d'Arcade | Menu")

#Chargement et collage de l'icon de la fenetre
WinIcon = pygame.image.load("Images/Icon.png").convert()
pygame.display.set_icon(WinIcon)

#Chargement et collage du Background
Background = pygame.image.load("Images/Background_Menu.png").convert()
BackgroundSize = Background.get_size()
BackgroundSizeDisplay = BackgroundSize
screen.blit(Background, (0,0))

#Chargement et collage du Logo
Icon = pygame.image.load("Images/Icon_alpha.png").convert_alpha()
difference_logo = 15
Icon_pos = (pygame.display.get_surface().get_width()-pygame.transform.scale(Icon, (100, 100)).get_width()-difference_logo, pygame.display.get_surface().get_height()-pygame.transform.scale(Icon, (100, 100)).get_height()-difference_logo)
screen.blit(pygame.transform.scale(Icon, (100, 100)), Icon_pos)

#Chargement et collage de la bannière news
news_banner = pygame.image.load("Images/Banner.png")
screen.blit(news_banner, (0, 0))

#Mise en place du pointer
pygame.mouse.set_visible(False)
pointer_img = pygame.image.load("Images/Pointer.png")

#Mise en place des menus
menu_font = pygame.font.Font("Fonts/game_over.ttf", 80)
title_font = pygame.font.Font("Fonts/game_over.ttf", 150)
about_font = pygame.font.Font("Fonts/game_over.ttf", 60)
news_font = pygame.font.Font("Fonts/game_over.ttf", 55)

default_pos = (0, -150)

color_options_hovered = (191, 129, 28)
color_option_quit = (191, 0, 0)
color_options_nhovered = (136, 136, 136)
color_titles = (253, 165, 16)
color_about = (200, 200, 200)
color_news = (255, 217, 0)

#Main menu
option_mainmenu_1 = "Pong 1 joueur"
option_mainmenu_2 = "Pong 2 joueurs"
option_mainmenu_3 = "Options"
option_mainmenu_4 = "A propos"
option_mainmenu_5 = "Quitter"
title_mainmenu = "BORNE D'ARCADE"

#About menu
option_back_to_menu = "Retour au menu"
title_about = "A PROPOS"
description_about_1 = "Menu réalisé par Valentin Bonnet"
description_about_2 = "Pong 1 joueur réalisé par Etienne Faviere"
description_about_3 = "Pong 2 joueurs réalisé par Maximilien Beaulaton"
description_about_4 = "Menu et jeux réalisés pour les TPE d'ISN 2017-2018 au lycée St Eloi"
description_about_5 = "©Copyright Beaulaton Maximilien & Bonnet Valentin"
description_about_6 = "& Faviere Etienne - 2017/2018"

#Options
title_settings = "OPTIONS"

#Quit menu
option_quit_1 = "Oui"
option_quit_2 = "Non"
title_quit = "Etes vous sur de vouloir quitter ?"

#News
News_text = " Jeux réalisés avec Python !"
News_pos = (5, 5)
news_link = "http://www.python.org"

#Click sound
click_sound = pygame.mixer.Sound("Sounds/click.wav")
sound_state = True


options = [Option(option_mainmenu_1, default_pos), Option(option_mainmenu_2, default_pos), Option(option_mainmenu_3, default_pos), Option(option_mainmenu_4, default_pos), Option(option_mainmenu_5, default_pos)]
titres = [Titre(title_mainmenu, default_pos, color_titles)]
descriptions = []
info = [News(News_text, News_pos, color_news)]

settings()


while True:
    pygame.event.pump()
    pygame.display.set_caption("Borne d'Arcade | Menu")

    #Chargement, collage et mise à l'échelle du Background
    screen_x = pygame.display.get_surface().get_width()
    screen_y = pygame.display.get_surface().get_height()
    if screen_x > screen_y :
        BackgroundSizeDisplay = (screen_x, int(WinSize[1] * screen_x / WinSize[0]))
    else :
        BackgroundSizeDisplay = (int(WinSize[1] * screen_y / WinSize[0]), screen_y)

    screen = pygame.display.set_mode(BackgroundSizeDisplay, RESIZABLE)
    screen.blit(pygame.transform.scale(Background, BackgroundSizeDisplay), (0,0))

    #Chargement, collage, mise à l'échelle du Logo et zoom lors du passage de la souris
    Icon_pos = (pygame.display.get_surface().get_width()-pygame.transform.scale(Icon, (100, 100)).get_width()-difference_logo, pygame.display.get_surface().get_height()-pygame.transform.scale(Icon, (100, 100)).get_height()-difference_logo)
    Icon_resize = (100, 100)
    zoom_icon = 10
    if pygame.Rect(Icon_pos, (Icon_pos[0]+Icon.get_width(), Icon_pos[1]+Icon.get_height())).collidepoint(pygame.mouse.get_pos()):
        screen.blit(pygame.transform.scale(Icon, ((Icon_resize[0]+zoom_icon), (Icon_resize[1]+zoom_icon))), (Icon_pos[0]-(zoom_icon/2), Icon_pos[1]-(zoom_icon/2)))
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            options = [Option(option_back_to_menu, default_pos)]
            titres = [Titre(title_about, default_pos, color_titles)]
            descriptions = [About(description_about_1, default_pos), About(description_about_2, default_pos), About(description_about_3, default_pos), About(description_about_4, default_pos), About(description_about_5, default_pos), About(description_about_6, default_pos)]
    else :
        screen.blit(pygame.transform.scale(Icon, Icon_resize), Icon_pos)

    #Position y des options
    nb_options = len(options)
    text_options_height_total = 0
    difference_options = 0
    difference_about_option = 15
    add_difference_options = (20, 2) #2x - Quit & Settings
    for i in range(0, nb_options):
    	text_options_height_total = text_options_height_total + options[i].get_text_height()
    text_options_height_total = text_options_height_total + (add_difference_options[0]*add_difference_options[1])

    texts_options_height = - options[0].get_text_height()

    for i in range(0, nb_options):
        texts_options_height = texts_options_height + options[i].get_text_height()
        if i > 0 :
            texts_options_height = texts_options_height + difference_options
        if options[i].get_name() == option_mainmenu_3:
            options[i] = Option(options[i].get_name(), (options[i].get_pos()[0], (options[i].set_pos_y_default()+texts_options_height+add_difference_options[0])))
        elif options[i].get_name() == option_mainmenu_4:
            options[i] = Option(options[i].get_name(), (options[i].get_pos()[0], (options[i].set_pos_y_default()+texts_options_height+add_difference_options[0])))
        elif options[i].get_name() == option_mainmenu_5:
            options[i] = Option(options[i].get_name(), (options[i].get_pos()[0], (options[i].set_pos_y_default()+texts_options_height+(add_difference_options[0]*add_difference_options[1]))))
        elif options[i].get_name() == option_back_to_menu:
            options[i] = Option(options[i].get_name(), (options[i].get_pos()[0], (pygame.display.get_surface().get_height()-options[i].get_text_height()-difference_about_option)))
        else:
            options[i] = Option(options[i].get_name(), (options[i].get_pos()[0], (options[i].set_pos_y_default()+texts_options_height)))


    #Position y des descriptions
    if descriptions != [] :
        nb_desc = len(descriptions)
        text_desc_height_total = 0
        difference_desc = 10
        for i in range(0, nb_desc):
            text_desc_height_total = text_desc_height_total + descriptions[i].get_text_height()

        texts_desc_height = - descriptions[0].get_text_height()

        for i in range(0, nb_desc):
            texts_desc_height = texts_desc_height + descriptions[i].get_text_height()
            if i > 0 :
                texts_desc_height = texts_desc_height + difference_desc
            descriptions[i] = About(descriptions[i].get_name(), (descriptions[i].get_pos()[0], (descriptions[i].set_pos_y_default()+texts_desc_height)))


    #Position y des titres
    nb_titles = len(titres)
    text_titles_height_total = 0
    title_pos_y = 95
    if nb_titles == 1 :
        difference_titles = 0
    else :
        difference_titles = 5
    for i in range(0, nb_titles):
        text_titles_height_total = text_titles_height_total + titres[i].get_text_height()

    for i in range(0, nb_titles):
        if i == 0 :
            titres[i] = Titre(titres[i].get_name(), (titres[i].get_pos()[i], (title_pos_y-titres[i].get_text_height()-difference_titles/2)), titres[i].get_color())
        else :
            titres[i] = Titre(titres[i].get_name(), (titres[i].get_pos()[i], (title_pos_y+difference_titles/2)), titres[i].get_color())


    #Traitement des options
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    click_sound.play()
                    #Option 1
                    if option.get_name() == option_mainmenu_1 :
                        print("Lancement du jeu Pong 1 joueur...")
                        exec(open("Jeux/Pong 1.py").read())
                    #Option 2
                    elif option.get_name() == option_mainmenu_2 :
                        print("Lancement du jeu Pong 2 joueurs...")
                        exec(open("Jeux/Pong 2.py").read())
                    #Option 3
                    elif option.get_name() == option_mainmenu_3 :
                        titres = [Titre(title_settings, default_pos, color_titles)]
                        options = settings()
                    #Option 1 de l'option 3
                    elif option.get_name() == name_options[0] :
                        options = Change_key("Pong : Joueur 2 - Droite")
                    #Option 2 de l'option 3
                    elif option.get_name() == name_options[1] :
                        options = Change_key("Pong : Joueur 2 - Gauche")
                    #Option 3 de l'option 3
                    elif option.get_name() == name_options[2] :
                        options = Change_key("Pong : Joueur 1 - Gauche")
                    #Option 4 de l'option 3
                    elif option.get_name() == name_options[3] :
                        options = Change_key("Pong : Joueur 1 - Droite")
                    #Option 5 de l'option 3
                    elif option.get_name() == name_options[4] :
                        options = set_music("Pong : Musique")
                    #Option 4
                    elif option.get_name() == option_mainmenu_4 :
                        options = [Option(option_back_to_menu, default_pos)]
                        titres = [Titre(title_about, default_pos, color_titles)]
                        descriptions = [About(description_about_1, default_pos), About(description_about_2, default_pos), About(description_about_3, default_pos), About(description_about_4, default_pos), About(description_about_5, default_pos), About(description_about_6, default_pos)]
                    #Option de l'option 4 & 3
                    elif option.get_name() == option_back_to_menu :
                        options = [Option(option_mainmenu_1, default_pos), Option(option_mainmenu_2, default_pos), Option(option_mainmenu_3, default_pos), Option(option_mainmenu_4, default_pos), Option(option_mainmenu_5, default_pos)]
                        titres = [Titre(title_mainmenu, default_pos, color_titles)]
                        descriptions = []
                    #Option 5
                    elif option.get_name() == option_mainmenu_5 :
                        title_font = pygame.font.Font("Fonts/game_over.ttf", 100)
                        titres = [Titre(title_quit, default_pos, color_titles)]
                        options = [Option(option_quit_1, default_pos), Option(option_quit_2, default_pos)]
                    #Option de l'option 5
                    elif option.get_name() == option_quit_1 :
                        pygame.quit()
                    elif option.get_name() == option_quit_2 :
                        options = [Option(option_mainmenu_1, default_pos), Option(option_mainmenu_2, default_pos), Option(option_mainmenu_3, default_pos), Option(option_mainmenu_4, default_pos), Option(option_mainmenu_5, default_pos)]
                        title_font = pygame.font.Font("Fonts/game_over.ttf", 150)
                        titres = [Titre(title_mainmenu, default_pos, color_titles)]
        else:
            option.hovered = False

        option.draw()

    #Traitement des titres
    for titre in titres:
    	titre.draw()

    #Traitement des descriptions
    for description in descriptions:
    	description.draw()
    
    #Traitement des événements sur les news
    for news in info:
        if news.rect.collidepoint(pygame.mouse.get_pos()):
            if sound_state == True:
                click_sound.play()
                sound_state = False
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    webbrowser.open(news_link)
        else:
            sound_state = True

    #Traitement des événements
    for event in pygame.event.get():
        if event.type == QUIT: #Si on quite la fenetre
            pygame.quit()

        if event.type == VIDEORESIZE:
            if event.dict['size'] < WinSize : #Si la fenetre est redimensionnée
                screen = pygame.display.set_mode(WinSize, RESIZABLE)
            else :
                screen = pygame.display.set_mode(event.dict['size'], RESIZABLE)
            screen.blit(pygame.transform.scale(Background, event.dict['size']), (0,0))

            for titre in titres:
                titre.refresh_title()
            for option in options:
                option.refresh_options()
            for description in descriptions:
                description.refresh_about()

            pygame.display.flip()
            pygame.display.update()

    if pygame.display.get_surface().get_size() < WinSize :
    	screen = pygame.display.set_mode(WinSize, RESIZABLE)

    #Rafraichissement de la bannière news
    screen.blit(news_banner, (-28, -28))

    #Rafraichissement des News
    if len(News_text) > 15 :
        News_text_1 = ""
        News_text_2 = ""
        for i in News_text :
            if len(News_text_1) < 15 :
                News_text_1 = News_text_1 + i
            elif len(News_text_2) < 15 :
                News_text_2 = News_text_2 + i
            elif len(News_text_2) == 15 :
                News_text_2 = News_text_2 + "..."
        info = [News(News_text_1, News_pos, color_news), News(News_text_2, (23, 23), color_news)]
    else :
        info = [News(News_text, News_pos, color_news)]

    #Rafraichissement du pointer
    pointer_pos = pygame.mouse.get_pos()
    if pointer_pos == (0, 0):
        screen.blit(pointer_img, (-100, -100))
    else:
        screen.blit(pointer_img, (pointer_pos[0], pointer_pos[1]))

    #Rafraichissement
    pygame.display.flip()
    pygame.display.update()