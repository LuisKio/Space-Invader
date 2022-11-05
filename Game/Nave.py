import pygame
from Game import Proyectil

#NAVE ESPACIAL
class naveEspacial(pygame.sprite.Sprite):
	def __init__(self, ANCHO, ALTO):
		pygame.sprite.Sprite.__init__(self);
		self.ImageNave = pygame.image.load("Game/img/nave.png");
		self.ImageNave = pygame.transform.scale(self.ImageNave, (103, 66));

		self.rect = self.ImageNave.get_rect();
		self.rect.centerx = ANCHO / 2;
		self.rect.centery = ALTO - 30;

		#lista de disparos
		self.listaDisparo = [];
		self.vida = True;

		#movimiento
		self.velocidad = 20;

		#puntos
		self.puntos = 0;

		self.sonidoDisparo = pygame.mixer.Sound('Game/music/disparo.wav');

	def movimientoDerecha(self):
		self.rect.right += self.velocidad;
		self.__movimiento();

	def movimientoIzquierda(self):
		self.rect.left -= self.velocidad;
		self.__movimiento();


	def __movimiento(self):
		if(self.vida == True):
			if self.rect.left <= 0:
				self.rect.left = 0;
			elif(self.rect.right > 870):
				self.rect.right = 840;

	def disparar(self, x, y):
		miProyectil = Proyectil.proyectil(x,y, "Game/img/disparoa.jpg", True);
		self.listaDisparo.append(miProyectil);
		self.sonidoDisparo.play();

	def destruccion(self):
		self.vida = False;
		self.velocidad = 0;


	def dibujar(self,superficie):
		superficie.blit(self.ImageNave, self.rect);