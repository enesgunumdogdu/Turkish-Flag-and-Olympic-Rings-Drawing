# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 12:25:24 2023

@author: enesgunumdogdu
"""

import pygame
import math
import numpy as np
import matplotlib.pyplot as plt

#kodu başlatma
pygame.init()

# çerçeve ölçüleri ve başlığı
G = 600
window = pygame.display.set_mode((G, G-100))
pygame.display.set_caption("Olimpiyat Halkaları")

# renkleri önceden tanımladım
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 195, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#arkaplan rengini ayarladım
window.fill(WHITE)

# dairelerin kalınlık ve merkezini tek seferde tanımladım
R = G/6
thickness = 12

# merkez hesaplaması
x1, y1 = G/3 - R/2, G/2 - R*2
x2, y2 = G/2, G/2 - R*2
x3, y3 = G*2/3 + R/2, G/2 - R*2
x4, y4 = G/4 + R, G/2 - R
x5, y5 = G*3/4 - R, G/2 - R
x6, y6 = G/2, G/2

# dairelerin çizimii
pygame.draw.circle(window, BLUE, (int(x1)-20, int(y1)+50), int(R*0.8), thickness)
pygame.draw.circle(window, BLACK, (int(x2), int(y2)+50), int(R*0.8), thickness)
pygame.draw.circle(window, RED, (int(x3)+20, int(y3)+50), int(R*0.8), thickness)
pygame.draw.circle(window, YELLOW, (int(x4)-35, int(y4)+30), int(R*0.8), thickness)
pygame.draw.circle(window, GREEN, (int(x5)+35, int(y5)+30), int(R*0.8), thickness)


# güncelleme
pygame.display.update()

# sonsuz döngü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
