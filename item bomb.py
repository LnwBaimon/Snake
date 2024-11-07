import pygame
import time
import random

# ตั้งค่าสี
white = (255, 255, 255)
blue = (50, 153, 213)
orange = (255, 165, 0)  # สีของระเบิด
flash_color = (255, 0, 0)  # สีสำหรับเอฟเฟคระเบิด

# ตั้งค่าหน้าจอ
dis_width = 600
dis_height = 400

# ขนาดของระเบิด
bomb_size = 10
bomb_interval = 3000  # ระยะเวลาเพิ่มระเบิดใหม่ทุกๆ 3 วินาที

# กำหนดค่าเริ่มต้นของ pygame
pygame.init()
clock = pygame.time.Clock()

# กำหนดหน้าจอเกม
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Increasing Bombs with Effects')

# ฟังก์ชันแสดงเอฟเฟคระเบิด
def bomb_effect(bombx, bomby):
    for _ in range(5):  # ทำให้จุดระเบิดเปลี่ยนสีสลับกัน 5 ครั้ง
        pygame.draw.rect(dis, flash_color, [bombx, bomby, bomb_size, bomb_size])
        pygame.display.update()
        time.sleep(0.1)  # เวลาแสดงสีแดง
        pygame.draw.rect(dis, orange, [bombx, bomby, bomb_size, bomb_size])
        pygame.display.update()
        time.sleep(0.1)  # เวลาแสดงสีส้มปกติ

# ฟังก์ชันหลักของเกม
def gameLoop():
    game_over = False

    # ลิสต์เก็บตำแหน่งระเบิดทั้งหมด
    bombs = [[round(random.randrange(0, dis_width - bomb_size) / 10.0) * 10.0,
              round(random.randrange(0, dis_height - bomb_size) / 10.0) * 10.0]]

    last_bomb_time = pygame.time.get_ticks()  # เวลาในการเพิ่มระเบิดครั้งล่าสุด

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # เติมพื้นหลังด้วยสีฟ้า
        dis.fill(blue)

        # วาดระเบิดทั้งหมดบนหน้าจอ
        for bomb in bombs:
            pygame.draw.rect(dis, orange, [bomb[0], bomb[1], bomb_size, bomb_size])

        # เพิ่มระเบิดใหม่ทุกๆ ระยะเวลา (เช่น ทุก 8000 มิลลิวินาที)
        current_time = pygame.time.get_ticks()
        if current_time - last_bomb_time > bomb_interval:
            bombx = round(random.randrange(0, dis_width - bomb_size) / 10.0) * 10.0
            bomby = round(random.randrange(0, dis_height - bomb_size) / 10.0) * 10.0
            bombs.append([bombx, bomby])
            last_bomb_time = current_time

            # แสดงเอฟเฟคระเบิดที่ระเบิดล่าสุด
            bomb_effect(bombx, bomby)

        pygame.display.update()
        clock.tick(80)

    pygame.quit()
    quit()

# เริ่มเกม
gameLoop()
