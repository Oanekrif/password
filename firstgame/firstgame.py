import pygame
import random

# المستدلات المهمة
WIDTH = 800
HEIGHT = 600
FPS = 999

# ألوان
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# إعداد النافذة
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("albarae's game")
clock = pygame.time.Clock()


# تعريف السيارة
class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.score = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        # زيادة سرعة السيارة مع مرور الوقت
        self.score += 1
        if self.score % 80 == 0:
            self.speedx += 1


# تعريف العقبات
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


# إعداد الرسومات
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
car = Car()
all_sprites.add(car)
for i in range(8):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# متغير الحالة
game_over = False

# الخطوة الأخيرة للتحسينات
font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# الحلقة الرئيسية
running = True
while running:
    # سرعة الحلقة
    clock.tick(FPS)

    # معالجة الأحداث
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # تحديث
    all_sprites.update()

    # الاصطدامات
    hits = pygame.sprite.spritecollide(car, obstacles, False)
    if hits:
        game_over = True

    # إعادة اللعب
    if game_over:
        # إعادة تعيين القيم الأولية للسيارة والعقبات
        car.rect.centerx = WIDTH / 2
        car.rect.bottom = HEIGHT - 10
        car.speedx = 0
        car.score = 0
        for obstacle in obstacles:
            obstacle.rect.x = random.randrange(WIDTH - obstacle.rect.width)
            obstacle.rect.y = random.randrange(-100, -40)
            obstacle.speedy = random.randrange(1, 8)

        # تنظيف الشاشة
        screen.fill(BLACK)

        # إعادة تعيين قيمة المتغير game_over
        game_over = False

    # الرسومات
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # رسم السكور
    draw_text(screen, "Score: " + str(car.score), 18, WIDTH / 2, 10)

    pygame.display.flip()
pygame.quit()