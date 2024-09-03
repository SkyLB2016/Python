import pygame
import random

# 初始化Pygame
pygame.init()

# 设置游戏窗口大小
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

# 设置游戏标题
pygame.display.set_caption("Snake Game")

# 定义颜色常量
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 定义蛇的初始位置和长度
snake_pos = [[320, 240]]
snake_len = 10
snake_speed = 2

# 定义食物的初始位置和大小
food_pos = [random.randint(0, width - 20) * 20, random.randint(0, height - 20) * 20]
food_size = 20

# 定义计分变量
score = 0
font = pygame.font.Font(None, 36)

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_speed += 1
            elif event.key == pygame.K_DOWN:
                snake_speed -= 1
            elif event.key == pygame.K_LEFT:
                snake_speed += snake_len // 2
            elif event.key == pygame.K_RIGHT:
                snake_speed -= snake_len // 2
            if snake_speed < 1:
                snake_speed = 1
            elif snake_speed > 3:
                snake_speed = 3
    # 生成食物
    if snake_pos[-1][0] % 40 == 0 and snake_pos[-1][1] % 40 == 0:
        food_pos = [random.randint(0, width - food_size) * food_size, random.randint(0, height - food_size) * food_size]
    # 移动蛇头并判断是否吃到食物
    snake_pos.append([snake_pos[-1][0] + snake_speed, snake_pos[-1][1]])
    if snake_pos[-1][0] == food_pos[0] and snake_pos[-1][1] == food_pos[1]:
        score += 10
        food_pos = [random.randint(0, width - food_size) * food_size, random.randint(0, height - food_size) * food_size]
    else:
        snake_pos.pop()
    # 判断是否撞到边界或自身而死
    if snake_pos[-1][0] < 0 or snake_pos[-1][0] >= width or snake_pos[-1][1] < 0 or snake_pos[-1][1] >= height or len(snake_pos) > width // food_size * food_size // 2 * 2 + 2:
        running = False
    # 绘制游戏界面并显示得分信息，时间变量用于模拟帧率，使得游戏运行速度稳定在每秒60帧左右。