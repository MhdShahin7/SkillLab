# Part A: Multi-Player Card Game Simulator

## Problem Description
This program simulates a round-based multi-player card game. Each player receives an equal number of cards from a standard 52-card deck, and cards are played over multiple rounds. In each round, a card is randomly selected from each player's hand, cards played are displayed, and the user inputs the round winner. The overall winner is announced at the end based on total rounds won.

## Technical Features & Implementation
- **Deck Creation**: Uses Python **list comprehension** to generate all 52 cards (13 ranks × 4 suits).
- **Shuffling**: Shuffles the deck randomly using `random.shuffle()`.
- **Fair Distribution**: Distributes cards equally among all input players.
- **Random Card Selection**: Selects a random card from each player's hand every round.
- **Input Validation**: Validates user inputs for player counts and round winner selections, ensuring robust error handling.
- **Score Tracking**: Tracks round wins per player and determines single winners or ties upon game completion.

## How to Run
Run the game using Python 3:
```bash
python Part_A/card_game.py
```
