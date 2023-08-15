import pygame

class Sokoban:
    def __init__(self):
        pygame.init()
        
        self.load_images()
        self.new_game()
        
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.coins = 0
        self.moves
        self.scale = self.images[3].get_height()
        
        self.robot = self.map[2][2]

        window_height = (self.scale * self.height) + 50
        window_width = self.scale * self.width
        self.window = pygame.display.set_mode((window_width, window_height))

        pygame.display.set_caption("Sokoban")

        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["coin", "door", "monster", "robot", "wall"]:
            self.images.append(pygame.image.load("src/" + name + ".png"))

    def new_game(self):
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 1],
                    [1, 2, 3, 0, 0, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 2, 1],
                    [1, 0, 0, 1, 2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 1, 1, 1, 0, 1],
                    [1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.coins = 0
        self.moves = 0

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            self.game_over()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move(1, 0)
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.QUIT:
                exit()

    def find_robot(self ):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [3]:
                    return (y, x)
    
    def move(self, move_y, move_x):
        robot_old_y, robot_old_x = self.find_robot() 
        robot_new_y = robot_old_y + move_y
        robot_new_x = robot_old_x + move_x

        if self.map[robot_new_y][robot_new_x] == 1:
            return
        
        if self.map[robot_new_y][robot_new_x] == 0 and self.moves < 85:
                self.update_coins()
        
        if self.map[robot_new_y][robot_new_x] in [0, 4] and self.moves < 85:
            self.map[robot_old_y][robot_old_x] = 4
            self.map[robot_new_y][robot_new_x] = 3
            self.moves += 1

        if self.map[robot_new_y][robot_new_x] == 2:
            self.new_game()

    def draw_window(self):
        self.window.fill((255, 255, 255))

        for y in range(self.height):
            for x in range(self.width):
                square = self.map[y][x]
                self.window.blit(self.images[square], (x * self.scale, y * self.scale))

        game_font = pygame.font.SysFont("Arial", 24) 
        text = game_font.render(f"Coins: {self.coins}", True, (255, 0, 0)) 
        self.window.blit(text, (600, self.height * self.scale + 10))

        text = game_font.render(f"Moves: {self.moves}", True, (255, 0, 0)) 
        self.window.blit(text, (850, self.height * self.scale + 10))

        text = game_font.render("F2 = new game", True, (255, 0, 0)) 
        self.window.blit(text, (40, self.height * self.scale + 10))

        text = game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(text, (325, self.height * self.scale + 10))

        if self.moves > 84:
            text = game_font.render("Game Over! You Lost!", True, (255, 0, 0))
            self.window.blit(text, (1050, self.height * self.scale + 10))
        elif self.game_over() == False:
            text = game_font.render("Collect all Coins in 84 Moves", True, (255, 0, 0))
            self.window.blit(text, (1050, self.height * self.scale + 10))
        elif self.game_over():
            text = game_font.render("Congratulations! You Won!", True, (255, 0, 0))
            self.window.blit(text, (1050, self.height * self.scale + 10))

        pygame.display.flip()

    def update_coins(self):
        self.coins += 1

    def game_over(self):
        for y in range(self.height):
            for x in range(self.width):
                square = self.map[y][x]
                if square == 0:
                    return False
        return True

if __name__ == "__main__":
    Sokoban()