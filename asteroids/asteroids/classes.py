import pygame, random, math

# interação com objetos
class BaseClass(pygame.sprite.Sprite): # colisao, movimentos	
	
	def __init__(self, x, y, image_str):
		pygame.sprite.Sprite.__init__(self) # acessa as variaveis

		self.image = pygame.image.load(image_str) 
		self.rect = self.image.get_rect()  
		self.rect.x = x #
		self.rect.y = y

	def destruir(self, ClassName): # remove sprites
		ClassName.sprite_list.remove(self)
		del self

class Nave(BaseClass): # tiro movimento e restrição

	sprite_list = pygame.sprite.Group() # lista tiro sprites
	def __init__(self, x, y, health, bala, image_str): 
		BaseClass.__init__(self,  x, y, image_str) 
		Nave.sprite_list.add(self) # update lista
		self.velx, self.vely = 0, 0 # movemento velocidade
		self.health = health
		self.bala = bala

	def movimento(self, screen_size): # movemento

		predict_loc_x = self.rect.x + self.velx # se move na tela
		predict_loc_y = self.rect.y + self.vely 

		if predict_loc_x < 0: 
			self.velx = 0
		elif predict_loc_x + self.rect.width > screen_size[0]:
			self.velx = 0

		if predict_loc_y < (screen_size[1] * 0.04):
			self.vely = 0
		elif predict_loc_y + self.rect.height > (screen_size[1] * 0.92):
			self.vely = 0

		self.rect.x += self.velx
		self.rect.y += self.vely

class Asteroids(BaseClass): #Cria asteroides

	sprite_list = pygame.sprite.Group() 

	def __init__(self, x, y, health, image_str):
		BaseClass.__init__(self, x, y, image_str)
		Asteroids.sprite_list.add(self) 

		self.vely = random.randint(1, 4)
		self.health = health

	def enemy_moving(self, screen_size):
		self.rect.y += self.vely

	@staticmethod
	def moving_enemy(fps, total_frames, screen_size):

		for enemy in Asteroids.sprite_list:

			enemy.enemy_moving(screen_size)
			
class Pacote(BaseClass): # # pacote de hp e bala 

	sprite_list = pygame.sprite.Group()
	def __init__(self, x, y, image_str):
		BaseClass.__init__(self, x, y, image_str)
		Pacote.sprite_list.add(self)
		self.vely = 2

	def movement(self, screen_size):
		self.rect.y += self.vely

	@staticmethod
	def moving_gift(fps, total_frames, screen_size):

		for gift in Pacote.sprite_list:

			gift.movement(screen_size)


class IniciaMenu(BaseClass): # inicio menu controle

	sprite_list = pygame.sprite.Group()
	def __init__(self, x, y, image_str):
		BaseClass.__init__(self, x, y, image_str)
		IniciaMenu.sprite_list.add(self)


class Projetil(pygame.sprite.Sprite): # porjectil
	location = 0
	sprite_list = pygame.sprite.Group() 
	normal_list = [] 
	def __init__(self, x, y, vely, tiro, image_str, fps, total_frames, screen_size):
		
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_str)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.shit = tiro
		self.vely = vely
		self.fps = fps
		self.total_frames = total_frames
		self.screen_size = screen_size

		interval = .2 
		spawn_time = fps * interval

		
		if total_frames % spawn_time != 0:
			return
		else:
			if tiro.bala > 0:
				tiro.bala -=1
			else:
				tiro.bala = 0

		Projetil.sprite_list.add(self) 
		Projetil.normal_list.append(self) 

	@staticmethod 
	def disparo():

		for projetil in Projetil.sprite_list:
			projetil.rect.y += projetil.vely

	def destruir(self): # remove  sprite

		Projetil.sprite_list.remove(self)
		Projetil.normal_list.remove(self)
		del self

class TextToScreen(object): # texto na tela

	def __init__(self, x, y, size, color):
		self.x = x
		self.y = y
		self.size = size
		self.color = color

	def text_return(self, screen, text):

		self.init_font = pygame.font.SysFont('MS serif', self.size)
		self.rendered = self.init_font.render(text, True, self.color)
		screen.blit(self.rendered, (self.x, self.y))





