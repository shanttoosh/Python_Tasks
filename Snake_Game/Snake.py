import tkinter as tk
import random

# Constants
WIDTH = 600
HEIGHT = 400
SNAKE_SIZE = 20
INITIAL_SNAKE_LENGTH = 5
MOVE_INCREMENT = 20
UPDATE_DELAY = 100

# Setting up the environment
class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = None
        self.food = None
        self.direction = 'Right'
        self.next_direction = 'Right'
        self.score = 0
        self.running = True

        self.init_game()
        self.root.bind("<KeyPress>", self.change_direction)
        self.update_game()

    def init_game(self):
        self.snake = [(SNAKE_SIZE * i, 0) for i in range(INITIAL_SNAKE_LENGTH, 0, -1)]
        self.food = self.create_food()
        self.draw_snake()
        self.draw_food()

    def create_food(self):
        while True:
            x = random.randint(0, (WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE
            y = random.randint(0, (HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + SNAKE_SIZE, segment[1] + SNAKE_SIZE, fill="green", tag="snake")

    def draw_food(self):
        self.canvas.delete("food")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + SNAKE_SIZE, self.food[1] + SNAKE_SIZE, fill="red", tag="food")

    def change_direction(self, event):
        key = event.keysym
        directions = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        if key in directions and key != directions[self.direction]:
            self.next_direction = key

    def move_snake(self):
        head_x, head_y = self.snake[0]
        self.direction = self.next_direction

        if self.direction == 'Left':
            head_x -= MOVE_INCREMENT
        elif self.direction == 'Right':
            head_x += MOVE_INCREMENT
        elif self.direction == 'Up':
            head_y -= MOVE_INCREMENT
        elif self.direction == 'Down':
            head_y += MOVE_INCREMENT

        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

    def check_collisions(self):
        head_x, head_y = self.snake[0]
        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT) or (self.snake[0] in self.snake[1:]):
            self.running = False

    def check_food(self):
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.create_food()
            self.draw_food()
            self.score += 1

    def update_game(self):
        if self.running:
            self.move_snake()
            self.check_collisions()
            self.check_food()
            self.draw_snake()
            self.root.after(UPDATE_DELAY, self.update_game)
        else:
            self.game_over()

    def game_over(self):
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=('Helvetica', 24))
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2 + 30, text=f"Score: {self.score}", fill="white", font=('Helvetica', 16))
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2 + 60, text="Press 'R' to Restart", fill="white", font=('Helvetica', 16))
        self.root.bind("<KeyPress-r>", self.restart_game)

    def restart_game(self, event):
        self.canvas.delete("all")
        self.direction = 'Right'
        self.next_direction = 'Right'
        self.score = 0
        self.running = True
        self.init_game()
        self.update_game()

# To Run the game
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
