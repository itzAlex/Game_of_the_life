# /usr/env/bin python
# coding: utf-8

import random
import itertools
import os, time

clear = lambda: os.system('clear')

class GameOfLife(object):
	
	def __init__(self, filas, columnas):
		
		self.filas = filas
		self.columnas = columnas
		
		fila_vida = lambda: [random.randint(0, 1) for n in range(self.columnas)]
		self.juego = [fila_vida() for n in range(self.filas)]
	
	def __str__(self):
		
		juego = ''
		
		for fila in self.juego:
			for celula in fila:
				juego += '@ ' if celula else '. '
			juego += '\n'
		return juego
	
	def vecinos(self, nf, nc):
		
		distancias_vecinos = list(
			set(itertools.permutations([-1, -1, 1, 1, 0], 2))
			)
		
		fuera_de_juego = lambda x, y: not (x in range(self.filas) and y in range(self.columnas))
		
		vecinos = 0
		
		for dist_fila, dist_columna in distancias_vecinos:
			if not fuera_de_juego(nf + dist_fila, nc + dist_columna):
				vecinos += 1 if self.juego[nf + dist_fila][nc + dist_columna] else 0
		
		return vecinos
	
	def recorrer(self):
		
		for nf in range(self.filas):
			for nc in range(self.columnas):
				vecinos = self.vecinos(nf, nc)
				
				if vecinos < 2 or vecinos > 3:
					self.juego[nf][nc] = 0
				elif vecinos == 3:
					self.juego[nf][nc] = 1

def main():
	clear()
	
	print("..............................")
	print("Bienvenido al juego de la vida")
	print("..............................")
	
	filas, columnas = int(input("Filas -- ")), int(input("Columnas -- "))
	
	juego = GameOfLife(filas, columnas)
	
	while True:
		clear()
		print(juego)
		juego.recorrer()
		time.sleep(0.5)

if __name__ == '__main__':
	main()
