import pygame, sys, classes, random
from processo import off_tela, controles

def inicio(tiro, fps, total_frames, screen_size, start_sprite, exit_sprite, title_sprite):

	tiro.bala = 1000

	inicio_game = controles(tiro, fps, total_frames, screen_size, start_sprite, exit_sprite)

	off_tela(screen_size)		
	inicio_animacao(tiro, start_sprite, exit_sprite, title_sprite)


	return inicio_game

# inicio, sair, 
def inicio_animacao(tiro, start_sprite, exit_sprite, title_sprite): 
	
	# title
	if pygame.sprite.spritecollide(title_sprite, classes.Projetil.sprite_list, True): 
	 	title_sprite.image = pygame.image.load("images/misc/title_hit.png")
	else:
	 	title_sprite.image = pygame.image.load("images/misc/title.png")

	# inicio
	if pygame.sprite.spritecollide(start_sprite, classes.Nave.sprite_list, False) \
	 or pygame.sprite.spritecollide(start_sprite, classes.Projetil.sprite_list, True):
		start_sprite.image = pygame.image.load("images/misc/start_high.png")
	else:
		start_sprite.image = pygame.image.load("images/misc/inicio.png")

	# sair
	if pygame.sprite.spritecollide(exit_sprite, classes.Nave.sprite_list, False) \
	 or pygame.sprite.spritecollide(exit_sprite, classes.Projetil.sprite_list, True):
		exit_sprite.image = pygame.image.load("images/misc/exit_high.png")
	else:
		exit_sprite.image = pygame.image.load("images/misc/sair.png")

	



