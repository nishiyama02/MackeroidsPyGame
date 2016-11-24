import pygame, sys, classes, random


def processo(tiro, fps, total_frames, screen_size, start_sprite, exit_sprite):
			
	pontuacao = 0 # inicio a pontuacao 
	
	controles(tiro, fps, total_frames, screen_size, start_sprite, exit_sprite)

	#got_gift = pacote_intervalo(fps, total_frames, screen_size)
	pontuacao += off_tela(screen_size)
	pontuacao += asteroide_colisao(tiro, classes.Nave.sprite_list) 	
	colisao(tiro)
	asteroid_spawn(fps, total_frames, screen_size)

	if tiro.health == 0: 

		try:
			for i in classes.Asteroids.sprite_list: 

				i.destruir(classes.Asteroids)
				i.destruir(classes.Pacote)
 
			print('MORREU!')
		except:
			pass

		return True, pontuacao 

	return False, pontuacao 


# segue comando dos usuários
def controles(tiro, fps, total_frames, screen_size, start_sprite, exit_sprite):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		keys = pygame.key.get_pressed()

		if event.type == pygame.KEYUP:
			tiro.velx = 0
			tiro.vely = 0
			tiro.image = pygame.image.load('images/tiro/espaconave.png')
		
		if keys[pygame.K_w]:
			tiro.vely = -8
			tiro.image = pygame.image.load('images/tiro/espaconave_ignicao.png')

		if keys[pygame.K_s]:
			tiro.vely = 4 
			tiro.image = pygame.image.load('images/tiro/espaconave.png')

		if keys[pygame.K_d]:
			tiro.velx = 7
			tiro.image = pygame.image.load('images/tiro/espaconave.png')

		if keys[pygame.K_a]:
			tiro.velx = -7
			tiro.image = pygame.image.load('images/tiro/espaconave.png')

		
		# inicio game 
		if pygame.sprite.spritecollide(start_sprite, classes.Nave.sprite_list, False):

			if keys[pygame.K_RETURN]:
				tiro.health = 35
				
				return False
		# sair game
		if pygame.sprite.spritecollide(exit_sprite, classes.Nave.sprite_list, False):

			if keys[pygame.K_RETURN]:
				pygame.quit()
				sys.exit()

	keys = pygame.key.get_pressed()

	if tiro.bala > 0: 
		if keys[pygame.K_SPACE]:
			classes.Projetil(tiro.rect.x + 10, tiro.rect.y - 6 , -11, tiro, 'images/tiro/shot.png', fps, total_frames, screen_size)


	return True 

# intervalo de asteroids e imagens
def asteroid_spawn(fps, total_frames, screen_size):

	interval = .2 
	spawn_time = fps * interval

	if total_frames % spawn_time == 0:
		hp = random.randint(1, 5) 

		x = random.randint(4, screen_size[0] - 44) 
	
		if hp == 1:
			classes.Asteroids(x, -60, hp, 'images/asteroid/asteroid3.png')
		elif hp > 1 and hp < 4:
			classes.Asteroids(x, -60, hp, 'images/asteroid/asteroid2.png')
		else:
			classes.Asteroids(x, -60, hp, 'images/asteroid/asteroid.png')


# deleta imagens de asteroides detruidos
def off_tela(screen_size): 
	pontuacao = 0 

	try:
		for i in classes.Projetil.normal_list:
			if i.rect.y < -200: 
				i.destruir()
	except:
		pass

	try:
		for i in classes.Asteroids.sprite_list: 

			if i.rect.y > screen_size[1] + 200:
				i.destruir(classes.Asteroids)
				pontuacao += 0.4 
	except:
		pass

	return pontuacao

# astedoide  colisao com tiro
def asteroide_colisao(tiro, ClassName):  
	pontuacao = 0

	for asteriod in classes.Asteroids.sprite_list:

		# if tiro hit
		if pygame.sprite.spritecollide(asteriod, ClassName, False): 
		

			tiro.health -= 1
			pontuacao += 1
			asteriod.health -= 1

			if asteriod.health > 1 and asteriod.health < 4:
				asteriod.image = pygame.image.load('images/asteroid/asteroid2.png')
				pontuacao += 1
			elif asteriod.health == 1:
				asteriod.image = pygame.image.load('images/asteroid/asteroid3.png')	
				pontuacao += 1			
			elif asteriod.health <= 0:
				asteriod.destruir(classes.Asteroids)
				pontuacao += 10
			else:
				pass

			if tiro.health <= 0:
	
				tiro.health = 0

		# if Pojetil acerto
		if pygame.sprite.spritecollide(asteriod, classes.Projetil.sprite_list, True):
			pontuacao += 1
			asteriod.health -= 1
			if asteriod.health > 1 and asteriod.health < 4:
				asteriod.image = pygame.image.load('images/asteroid/asteroid2.png')
				pontuacao += 1
			elif asteriod.health == 1:
				asteriod.image = pygame.image.load('images/asteroid/asteroid3.png')	
				pontuacao += 1			
			elif asteriod.health <= 0:
				asteriod.destruir(classes.Asteroids)
				pontuacao += 10
			else:
				pass
			
	return pontuacao

# Colisao tiro
def colisao(tiro): 

	for gift in classes.Pacote.sprite_list:
		if pygame.sprite.spritecollide(gift, classes.Nave.sprite_list, False) \
		 or pygame.sprite.spritecollide(gift, classes.Projetil.sprite_list, True):
			gift_chance = random.randint(1, 20)
			if gift_chance <= 14:

				tiro.bala += 15
				if tiro.bala >= 1000:
					tiro.bala = 1000

			else:
				tiro.health += 5
				if tiro.health >= 100:
					tiro.health = 100
				

			gift.destruir(classes.Pacote)




