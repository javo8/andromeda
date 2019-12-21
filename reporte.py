#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import requests
import json

def collatz(numero):
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

valores = ['-3', '0', '1', '20', '[20]', '{20}', '20.0', '20.1', 'hola', '']

correctos = 0
incorrectos = 0

for valor in valores:
    print("Probando " + str(valor) + "... ", end='')
    try:
        r = requests.post('http://localhost:8080/calcular_collatz', data = valor, headers = {'Content-Type': 'application/json'})
        if collatz(int(valor)) == r.json():
            print('OK')
            correctos = correctos + 1
        else:
            print('Falla')
            incorrectos = incorrectos + 1
    except Exception as e:
        print('Falla')
        incorrectos = incorrectos + 1

print(u'Total de intentos: ' + str(incorrectos + correctos))

plt.pie([correctos, incorrectos], labels=['OK', 'Falla'], colors=['green', 'orange'], autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()
