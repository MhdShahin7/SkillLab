"""
Part A - Multi-Player Card Game
================================
A round-based card game where players compete by playing cards each round.
The player who wins the most rounds is the overall winner.
"""

import random


# ─── Deck Creation (list comprehension as required) ──────────────────────────

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

def create_deck():
    """Create a standard 52-card deck using list comprehension."""
    return [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]


# ─── Input Helpers ────────────────────────────────────────────────────────────

def get_number_of_players():
    """Prompt and validate the number of players (must be a positive integer >= 2)."""
    while True:
        user_input = input("\nEnter the number of players (minimum 2): ").strip()
        if not user_input.isdigit():
            print("  [!] Invalid input! Please enter a positive integer.")
            continue
        num = int(user_input)
        if num < 2:
            print("  [!] You need at least 2 players to start the game.")
            continue
        if 52 // num == 0:
            print(f"  [!] Too many players! A 52-card deck cannot be shared among {num} players.")
            continue
        return num


def get_round_winner(num_players):
    """Prompt and validate the round winner (must be 1 to num_players)."""
    while True:
        user_input = input(f"\n  Who won this round? Enter player number (1-{num_players}): ").strip()
        if not user_input.isdigit():
            print(f"  [!] Invalid input! Please enter a number between 1 and {num_players}.")
            continue
        winner = int(user_input)
        if winner < 1 or winner > num_players:
            print(f"  [!] Player number must be between 1 and {num_players}.")
            continue
        return winner


# ─── Game Logic ───────────────────────────────────────────────────────────────

def distribute_cards(deck, num_players):
    """Distribute cards evenly among players. Leftover cards are discarded."""
    cards_per_player = len(deck) // num_players
    hands = {}
    for i in range(num_players):
        start = i * cards_per_player
        hands[i + 1] = deck[start: start + cards_per_player]
    return hands, cards_per_player


def play_game():
    print("=" * 60)
    print("       WELCOME TO THE MULTI-PLAYER CARD GAME")
    print("=" * 60)

    # ── Setup ──────────────────────────────────────────────────
    num_players = get_number_of_players()

    deck = create_deck()
    random.shuffle(deck)

    hands, cards_per_player = distribute_cards(deck, num_players)
    scores = {i + 1: 0 for i in range(num_players)}

    print(f"\n[OK] {num_players} players joined. Each player gets {cards_per_player} cards.")
    print(f"   Total rounds to play: {cards_per_player}")
    print("-" * 60)

    # ── Rounds ─────────────────────────────────────────────────
    for round_num in range(1, cards_per_player + 1):
        print(f"\n{'─'*60}")
        print(f"  ROUND {round_num} of {cards_per_player}")
        print(f"{'─'*60}")

        for player in range(1, num_players + 1):
            # Randomly select one card from the player's remaining hand
            card = random.choice(hands[player])
            hands[player].remove(card)
            print(f"  Player {player} plays: {card}")

        # Get the round winner from the user
        round_winner = get_round_winner(num_players)
        scores[round_winner] += 1
        print(f"  >> Player {round_winner} wins Round {round_num}!")

    # ── Final Results ──────────────────────────────────────────
    print(f"\n{'='*60}")
    print("                   GAME OVER")
    print(f"{'='*60}")
    print("\n  Final Scores:")
    for player, score in scores.items():
        print(f"      Player {player}: {score} round(s) won")

    max_score = max(scores.values())
    winners = [p for p, s in scores.items() if s == max_score]

    print()
    if len(winners) == 1:
        print(f"  Overall Winner: Player {winners[0]} with {max_score} round(s) won!")
    else:
        tied = ", ".join(f"Player {w}" for w in winners)
        print(f"  It's a TIE between {tied} -- each won {max_score} round(s)!")

    print("=" * 60)
    print("  Thanks for playing!")
    print("=" * 60)


# ─── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    play_game()
