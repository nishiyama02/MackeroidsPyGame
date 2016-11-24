import pygame, sys
import time, math
from classes import *
from processo import processo
from star_screen import inicio

pygame.init()
pygame.font.init()

screen_size = (640, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('*')
clock = pygame.time.Clock()
fps = 60

# pontuacao
bala = 100
total_frames = 0
total_pontuacao = 0
hp = 35
max_pontuacao = 0
hight_pontuacao = 0

# tiro 
tiro = Nave((screen_size[0] - 32) * 0.5, screen_size[1] * 0.75, hp, bala, 'images/tiro/espaconave.png')

# inicio menu 
start_sprite = IniciaMenu(screen_size[0] * 0.15, screen_size[1] * 0.45, 'images/misc/inicio.png')
exit_sprite = IniciaMenu(screen_size[0] * 0.65, screen_size[1] * 0.45, 'images/misc/sair.png')
title_sprite = IniciaMenu(screen_size[0] * 0.3, screen_size[1] * 0.25, 'images/misc/title.png')
instructions = IniciaMenu(screen_size[0] * 0.25, screen_size[1] * 0.8, 'images/misc/instrucao.png')

# texto tela
pontuacao_couter = TextToScreen(screen_size[0] * 0.66, 4, 32, (205, 220, 255))
bala_track = TextToScreen(screen_size[0] * 0.36, 4, 32, (235, 190, 215))
hp_tracker = TextToScreen(screen_size[0] * 0.01, 4, 32, (180, 255, 190))
game_over = TextToScreen(screen_size[0] * 0.30, screen_size[1] * 0.16, 64, (190, 130, 135))
beta =  TextToScreen(2, screen_size[1] -16, 20, (100, 40, 60))


star_screen = True


#processo do game
def game_on(star_screen, tiro, total_pontuacao, max_pontuacao, hight_pontuacao, fps, total_frames, screen_size):
	
	# inicio tela
	if star_screen: 

		star_screen = inicio(tiro, fps, total_frames, screen_size, start_sprite, exit_sprite, title_sprite)
		max_pontuacao = math.floor(total_pontuacao)


		IniciaMenu.sprite_list.draw(screen)

		if max_pontuacao > 0: # game over 
			pontuacao_couter.text_return(screen, 'pontuacao: ' + str(max_pontuacao))
			game_over.text_return(screen, 'GAME OVER')
		

	if not star_screen: # game tela

		if max_pontuacao > 0: 
			total_pontuacao = 0
	

		star_screen, pontuacao = processo(tiro, fps, total_frames, screen_size, start_sprite, exit_sprite) 
		total_pontuacao += pontuacao
		str_total_pontuacao = math.floor(total_pontuacao)

		# sprite tela
		Asteroids.moving_enemy(fps, total_frames, screen_size)
		Pacote.moving_gift(fps, total_frames, screen_size)

		# texto tela
		pontuacao_couter.text_return(screen, 'pontuacao: ' + str(str_total_pontuacao))
		bala_track.text_return(screen, 'bala: ' + str(tiro.bala))
		hp_tracker.text_return(screen, 'hp: ' + str(tiro.health))

	return star_screen, total_pontuacao


while True: # main loop

	screen.fill((13, 10, 18))
	clock.tick(fps)


	total_frames += 1 

	star_screen, total_pontuacao = game_on(star_screen, tiro, total_pontuacao, max_pontuacao, hight_pontuacao, fps, total_frames, screen_size)
				

	tiro.movimento(screen_size)
	Projetil.disparo()

	Asteroids.sprite_list.draw(screen)
	Nave.sprite_list.draw(screen)
	Projetil.sprite_list.draw(screen)
	Pacote.sprite_list.draw(screen)


	beta.text_return(screen, 'MACKENZIE 2016')
	pygame.display.flip()


pygame.quit()
sys.exit()