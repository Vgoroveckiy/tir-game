import random

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/pistol.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")  # Загрузка изображения цели
# Изменение размера изображения до 80x80 пикселей
target_width = 80
target_height = 80

target_img = pygame.transform.scale(target_img, (target_width, target_height))
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0

running = True
clock = pygame.time.Clock()  # Добавляем часы для управления частотой обновления экрана

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (
                mouse_x >= target_x
                and mouse_x <= target_x + target_width
                and mouse_y >= target_y
                and mouse_y <= target_y + target_height
            ):
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))

    pygame.display.update()
    clock.tick(60)  # Устанавливаем частоту обновления экрана в 60 кадров в секунду

pygame.quit()
