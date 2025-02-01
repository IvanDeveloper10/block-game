import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Clases y funciones
def draw_text(text, size, x, y, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 50)
        self.speed = 5
    
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
    
    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

class Block:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 50), 0, 50, 50)
        self.speed = random.randint(3, 6)
    
    def move(self):
        self.rect.y += self.speed
    
    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Función principal
def main():
    clock = pygame.time.Clock()
    player = Player()
    blocks = []
    score = 0
    running = True
    
    while running:
        screen.fill(BLACK)
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        player.move(keys)
        player.draw()
        
        if random.randint(1, 30) == 1:
            blocks.append(Block())
        
        for block in blocks[:]:
            block.move()
            block.draw()
            if block.rect.colliderect(player.rect):
                running = False
            if block.rect.top > HEIGHT:
                blocks.remove(block)
                score += 1
        
        draw_text(f"Score: {score}", 30, WIDTH // 2, 30)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

# Pantalla de inicio
def start_screen():
    screen.fill(BLACK)
    draw_text("DODGE THE BLOCKS", 50, WIDTH // 2, HEIGHT // 2 - 50)
    draw_text("Presiona cualquier tecla para jugar", 30, WIDTH // 2, HEIGHT // 2 + 20)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                waiting = False

# Ejecutar el juego
start_screen()
main()
