# Tic Tac Toe

## Table of Contents
1. [Overview](#1-overview)
2. [Features](#2-features)
3. [Requirements](#3-requirements)
4. [Installation](#4-installation)
5. [Usage](#5-usage)
6. [Gameplay](#6-gameplay)
7. [Customization](#7-customization)
8. [Troubleshooting](#8-troubleshooting)
9. [License](#9-license)
10. [Acknowledgements](#10-acknowledgements)
11. [Connect with Me](#11-connect-with-me)

## 1. Overview

This project is a simple Tic Tac Toe game built using Python's `tkinter` library. The game allows two players to play Tic Tac Toe in a graphical interface. The game highlights the winning combination or indicates a tie when the board is full.

## 2. Features

- Interactive Tic Tac Toe game for two players.
- Real-time game status display.
- Highlights the winning combination or indicates a tie.
- Option to restart the game after it ends.

## 3. Requirements

- Python 3.x
- tkinter (comes with standard Python installations)

## 4. Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
2. **Navigate to the Project Directory:**
   ```bash
   cd <project-directory>

## 5. Usage

1. **Run the Tic Tac Toe Application:**

   ```bash
   python tic_tac_toe.py

2. **Start Playing**

- The game window will open with an empty Tic Tac Toe grid.
- Players take turns clicking on the grid to place their marks (X or O).

## 6. Gameplay

- **Player Turns:** The current player is indicated at the top of the window.
- **Winning the Game:** The game automatically highlights the winning combination and declares the winner.
- **Tie Game:** If the grid is full and no player has won, the game will declare a tie and highlight the grid in yellow.
- **Restarting:** After the game ends, a "Restart Game" button will appear, allowing you to start a new game.

## 7. Customization

- **Grid Size:** The default grid is 3x3. You can adjust the code to create a larger grid.
- **Button Appearance:** Modify the font, size, and color of the buttons by changing the `tk.Button` parameters.
- **Winning/Tie Highlight:** Change the highlight colors by modifying the `highlight_winner` and `highlight_tie` functions.

## 8. Troubleshooting

- **Game Not Running:** Ensure that `tkinter` is installed and properly set up in your Python environment.
- **No Highlight on Win/Tie:** Verify that the `check_winner` function correctly identifies the winning or tie conditions.

## 9. License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 10. Acknowledgements

- `tkinter` for the GUI framework.
- Python community for the extensive libraries and support.

## 11. Connect with Me

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/shanttoosh-v-470484289/)

