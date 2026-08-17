import os
import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♠ Spades", "♥ Hearts", "♦ Diamonds", "♣ Clubs"]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def create_deck():
    return [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]


def get_number_of_players():
    while True:
        val = input("  ➜ Enter number of players (2-52): ").strip()
        if not val.isdigit():
            print("  ❌ Please enter a valid number.\n")
            continue
        num = int(val)
        if num < 2:
            print("  ❌ Minimum 2 players required.\n")
            continue
        if 52 // num == 0:
            print(f"  ❌ Too many players for a 52-card deck.\n")
            continue
        return num


def get_round_winner(num_players):
    while True:
        val = input(f"\n  🏆 Who won this round? Enter player number (1-{num_players}): ").strip()
        if val.isdigit():
            winner = int(val)
            if 1 <= winner <= num_players:
                return winner
        print(f"  ❌ Invalid choice. Please enter a number from 1 to {num_players}.")


def distribute_cards(deck, num_players):
    cards_per_player = len(deck) // num_players
    hands = {i + 1: deck[i * cards_per_player : (i + 1) * cards_per_player] for i in range(num_players)}
    return hands, cards_per_player


def draw_card_box(player, card):
    lines = [
        f"┌──────────────────────────┐",
        f"│  Player {player:<2}               │",
        f"│  🃏 {card:<20} │",
        f"└──────────────────────────┘",
    ]
    return lines


def display_round_cards(played_cards):
    print("\n  CARDS PLAYED THIS ROUND:")
    print("  " + "═" * 40)
    for player, card in played_cards.items():
        print(f"   [ Player {player} ]  ──▶   {card}")
    print("  " + "═" * 40)


def display_scoreboard(scores, current_round, total_rounds):
    print(f"\n  📊 SCOREBOARD (Round {current_round}/{total_rounds})")
    print("  ┌──────────┬────────┬─────────────────────────┐")
    print("  │ Player   │ Wins   │ Progress                │")
    print("  ├──────────┼────────┼─────────────────────────┤")
    for player, score in scores.items():
        bar = "█" * score + "░" * max(0, total_rounds - score)
        if len(bar) > 23:
            bar = bar[:20] + "..."
        print(f"  │ Player {player:<1} │ {score:<6} │ {bar:<23} │")
    print("  └──────────┴────────┴─────────────────────────┘")


def play_game():
    clear_screen()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                   🎴 MULTI-PLAYER CARD GAME 🎴               ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    num_players = get_number_of_players()
    deck = create_deck()
    random.shuffle(deck)

    hands, cards_per_player = distribute_cards(deck, num_players)
    scores = {i + 1: 0 for i in range(num_players)}
    total_rounds = cards_per_player

    print(f"\n  ✅ Setup Complete: {num_players} players | {total_rounds} rounds total")
    input("\n  Press ENTER to start Round 1...")

    for round_num in range(1, total_rounds + 1):
        clear_screen()
        print(f"╔══════════════════════════════════════════════════════════════╗")
        print(f"║                   ROUND {round_num:>2} of {total_rounds:<2}                          ║")
        print(f"╚══════════════════════════════════════════════════════════════╝")

        played_cards = {}
        for player in range(1, num_players + 1):
            card = random.choice(hands[player])
            hands[player].remove(card)
            played_cards[player] = card

        display_round_cards(played_cards)

        winner = get_round_winner(num_players)
        scores[winner] += 1

        print(f"\n  🎉 Round {round_num} Winner: Player {winner}!")
        display_scoreboard(scores, round_num, total_rounds)

        if round_num < total_rounds:
            input("\n  Press ENTER for the next round...")

    clear_screen()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                     🏆 FINAL RESULTS 🏆                      ║")
    print("╚══════════════════════════════════════════════════════════════╝")

    display_scoreboard(scores, total_rounds, total_rounds)

    max_score = max(scores.values())
    winners = [p for p, s in scores.items() if s == max_score]

    print("\n  " + "★" * 45)
    if len(winners) == 1:
        print(f"   👑 OVERALL WINNER: Player {winners[0]} with {max_score} wins!")
    else:
        tied_players = ", ".join(f"Player {p}" for p in winners)
        print(f"   🤝 IT'S A TIE between {tied_players} ({max_score} wins each)!")
    print("  " + "★" * 45 + "\n")


if __name__ == "__main__":
    play_game()
