Connect 4 Game Using Adversarial Search (Minimax)
1. Project Overview

This project implements the Connect 4 game where a human player competes against an intelligent AI agent.
The AI agent uses an adversarial search strategy, specifically the Minimax algorithm, to make optimal decisions in a competitive, turn-based environment.

The project aims to demonstrate practical understanding of game environments, decision-making under competition, and AI search algorithms.

2. Environment Description

The game is a two-player, turn-based, deterministic, zero-sum environment.

One player is a human, and the other is an AI agent.

The objective is to connect four discs in a row (horizontally, vertically, or diagonally).

The game ends when one player wins or when the board is completely filled (draw).

3. Adversarial Search Strategy

Algorithm Used: Minimax

The AI simulates future game states by exploring possible moves for both players.

The Minimax algorithm selects the move that maximizes the AI’s score while minimizing the opponent’s score.

The algorithm evaluates terminal states such as:

Win for AI

Win for Human

Draw

4. System Architecture

The project is organized in a modular and clean-code structure using Python classes and functions.

File Structure:

├── board.py          # Game board representation and rules

├── minimax.py        # Minimax algorithm and AI decision logic

├── game.py           # Graphical User Interface and game flow

├── main.py           # Entry point to run the game

├── README.md         # Project description and usage

├── Connect4_Project_Documentation.docx

5. Game Implementation Details
   
5.1 Board Module (board.py)

Represents the Connect 4 grid.

Validates moves.

Detects winning conditions.

Manages game state updates.

5.2 AI Module (minimax.py)

Implements the Minimax algorithm.

Evaluates game states using a scoring function.

Determines the optimal move for the AI agent.

5.3 GUI Module (game.py)

Implements a graphical interface using Tkinter.

Handles user input (mouse clicks).

Displays game status (win, loss, draw).

Allows restarting the game.

5.4 Main Module (main.py)

Launches the game and initializes the GUI.

6. Input Validation

The system prevents invalid moves such as selecting a full column.

User inputs are validated to ensure correct and stable gameplay.

7. How to Run the Project

Ensure Python 3.8 or higher is installed.

Open a terminal in the project directory.

Run the following command:

python main.py

8. Technologies Used

Python

Tkinter (Graphical User Interface)

Git & GitHub (Version Control)

9. Team Members

Abdullah Mostafa Barakat

Abdullah Sayed Awad

10. Conclusion

This project successfully applies adversarial search concepts to a real-world game scenario.
By implementing the Minimax algorithm, the AI agent demonstrates strategic reasoning and optimal decision-making in a competitive environment.
