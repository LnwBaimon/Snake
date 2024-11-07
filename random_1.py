import pygame
import random 

class Item:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.randomize_position()  

    def randomize_position(self):
        
        self.rect.x = random.randint(0, 800 - self.rect.width)
        self.rect.y = random.randint(0, 600 - self.rect.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Item:
    def __init__(self, image_paths):
        
        image_path = random.choice(image_paths)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.randomize_position()

    def randomize_position(self):
        self.rect.x = random.randint(0, 800 - self.rect.width)
        self.rect.y = random.randint(0, 600 - self.rect.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

pygame.init()
screen = pygame.display.set_mode((800, 600))

item_images = ["item", "item_speed.png", "item_score.png"]

item = Item(item_images)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    item.draw(screen)
    pygame.display.flip()

pygame.quit()