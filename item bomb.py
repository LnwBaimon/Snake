import pygame
import time
import random

# ตั้งค่าสี
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 165, 0)  # สีของระเบิด
flash_color = (255, 0, 0)  # สีสำหรับเอฟเฟคระเบิด

# ตั้งค่าหน้าจอ
dis_width = 600
dis_height = 400

# ขนาดของงู
snake_block = 10
snake_speed = 15

# กำหนดค่าเริ่มต้นของ pygame
pygame.init()
clock = pygame.time.Clock()

# กำหนดหน้าจอเกม
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game with Bomb Effect')

# ฟอนต์สำหรับแสดงข้อความ
font_style = pygame.font.SysFont(None, 50)

# ฟังก์ชันแสดงคะแนน
def Your_score(score):
    value = font_style.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# ฟังก์ชันสร้างงู
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# ฟังก์ชันแสดงข้อความ
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# ฟังก์ชันแสดงเอฟเฟคระเบิด
def bomb_effect(bombx, bomby):
    for _ in range(5):  # ทำให้จุดระเบิดเปลี่ยนสีสลับกัน 5 ครั้ง
        pygame.draw.rect(dis, flash_color, [bombx, bomby, snake_block, snake_block])
        pygame.display.update()
        time.sleep(0.1)  # เวลาแสดงสีแดง
        pygame.draw.rect(dis, orange, [bombx, bomby, snake_block, snake_block])
        pygame.display.update()
        time.sleep(0.1)  # เวลาแสดงสีส้มปกติ

# ฟังก์ชันหลักของเกม
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    score = 0  # เก็บคะแนน

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bombx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bomby = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, orange, [bombx, bomby, snake_block, snake_block])  # วาดระเบิดบนหน้าจอ
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1  # เพิ่มคะแนนเมื่อเก็บอาหาร

        if x1 == bombx and y1 == bomby:
            # สุ่มหักคะแนนระหว่าง 1 ถึง 5
            penalty = random.randint(1, 5)
            score -= penalty
            # แสดงเอฟเฟคระเบิดที่จุดระเบิด
            bomb_effect(bombx, bomby)
            # ชะงัก 1 วินาที
            time.sleep(1)
            # ย้ายระเบิดไปที่ตำแหน่งใหม่
            bombx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bomby = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            # ทำให้คะแนนไม่ติดลบ
            if score < 0:
                score = 0

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# เริ่มเกม
gameLoop()
