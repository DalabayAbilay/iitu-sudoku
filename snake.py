import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(-1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            body_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen,(216,180,34),body_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy

    def add_block(self):
        self.new_block = True
#---------------------------------------------------------------------
class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
#------------------------------------------------------------
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.speed()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()  
        self.snake.draw_snake()
        self.draw_score()
        self.draw_level()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row%2 == 0:
                for col in range(cell_number):
                    if col%2 == 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col%2 != 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_number*cell_size-60)
        score_y = int(cell_size*cell_number-40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect, 2)

    def draw_level(self):
        level_surface = game_font.render("level", True,(56,74,12))
        number_surface = game_font.render(str((len(self.snake.body) - 3)//5), True,(56,74,12))
        level_x = int(cell_size+15)
        level_y = int(cell_size*cell_number-40)
        level_rect = level_surface.get_rect(center = (level_x,level_y))
        number_rect = number_surface.get_rect(midleft = (level_rect.right+5,level_rect.centery))
        bgl_rect = pygame.Rect(level_rect.left-3,number_rect.top-5,level_rect.width + number_rect.width + 10,number_rect.height+10)

        pygame.draw.rect(screen,(167,209,61),bgl_rect)
        screen.blit(level_surface,level_rect)
        screen.blit(number_surface,number_rect)
        pygame.draw.rect(screen,(56,74,12),bgl_rect, 2)
    
    def speed(self):
        if (len(self.snake.body) - 3)//5 > level:
            pass
#-------------------------------------------------
pygame.init()
cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number,cell_number*cell_size))
clock = pygame.time.Clock()
apple = pygame.transform.scale(pygame.image.load("images/apple2.png"), (35,35)).convert_alpha()
game_font = pygame.font.Font("images/Papernotes Sketch.ttf", 25)
FPS = 150
level = 0

game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,FPS)
#---------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
            if (len(game.snake.body) - 3)//5 > level:
                FPS -= 100
                level += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1,0)

    screen.fill((175,215,70))
    game.draw_elements()
    pygame.display.update()
    clock.tick(60)