"""
Part A - Multi-Player Card Game
================================
A round-based card game where players compete by playing cards each round.
The player who wins the most rounds is the overall winner.
"""

import random
import os


# ─── Helpers ──────────────────────────────────────────────────────────────────

def clear():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Wait for the user to press Enter before continuing."""
    input("\n  [ Press Enter to continue... ]")

def banner(title):
    """Print a styled section banner."""
    print("\n" + "=" * 50)
    print(f"   {title}")
    print("=" * 50)

def show_scoreboard(scores, round_num, total_rounds):
    """Display current scores for all players."""
    print("\n  +----------------------+")
    print(f"  |  SCOREBOARD  (Round {round_num}/{total_rounds})")
    print("  +----------------------+")
    for player, score in scores.items():
        bar = "█" * score + "░" * (total_rounds - score)
        print(f"  |  Player {player}: {score} pts  {bar}")
    print("  +----------------------+")


# ─── Deck ─────────────────────────────────────────────────────────────────────

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

def create_deck():
    """Create a standard 52-card deck using list comprehension."""
    return [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]


# ─── Input Validation ─────────────────────────────────────────────────────────

def get_number_of_players():
    while True:
        val = input("  How many players? (min 2): ").strip()
        if not val.isdigit():
            print("  [!] Enter a whole number.\n")
            continue
        n = int(val)
        if n < 2:
            print("  [!] Need at least 2 players.\n")
        elif 52 // n == 0:
            print(f"  [!] Too many players for a 52-card deck.\n")
        else:
            return n

def get_round_winner(num_players):
    while True:
        val = input(f"\n  >> Who won? Enter player number (1-{num_players}): ").strip()
        if not val.isdigit():
            print(f"  [!] Enter a number between 1 and {num_players}.")
            continue
        w = int(val)
        if 1 <= w <= num_players:
            return w
        print(f"  [!] Must be between 1 and {num_players}.")


# ─── Card Distribution ────────────────────────────────────────────────────────

def distribute_cards(deck, num_players):
    cards_each = len(deck) // num_players
    hands = {i + 1: deck[i * cards_each:(i + 1) * cards_each] for i in range(num_players)}
    return hands, cards_each


# ─── Main Game ────────────────────────────────────────────────────────────────

def play_game():
    clear()
    banner("MULTI-PLAYER CARD GAME")
    print("""
  HOW TO PLAY:
  - Each player gets equal cards from a shuffled deck.
  - Every round, one random card is drawn from each player.
  - YOU decide who wins the round (based on the cards shown).
  - Player with the most round wins at the end is the champion!
    """)

    num_players = get_number_of_players()

    deck = create_deck()
    random.shuffle(deck)
    hands, cards_each = distribute_cards(deck, num_players)
    scores = {i + 1: 0 for i in range(num_players)}
    total_rounds = cards_each

    clear()
    banner("GAME STARTING")
    print(f"\n  Players  : {num_players}")
    print(f"  Cards ea : {cards_each}")
    print(f"  Rounds   : {total_rounds}")
    pause()

    # ── Round Loop ──────────────────────────────────────────────
    for round_num in range(1, total_rounds + 1):
        clear()
        banner(f"ROUND  {round_num}  of  {total_rounds}")

        print("\n  Cards played this round:")
        print("  " + "-" * 30)
        for player in range(1, num_players + 1):
            card = random.choice(hands[player])
            hands[player].remove(card)
            print(f"    Player {player}  -->  {card}")
        print("  " + "-" * 30)

        winner = get_round_winner(num_players)
        scores[winner] += 1
        print(f"\n  ★  Player {winner} wins this round!")

        show_scoreboard(scores, round_num, total_rounds)

        if round_num < total_rounds:
            pause()

    # ── Final Result ─────────────────────────────────────────────
    clear()
    banner("GAME OVER — FINAL RESULTS")

    print("\n  Final Scores:")
    print("  " + "-" * 30)
    for player, score in scores.items():
        print(f"    Player {player}  :  {score} round(s) won")
    print("  " + "-" * 30)

    max_score = max(scores.values())
    champions = [p for p, s in scores.items() if s == max_score]

    print()
    if len(champions) == 1:
        print(f"  WINNER --> Player {champions[0]}  ({max_score} rounds won)")
    else:
        tied = " & ".join(f"Player {p}" for p in champions)
        print(f"  TIE --> {tied}  ({max_score} rounds each)")

    print("\n  Thanks for playing!\n")


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    play_game()
