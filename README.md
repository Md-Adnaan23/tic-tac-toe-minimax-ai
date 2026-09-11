# Tic Tac Toe - Minimax AI

A classic Tic Tac Toe game built with Python's Tkinter library, featuring an **unbeatable AI opponent** powered by the Minimax algorithm. Play solo against the computer or challenge a friend in Multiplayer mode.

## Features

- 🎮 **Two Game Modes**
  - **Singleplayer** — Play against an AI opponent that never loses
  - **Multiplayer** — Play locally with a friend (X vs O)
- 🧠 **Unbeatable AI** using the Minimax algorithm — the AI looks ahead through all possible future moves to always pick the optimal one
- 🖱️ Simple, clean GUI built with Tkinter
- 🔄 **Retry** button to reset the board without restarting the app
- ❌ **Quit** button to exit the game
- 🏆 Win detection for rows, columns, and diagonals
- 🤝 Draw detection when the board fills up with no winner

## How It Works

The AI opponent uses the **Minimax algorithm**, a decision-making strategy from game theory:

1. The AI simulates every possible move it could make.
2. For each move, it recursively predicts how the game would play out if both players played optimally.
3. It scores each outcome (`+1` for an AI win, `-1` for a player win, `0` for a draw).
4. It picks the move that maximizes its best guaranteed outcome.

Because of this, the AI **never loses** — at best, you can force a draw.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)

## How to Run

```bash
git clone https://github.com/<your-username>/tic-tac-toe-minimax-ai.git
cd tic-tac-toe-minimax-ai
python tic_tac_toe.py
```

## How to Play

1. Launch the app.
2. Select **Singleplayer** (vs AI) or **Multiplayer** (2 players) from the mode buttons.
3. Click any empty cell to make your move.
4. In Singleplayer mode, the AI automatically responds after your move.
5. Click **Retry** to reset the board and play again.
6. Click **Quit Game** to close the app.

## Project Structure

```
tic-tac-toe-minimax-ai/
│
├── tic_tac_toe.py     # Main game file (Tkinter UI + game logic + Minimax AI)
└── README.md          # Project documentation
```

## Future Improvements

- [ ] Add difficulty levels (easy/medium/hard) by limiting Minimax search depth
- [ ] Add score tracking across multiple rounds
- [ ] Add sound effects
- [ ] Highlight the winning line on the board
