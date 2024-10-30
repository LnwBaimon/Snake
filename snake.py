import pygame
import random

pygame.init()

pygame.display.set_caption("Snake")

width = 800
hight = 600
screen = pygame.display.set_mode((width,hight))

black = (0, 0 ,0)
white = (255, 255, 255)
blue = (0, 255, 0)
green = (0, 0, 255)
red = (255, 0, 0)

font = pygame.font.Font("Graphic/PixelFont.ttf", 30)
bigfont = pygame.font.Font("Graphic/PixelFont.ttf", 32)

bg = pygame.image.load("Graphic/Bggame.png")
bg = pygame.transform.scale(bg, (800,600))

def menu():
    menu_running = True
    while menu_running:

        start_text = font.render("Start Game",True, black)
        profile_text = font.render("Profile", True, black)
        quit_text = font.render("Quit", True, black)

        start_rect = start_text.get_rect(center = (width // 2, hight // 2.3))
        profile_rect = profile_text.get_rect(center = (width // 2, hight // 1.6))
        quit_rect = quit_text.get_rect(center = (width // 2, hight // 1.2))

        screen.blit(bg, (0, 0))
        screen.blit(start_text, start_rect)
        screen.blit(profile_text, profile_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_rect.collidepoint(mouse_pos):
                        return "start"
                    elif profile_rect.collidepoint(mouse_pos):
                        return "profile"
                    elif quit_rect.collidepoint(mouse_pos):
                        return "quit"
    pygame.quit()


def profile():
    profile_running = True
    while profile_running:

        profile_bg = pygame.image.load("Graphic/Dev_profile.jpg")
        profile_bg = pygame.transform.scale(profile_bg, (500, 300))

        profile_text = font.render("Profile", True, white)
        back_text = font.render("Back", True, white)

        profile_rect = profile_text.get_rect(topleft = (20, 15))
        back_rect = back_text.get_rect(bottomleft= (50, hight - 80))

        screen.fill(black)

        screen.blit(profile_bg, (100, 100))
        screen.blit(profile_text, profile_rect)
        screen.blit(back_text, back_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_rect.collidepoint(mouse_pos):
                        return "menu"

font1 = pygame.font.Font("Graphic/PixelFont.ttf", 15)

score = 0

def show_score():
    
    score_text = font1.render(f"Score : {score}  Level : {current_level}", True, white)
    
    score_rect = score_text.get_rect(topleft=(20, 15))

    screen.blit(score_text, score_rect)

    pygame.display.update()

def over_score():

    bg_meme1 = pygame.image.load("Graphic/Meme1.png")
    bg_meme1 = pygame.transform.scale(bg_meme1, (300, 200))

    over_text = bigfont.render("Nice Try : )", True, white)
    play_again_text = font1.render("Press R to Play Again", True, white)
    home_text = font1.render("Prees M to Menu", True, white)

    over_rect = over_text.get_rect(midtop = (width / 2, hight / 8))
    play_again_rect = play_again_text.get_rect(midtop = (width / 2, hight / 4))
    home_rect = home_text.get_rect(midtop = (width / 2, hight / 3))
    bg_meme_rect = bg_meme1.get_rect(bottomright=(width - 10, hight - 10))
    
    screen.blit(over_text, over_rect)
    screen.blit(play_again_text, play_again_rect)
    screen.blit(home_text, home_rect)
    screen.blit(bg_meme1, bg_meme_rect)

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # เริ่มเกมใหม่
                    waiting = False
                    return True  # ส่งคืนค่าให้เรียกฟังก์ชันเกมใหม่
                elif event.key == pygame.K_m:  # กลับไปที่เมนู
                    waiting = False
                    return False  # ส่งคืนค่าเพื่อกลับไปที่เมนู

level_thresholds = [3, 15, 20, 25]  
current_level = 1


def game():

    global score, snake_pos, snake_body, food_pos, food_spawn, direction, change_to, current_level

    # ตั้งค่าเกม

    clock = pygame.time.Clock()
    score = 0
    previous_score = 0
    current_level = 1
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    snake_speed = 10

    food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (hight // 10)) * 10]
    food_spawn = True

    direction = "RIGHT"
    change_to = direction

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_w:
                    change_to = "UP"
                if event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_s:
                    change_to = "DOWN"
                if event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_a:
                    change_to = "LEFT"
                if event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"
                elif event.key == pygame.K_d:
                    change_to = "RIGHT"

        # ควบคุมทิศทางของงู
        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        if change_to == "DOWN" and direction != "UP":
            direction = "DOWN"
        if change_to == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change_to == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"

        # อัปเดตตำแหน่งของงู
        if direction == "UP":
            snake_pos[1] -= 10
        if direction == "DOWN":
            snake_pos[1] += 10
        if direction == "LEFT":
            snake_pos[0] -= 10
        if direction == "RIGHT":
            snake_pos[0] += 10

        # การเพิ่มขนาดของงูเมื่อเก็บอาหาร

        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            previous_score = score
            score += 1
            snake_speed+=1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (hight // 10)) * 10]
        food_spawn = True

        # ตรวจสอบการเลื่อนระดับ

        if current_level <= len(level_thresholds) and score >= level_thresholds[current_level - 1]:
            current_level += 1
            snake_speed += 5 # เพิ่มความเร็วของงูเมื่อเลื่อนระดับ
            score = 0
            snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]] 
            snake_body.append([snake_pos[0] + 10, snake_pos[1]])  
            

        
        screen.fill(black)

        for pos in snake_body: # ตัวงู
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10)) # แอปเปิ้ล

        # ตรวจสอบการชนขอบจอ
        if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= hight:
            if over_score():  # ถ้าเลือกเริ่มใหม่
                game()  # เริ่มเกมใหม่
                return  # ออกจากฟังก์ชันเพื่อไม่ให้รันต่อ
            else:
                return  # กลับไปที่เมนู
        
        # ตรวจสอบการชนตัวเอง
        if snake_pos in snake_body[1:]:
            if over_score():  # ถ้าเลือกเริ่มใหม่
                game()  # เริ่มเกมใหม่
                return  # ออกจากฟังก์ชันเพื่อไม่ให้รันต่อ
            else:
                return  # กลับไปที่เมนู

        # แสดงคะแนนและระดับ
        show_score()

        # อัปเดตหน้าจอ
        pygame.display.update()

        # ตั้งค่า FPS
        clock.tick(snake_speed)



def main():
    while True:
        menu_result = menu()
        if menu_result == "start":
            game()
        elif menu_result == "profile":
            profile()
        elif menu_result == "quit":
            break

    pygame.quit()

main()