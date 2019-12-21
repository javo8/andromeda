#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class collatz:
	
	def collatz(self, numero):
		try:
			if not isinstance(numero, int) or numero <= 0:
				raise ValueError
		except Exception as e:
			secuencia = [-1]
		else:
			secuencia = [int(numero)]
			while numero != 1:
				if numero % 2 == 0:
					numero = int(numero / 2)
					secuencia.append(numero)
				else:
					numero = int((numero * 3) + 1)
					secuencia.append(numero)
		
		return secuencia
