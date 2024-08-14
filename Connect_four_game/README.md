# 🎮 Connect Four Game

Welcome to the Connect Four game built with Python and Tkinter! This is a classic two-player game where the goal is to connect four of your pieces in a row, either horizontally, vertically, or diagonally.

## 📜 Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Play](#how-to-play)
5. [Code Overview](#code-overview)
6. [Future Enhancements](#future-enhancements)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgements](#10-acknowledgements)
10. [Connect with Me](#11-connect-with-me)

## 1. 💡 Introduction

This Connect Four game is a simple implementation using Python's Tkinter library. The game is played on a 7x6 grid where players take turns dropping their colored discs from the top into a vertical grid. The first player to connect four discs in a row wins the game!

## ✨ Features

- 🟢 **Interactive GUI:** Easy-to-use graphical interface built with Tkinter.
- 🔄 **Restart Option:** Players can restart the game at any time.
- 🥇 **Winning Detection:** The game automatically detects when a player has won or if the game ends in a draw.
- 🎨 **Colorful Design:** Player pieces are displayed in red and yellow, with a blue background representing the board.

## 2. 🛠 Installation

To run the Connect Four game on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shanttoosh/connect-four.git
2. **Navigate to the project directory:**
   ```bash
   cd connect-four
3. **Run the game:**
   ```bash
   python connect_four.py
   
## 4. 🎮 How to Play

- The game starts with Player 1 (red) and Player 2 (yellow).
- Players take turns clicking on one of the columns to drop their disc.
- The goal is to connect four discs in a row, either horizontally, vertically, or diagonally.
- The first player to connect four wins the game! If the board is full and no player has connected four, the game ends in a draw.

## 5. 🧩 Code Overview

- **ConnectFour Class:** The main class that handles the game logic, including drawing the board, handling player moves, and checking for win conditions.

### Functions:
- `draw_board()`: Draws the empty board with white circles.
- `handle_click(event)`: Handles user clicks to place pieces.
- `winning_move(piece)`: Checks if the current move is a winning move.
- `restart_game()`: Restarts the game and resets the board.

## 6. 🚀 Future Enhancements

- 🔊 **Sound Effects:** Add sound effects for placing pieces and winning.
- 💻 **AI Opponent:** Implement an AI opponent for single-player mode.
- 🌐 **Online Multiplayer:** Allow players to compete against others online.

## 7. 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to submit a pull request or open an issue.

## 8. 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 9. Acknowledgements

- `tkinter` for the GUI framework.
- Python community for the extensive libraries and support.

## 10. Connect with Me

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/shanttoosh-v-470484289/)

