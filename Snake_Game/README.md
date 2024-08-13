# Snake Game

This is a simple Snake Game implemented using Python and the tkinter library. The objective of the game is to control the snake to eat food, which increases the snake's length. The game ends if the snake collides with the walls or itself.

## Table of Contents
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Code Explanation](#code-explanation)
  - [Constants](#constants)
  - [SnakeGame Class](#snakegame-class)
  - [Game Initialization](#game-initialization)
  - [Game Logic](#game-logic)
  - [Collision Detection](#collision-detection)
  - [Game Over](#game-over)
  - [Restart Game](#restart-game)
- [Running the Game](#running-the-game)

## Installation

1. Ensure you have Python installed on your system.
2. You can run the game using the tkinter library, which is included with most Python installations.

## How to Play

- Use the arrow keys to control the snake's direction.
- The snake moves continuously in the last direction you pressed.
- The game ends when the snake collides with the walls or itself.
- You can restart the game by pressing the 'R' key after a game over.

## Code Explanation

### Constants

- `WIDTH`, `HEIGHT`: Dimensions of the game window.
- `SNAKE_SIZE`: Size of each segment of the snake.
- `INITIAL_SNAKE_LENGTH`: Starting length of the snake.
- `MOVE_INCREMENT`: The distance the snake moves per update.
- `UPDATE_DELAY`: Time delay between each movement update.

### SnakeGame Class

This class handles the initialization, updating, and logic of the Snake Game.

### Game Initialization

- **Canvas Setup**: The game window is created with the specified width and height.
- **Snake Creation**: The snake is initialized with a specified number of segments.
- **Food Creation**: A piece of food is randomly placed on the canvas.

### Game Logic

- **Movement**: The snake's head moves in the direction of the key pressed. The body follows the head.
- **Direction Change**: The direction is updated based on the arrow keys pressed.

### Collision Detection

- **Wall Collision**: The game checks if the snake's head has collided with the boundaries of the game window.
- **Self Collision**: The game checks if the snake has collided with itself.

### Game Over

- When the game ends, a "Game Over" message is displayed along with the final score.
- The game can be restarted by pressing the 'R' key.

### Restart Game

- The game resets to its initial state, allowing the player to start over.

## Running the Game

To run the game, execute the following command:

```bash
python snake_game.py

