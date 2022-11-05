import pygame
from random import randint
from Game import Proyectil

class invasor(pygame.sprite.Sprite):
	def __init__(self, velocidad, posx, posy, distantica, imagenUno, imagenDos):
		pygame.sprite.Sprite.__init__(self);

		self.imagenA = pygame.image.load(imagenUno);
		self.imagenA = pygame.transform.scale(self.imagenA, (50, 50));
		self.imagenB = pygame.image.load(imagenDos);
		self.imagenB = pygame.transform.scale(self.imagenB, (50, 50));
		self.listaImg = [self.imagenA, self.imagenB];
		self.posImg = 0;
		self.imgInvasor = self.listaImg[self.posImg];
		self.rect = self.imgInvasor.get_rect();

		self.listaDisparo = [];
		self.velocidad = velocidad;
		self.rect.top = posy;
		self.rect.left = posx;

		self.rangoDisparo = 1;
		self.tiempoCambio = 1;

		self.derecha = True;
		#permite que no sea infinito 
		self.contador = 0;
		#se le pone un limite para descender
		self.maxDescenso = self.rect.top + 40;

		self.limiteDerecha = posx + distantica;
		self.limiteIzquieda = posx - distantica;

		self.conquista = False;

	def get_velocidad(self):
		return self.velocidad;

	def set_velocidad(self, velocidad):
		self.velocidad = velocidad;

	def dibujar(self, superficie):
		self.imgInvasor = self.listaImg[self.posImg];
		superficie.blit(self.imgInvasor, self.rect);

	def comportamiento(self,tiempo):
		if(self.conquista==False):
			self.__movimientos();
			self.__ataque();
			if self.tiempoCambio == tiempo:
				self.posImg += 1;
				self.tiempoCambio += 1;

				if(self.posImg > len(self.listaImg)-1):
					self.posImg = 0;

	def __movimientos(self):
		if(self.contador < 3):
			self.__movimientoLateral();
		else:
			self.__descenso();

	def __descenso(self):
		if(self.maxDescenso == self.rect.top):
			self.contador = 0;
			self.maxDescenso = self.rect.top + 40;
		else:
			self.rect.top += 1;


	def __movimientoLateral(self):
		if self.derecha == True:
			self.rect.left = self.rect.left + self.velocidad;
			if(self.rect.left > self.limiteDerecha):
				self.derecha = False;
				self.contador += 1;
		else:
			self.rect.left = self.rect.left - self.velocidad;
			if(self.rect.left < self.limiteIzquieda):
				self.derecha = True


	def __ataque(self):
		#si es menor a 5 dispara
		if(randint(0,100) < self.rangoDisparo):
			self.__disparo();

	def __disparo(self):
		x,y = self.rect.center;
		miProyectil = Proyectil.proyectil(x,y, "Game/img/disparob.jpg",False);
		self.listaDisparo.append(miProyectil);