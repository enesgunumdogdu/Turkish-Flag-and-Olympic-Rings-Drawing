# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 11:08:04 2023

@author: enesgunumdogdu
"""
import pygame
import math
import numpy as np
import matplotlib.pyplot as plt

# kodu başlattım
pygame.init()

# renkleri tanımladım
RED = (213, 0, 0)
WHITE = (255, 255, 255)

# çerçeve ölçüsü
G = 600
window = pygame.display.set_mode((G, G))
pygame.display.set_caption("Türk Bayrağı")

# bayrağın ölçü parametreleri
A = G / 2
B = G / 2
C = G / 16
D = 2 * G / 5
E = G / 3
F = G / 4
L = 3 * G / 2
M = L / 30

#arka plan rengi
window.fill(RED)

# beyaz yıldızın ölçü hesaplaması ve çizimi
star_points = []
for i in range(5):
    angle_deg = 72 * i - 90
    angle_rad = math.radians(angle_deg)
    x = G / 2 + F / 2 * math.cos(angle_rad)
    y = G / 2 + F / 2 * math.sin(angle_rad)
    star_points.append((x+200, y))
    x = G / 2 + F / 4 * math.cos(angle_rad + math.pi / 5)
    y = G / 2 + F / 4 * math.sin(angle_rad + math.pi / 5)
    star_points.append((x+200, y))
pygame.draw.polygon(window, WHITE, star_points)

# beyaz daire
circle_center = (G/4+100, G/2)
pygame.draw.circle(window, WHITE, circle_center, G/4)

# kırmızı daire
pygame.draw.circle(window, RED, (int(G*3/4)-165, int(G/2)), int(G/5))

# bayrak çizgisi
hoist_rect = pygame.Rect(0, 0, M, G)
pygame.draw.rect(window, WHITE, hoist_rect)

# görüntüyü güncelle
pygame.display.update()

# sonsuz döngüye al
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
