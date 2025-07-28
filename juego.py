
import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# --- Configuración de la pantalla ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Coches Pygame")

# --- Colores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
ROAD_GREEN = (46, 204, 113) # Un verde más vibrante para la carretera

# --- Fuentes ---
font = pygame.font.Font(None, 36) # Fuente para la puntuación y mensajes
game_over_font = pygame.font.Font(None, 72)

# --- Clases del Juego ---

class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Crear una superficie para el coche del jugador
        self.image = pygame.Surface([30, 60])
        self.image.fill(BLUE) # Coche azul
        # Dibujar detalles del coche
        pygame.draw.rect(self.image, WHITE, [5, 10, 20, 10]) # Ventana delantera
        pygame.draw.rect(self.image, WHITE, [5, 40, 20, 10]) # Ventana trasera
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 50
        self.speed = 5

    def update(self):
        # Obtener el estado de las teclas presionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Mantener el coche dentro de los límites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Crear una superficie para el obstáculo
        self.image = pygame.Surface([30, 60])
        # Colores aleatorios para los obstáculos
        colors = [RED, YELLOW, GRAY, GREEN]
        self.color = random.choice(colors)
        self.image.fill(self.color)
        # Dibujar detalles del obstáculo
        pygame.draw.rect(self.image, YELLOW, [5, 5, 5, 5]) # Luz izquierda
        pygame.draw.rect(self.image, YELLOW, [self.image.get_width() - 10, 5, 5, 5]) # Luz derecha

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -50) # Aparece fuera de la pantalla por arriba
        self.speed = random.randrange(3, 6) # Velocidad aleatoria

    def update(self):
        self.rect.y += self.speed
        # Si el obstáculo sale de la pantalla, lo reiniciamos arriba
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -50)
            self.speed = random.randrange(3, 6) # Reiniciar velocidad
            return True # Indica que se ha pasado un obstáculo
        return False

# --- Funciones de Dibujo ---

def draw_road_lines(offset):
    line_color = WHITE
    line_thickness = 5
    line_length = 40
    line_gap = 60

    # Dibujar línea central
    for i in range(-2, int(SCREEN_HEIGHT / (line_length + line_gap)) + 2):
        y_pos = (i * (line_length + line_gap) + offset) % (SCREEN_HEIGHT + line_length) - line_length
        pygame.draw.rect(screen, line_color, [SCREEN_WIDTH // 2 - line_thickness // 2, y_pos, line_thickness, line_length])

def draw_text(surface, text, color, x, y, font_obj):
    text_surface = font_obj.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

# --- Bucle Principal del Juego ---

def game_loop():
    player_car = PlayerCar()
    all_sprites = pygame.sprite.Group()
    obstacles_group = pygame.sprite.Group()

    all_sprites.add(player_car)

    # Crear algunos obstáculos iniciales
    for _ in range(5):
        obstacle = Obstacle()
        obstacles_group.add(obstacle)
        all_sprites.add(obstacle)

    score = 0
    road_offset = 0
    road_speed = 5 # Velocidad de desplazamiento de la carretera

    clock = pygame.time.Clock()
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r: # Reiniciar con 'R'
                    game_loop() # Reiniciar el juego
                    return # Salir del bucle actual
                if not game_over and event.key == pygame.K_ESCAPE: # Salir con 'ESC'
                    running = False

        if not game_over:
            # Actualizar sprites
            all_sprites.update()

            # Desplazar la carretera
            road_offset = (road_offset + road_speed) % (SCREEN_HEIGHT + 100) # +100 para un desplazamiento suave

            # Comprobar si los obstáculos han pasado y aumentar la puntuación
            for obstacle in list(obstacles_group): # Iterar sobre una copia para modificar la original
                if obstacle.update(): # Si el obstáculo ha pasado la pantalla
                    score += 1
                    # Aumentar la velocidad de los obstáculos y la carretera gradualmente
                    
            def increase_speed():
                    for obs in obstacles_group:
                        obs.speed += 0.05
                    global road_speed  # Acceder a la variable global
                    road_speed += 0.01


            # Detección de colisiones
            if pygame.sprite.spritecollideany(player_car, obstacles_group):
                game_over = True

            # --- Dibujar ---
            screen.fill(ROAD_GREEN) # Fondo de la carretera
            draw_road_lines(road_offset) # Dibujar líneas de la carretera

            all_sprites.draw(screen) # Dibujar todos los sprites

            # Mostrar puntuación
            score_text = font.render(f"Puntuación: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

        else:
            # Pantalla de Game Over
            screen.fill(DARK_GRAY)
            draw_text(screen, "¡Juego Terminado!", RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, game_over_font)
            draw_text(screen, f"Puntuación Final: {score}", WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, font)
            draw_text(screen, "Presiona 'R' para Reiniciar", WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70, font)
            draw_text(screen, "Presiona 'ESC' para Salir", WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, font)


        pygame.display.flip() # Actualizar la pantalla

        # Controlar la velocidad de fotogramas
        clock.tick(60) # 60 FPS

    pygame.quit()
    sys.exit()

# Iniciar el juego
if __name__ == "__main__":
    game_loop()