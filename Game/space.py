import pygame,sys
from pygame.locals import *
from random import randint
from Game import Nave
from Game import Invasor as Enemigo

class Space:
	def __init__(self, velocidad):
		#viewport
		self.velocidad = velocidad;
		self.ANCHO = 900;
		self.ALTO = 480;
		self.listaEnemigo = [];
		self.pastSpeed = self.velocidad;
		self.gameState = True;
		#Cada rectangulo tiene cuatro valores, se conforman por (posicionx, posicionY, width, height)
		#para posicionar una imagen dentro de la matriz se hace referencia a la esquuinza super izquierda
		#toman el ancho y dividen entre dos

	def get_velocidad(self):
		return self.velocidad;

	def set_velocidad(self, velocidad):
		self.velocidad = velocidad;

	def get_gameState(self):
		return self.gameState;

	#permite remover todos los disparos de la lista.
	def detenerTodo(self):
		for enemigo in self.listaEnemigo:
			for disparo in enemigo.listaDisparo:
				enemigo.listaDisparo.remove(disparo);
			enemigo.conquista = True;



	def cargarEnemigos(self):
		posx = 100;
		for x in range(1,5):
			enemigo = Enemigo.invasor(self.velocidad,posx,100,40, 'Game/img/MarcianoA.jpg', 'Game/img/MarcianoB.jpg');
			self.listaEnemigo.append(enemigo);
			posx = posx+200;

		posx = 100;
		for x in range(1,5):
			enemigo = Enemigo.invasor(self.velocidad,posx,0,40, 'Game/img/Marciano2A.jpg', 'Game/img/Marciano2B.jpg');
			self.listaEnemigo.append(enemigo);
			posx = posx + 200;

		posx = 100;
		for x in range(1,5):
			enemigo = Enemigo.invasor(self.velocidad,posx,-100,40, 'Game/img/Marciano3A.jpg', 'Game/img/Marciano3B.jpg');
			self.listaEnemigo.append(enemigo);
			posx = posx + 200;


	#FUNCION PRINCIPAL
	def SpaceInvader(self):
		pygame.init();
		ventana = pygame.display.set_mode((self.ANCHO, self.ALTO));
		pygame.display.set_caption("SPACE INVADER");
		imgFondo = pygame.image.load("Game/img/fondo.jpg");
		imgFondo = pygame.transform.scale(imgFondo, (self.ANCHO, self.ALTO));

		pygame.mixer.music.load('Game/music/fondo.mp3');
		pygame.mixer.music.play(3);


		miFuenteSistema = pygame.font.SysFont("Arial",30);
		TextoUno  = miFuenteSistema.render("Fin de juego",0,(120,100,40));
		TextoR = miFuenteSistema.render("Presiona R para reiniciar",0,(120,100,40));
		TextoDos  = miFuenteSistema.render("Has ganado",0,(120,100,40));



		#datos para el jueg
		jugador = Nave.naveEspacial(self.ANCHO, self.ALTO);
		self.cargarEnemigos();
		enJuego = True; #ganar o perder
		self.gameState = enJuego;
		


		#reloj
		reloj = pygame.time.Clock();

		while True:
			texto = "Puntos: " + str(jugador.puntos);
			TextoPuntos = miFuenteSistema.render(texto, 0, (120,100,40));
			velocidad = "Velocidad: " + str(self.velocidad);
			TextoVelocidad = miFuenteSistema.render(velocidad, 10, (120,100,40));

			reloj.tick(60);
			#se obtienen los segundos
			tiempo = pygame.time.get_ticks() // 1000;
			for evento in pygame.event.get():
				if evento.type == QUIT:
					pygame.quit();
					sys.exit();

				if enJuego == True:
					if evento.type == pygame.KEYDOWN:
						if evento.key == K_LEFT:
							jugador.movimientoIzquierda();
						elif evento.key == K_RIGHT:
							jugador.movimientoDerecha();
						elif evento.key == K_s:
							#EVENTO PARA DISPARARLE A LOS ENEMIGOS
							#print("ENTRO");
							x,y = jugador.rect.center;
							jugador.disparar(x,y);

			ventana.blit(imgFondo, (0,0));
			ventana.blit(TextoPuntos, (0,10));
			ventana.blit(TextoVelocidad, (0,50));	
			jugador.dibujar(ventana);
			if len(jugador.listaDisparo) > 0:
				for x in jugador.listaDisparo:
					x.dibujar(ventana);
					x.trayectoria();
					#elimina el disparo
					if(x.rect.top < 30):
						jugador.listaDisparo.remove(x);
					else:
						for enemigo in self.listaEnemigo:
							if(x.rect.colliderect(enemigo.rect)):
								jugador.puntos += 1;
								#print(jugador.puntos);
								self.listaEnemigo.remove(enemigo);
								jugador.listaDisparo.remove(x);
			if(len(self.listaEnemigo) > 0):
				#Cambio de velocidad
				if self.pastSpeed != self.velocidad:
					for check in self.listaEnemigo:
						check.set_velocidad(self.velocidad);
					self.pastSpeed = self.velocidad;
				#Fin


				for enemigo in self.listaEnemigo:
					enemigo.comportamiento(tiempo);
					enemigo.dibujar(ventana);
					if(enemigo.rect.colliderect(jugador.rect)):
						jugador.destruccion();
						enJuego = False;
						self.detenerTodo();
					if len(enemigo.listaDisparo) > 0:
						for x in enemigo.listaDisparo:
							x.dibujar(ventana);
							x.trayectoria();

							if(x.rect.colliderect(jugador.rect)):
								jugador.destruccion();
								enJuego = False;
								self.detenerTodo();

							if(x.rect.top > 900):
								enemigo.listaDisparo.remove(x);
							else:
								for disparo in jugador.listaDisparo:
									if x.rect.colliderect(disparo.rect):
										jugador.listaDisparo.remove(disparo);
										enemigo.listaDisparo.remove(x);

			if enJuego == False:
				self.gameState = enJuego;
				pygame.mixer.music.fadeout(3000);
				ventana.blit(TextoUno, (self.ANCHO/2-70,300));
				ventana.blit(TextoR, (self.ANCHO/2-140,335));
				
				if evento.type == pygame.KEYDOWN:
					#print(evento.type == pygame.KEYDOWN);
					if evento.key == K_r:
						for x in range(4):
							#print("Entro");
							for enemigo in self.listaEnemigo:
								for x in enemigo.listaDisparo:
									enemigo.listaDisparo.remove(x);
								self.listaEnemigo.remove(enemigo);
						self.SpaceInvader();

			if len(self.listaEnemigo) == 0:
				pygame.mixer.music.fadeout(3000);
				ventana.blit(TextoDos, (self.ANCHO/2-70,300));
				ventana.blit(TextoR, (self.ANCHO/2-140,335));
				self.detenerTodo();

			pygame.display.update();

	#SpaceInvader();

