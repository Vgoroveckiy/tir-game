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
font = pygame.font.Font(None, 36)  # Инициализация шрифта для отображения очков

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
                score += 1  # Увеличиваем счет при попадании
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))

    # Отображение счета с контрастным цветом
    text_color = tuple(255 - c for c in color)  # Инвертируем цвет фона
    score_text = font.render(f"Очки: {score}", True, text_color)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)  # Устанавливаем частоту обновления экрана в 60 кадров в секунду

pygame.quit()
