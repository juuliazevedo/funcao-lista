# -*- coding: utf-8 -*-
"""teste.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bBUFt_zaHsbbBmOe49I2TT-ZIU2S6yOw
"""

numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
media(numeros)
med = media(numeros)
print("Média: ", med)
NumeroMaior = max(numeros)
NumeroMenor = min(numeros)
print("Maior número: ", NumeroMaior)
print("Menor número", NumeroMenor)
contpar = 0
for n in numeros:
  if n % 2 == 0:
    contpar += 1
print("Quantidade de números pares: ", contpar)

