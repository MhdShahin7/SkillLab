import os
import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

os.system("")

CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"
CLR_RED = "\033[91m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_CYAN = "\033[96m"
CLR_MAGENTA = "\033[95m"
CLR_WHITE = "\033[97m"
CLR_GRAY = "\033[90m"

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = [("♠ Spades", CLR_CYAN), ("♥ Hearts", CLR_RED), ("♦ Diamonds", CLR_RED), ("♣ Clubs", CLR_GREEN)]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def create_deck():
    return [f"{rank} of {suit_name}" for suit_name, _ in SUITS for rank in RANKS]


def get_number_of_players():
    while True:
        val = input(f"  {CLR_YELLOW}➜ Enter number of players (2-52): {CLR_RESET}").strip()
        if not val.isdigit():
            print(f"  {CLR_RED}❌ Please enter a valid number.{CLR_RESET}\n")
            continue
        num = int(val)
        if num < 2:
            print(f"  {CLR_RED}❌ Minimum 2 players required.{CLR_RESET}\n")
            continue
        if 52 // num == 0:
            print(f"  {CLR_RED}❌ Too many players for a 52-card deck.{CLR_RESET}\n")
            continue
        return num


def get_round_winner(num_players):
    while True:
        val = input(f"\n  {CLR_YELLOW}🏆 Who won this round? Enter player number (1-{num_players}): {CLR_RESET}").strip()
        if val.isdigit():
            winner = int(val)
            if 1 <= winner <= num_players:
                return winner
        print(f"  {CLR_RED}❌ Invalid choice. Please enter a number from 1 to {num_players}.{CLR_RESET}")


def distribute_cards(deck, num_players):
    cards_per_player = len(deck) // num_players
    hands = {i + 1: deck[i * cards_per_player : (i + 1) * cards_per_player] for i in range(num_players)}
    return hands, cards_per_player


def display_round_cards(played_cards):
    print(f"\n  {CLR_BOLD}{CLR_CYAN}Cards played this round:{CLR_RESET}")
    print(f"  {CLR_GRAY}" + "─" * 38 + f"{CLR_RESET}")
    for player, card in played_cards.items():
        print(f"    Player {player}  ──▶  {CLR_BOLD}{CLR_WHITE}{card}{CLR_RESET}")
    print(f"  {CLR_GRAY}" + "─" * 38 + f"{CLR_RESET}")


def display_scoreboard(scores, current_round, total_rounds):
    print(f"\n  {CLR_BOLD}{CLR_MAGENTA}📊 SCOREBOARD (Round {current_round}/{total_rounds}){CLR_RESET}")
    print(f"  {CLR_GRAY}┌──────────┬────────┬─────────────────────────┐{CLR_RESET}")
    print(f"  {CLR_GRAY}│{CLR_RESET} {CLR_BOLD}Player{CLR_RESET}   {CLR_GRAY}│{CLR_RESET} {CLR_BOLD}Wins{CLR_RESET}   {CLR_GRAY}│{CLR_RESET} {CLR_BOLD}Progress{CLR_RESET}                {CLR_GRAY}│{CLR_RESET}")
    print(f"  {CLR_GRAY}├──────────┼────────┼─────────────────────────┤{CLR_RESET}")

    for player, score in scores.items():
        filled = "█" * score
        empty = "░" * max(0, total_rounds - score)
        bar = f"{CLR_GREEN}{filled}{CLR_GRAY}{empty}{CLR_RESET}"
        text_bar = filled + empty
        if len(text_bar) > 23:
            bar = f"{CLR_GREEN}{filled[:20]}...{CLR_RESET}"

        print(f"  {CLR_GRAY}│{CLR_RESET} Player {player:<1} {CLR_GRAY}│{CLR_RESET} {CLR_CYAN}{score:<6}{CLR_RESET} {CLR_GRAY}│{CLR_RESET} {bar:<32} {CLR_GRAY}│{CLR_RESET}")

    print(f"  {CLR_GRAY}└──────────┴────────┴─────────────────────────┘{CLR_RESET}")


def play_game():
    clear_screen()
    print(f"{CLR_CYAN}╔══════════════════════════════════════════════════════════════╗{CLR_RESET}")
    print(f"{CLR_CYAN}║{CLR_RESET}             {CLR_BOLD}{CLR_WHITE}🎴  MULTI-PLAYER CARD GAME  🎴{CLR_RESET}               {CLR_CYAN}║{CLR_RESET}")
    print(f"{CLR_CYAN}╚══════════════════════════════════════════════════════════════╝{CLR_RESET}")
    print()

    num_players = get_number_of_players()
    deck = create_deck()
    random.shuffle(deck)

    hands, cards_per_player = distribute_cards(deck, num_players)
    scores = {i + 1: 0 for i in range(num_players)}
    total_rounds = cards_per_player

    print(f"\n  {CLR_GREEN}✅ Setup Complete:{CLR_RESET} {num_players} players | {total_rounds} rounds total")
    input(f"\n  {CLR_GRAY}Press ENTER to start Round 1...{CLR_RESET}")

    for round_num in range(1, total_rounds + 1):
        clear_screen()
        print(f"{CLR_CYAN}╔══════════════════════════════════════════════════════════════╗{CLR_RESET}")
        print(f"{CLR_CYAN}║{CLR_RESET}                   {CLR_BOLD}{CLR_YELLOW}ROUND {round_num:>2} of {total_rounds:<2}{CLR_RESET}                          {CLR_CYAN}║{CLR_RESET}")
        print(f"{CLR_CYAN}╚══════════════════════════════════════════════════════════════╝{CLR_RESET}")

        played_cards = {}
        for player in range(1, num_players + 1):
            card = random.choice(hands[player])
            hands[player].remove(card)
            played_cards[player] = card

        display_round_cards(played_cards)

        winner = get_round_winner(num_players)
        scores[winner] += 1

        print(f"\n  {CLR_BOLD}{CLR_GREEN}🎉 Round {round_num} Winner: Player {winner}!{CLR_RESET}")
        display_scoreboard(scores, round_num, total_rounds)

        if round_num < total_rounds:
            input(f"\n  {CLR_GRAY}Press ENTER for the next round...{CLR_RESET}")

    clear_screen()
    print(f"{CLR_YELLOW}╔══════════════════════════════════════════════════════════════╗{CLR_RESET}")
    print(f"{CLR_YELLOW}║{CLR_RESET}                     {CLR_BOLD}{CLR_WHITE}🏆 FINAL RESULTS 🏆{CLR_RESET}                      {CLR_YELLOW}║{CLR_RESET}")
    print(f"{CLR_YELLOW}╚══════════════════════════════════════════════════════════════╝{CLR_RESET}")

    display_scoreboard(scores, total_rounds, total_rounds)

    max_score = max(scores.values())
    winners = [p for p, s in scores.items() if s == max_score]

    print(f"\n  {CLR_YELLOW}" + "★" * 52 + f"{CLR_RESET}")
    if len(winners) == 1:
        print(f"   {CLR_BOLD}{CLR_GREEN}👑 OVERALL WINNER: Player {winners[0]} with {max_score} wins!{CLR_RESET}")
    else:
        tied_players = ", ".join(f"Player {p}" for p in winners)
        print(f"   {CLR_BOLD}{CLR_YELLOW}🤝 IT'S A TIE between {tied_players} ({max_score} wins each)!{CLR_RESET}")
    print(f"  {CLR_YELLOW}" + "★" * 52 + f"{CLR_RESET}\n")


if __name__ == "__main__":
    play_game()
