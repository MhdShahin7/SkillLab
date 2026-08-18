import random
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    return deck


def get_number_of_players():
    while True:
        try:
            user_input = input("Enter number of players (1-52): ").strip()
            num_players = int(user_input)
            if num_players <= 0:
                print("Error: Number of players must be a positive integer (greater than 0).")
            elif num_players > 52:
                print("Error: Cannot have more than 52 players for a standard deck.")
            else:
                return num_players
        except ValueError:
            print("Error: Invalid input! Please enter a valid integer.")


def get_round_winner(num_players, round_num):
    while True:
        try:
            user_input = input(f"Enter the winner for Round {round_num} (Player 1 to {num_players}): ").strip()
            winner_num = int(user_input)
            if 1 <= winner_num <= num_players:
                return winner_num
            else:
                print(f"Error: Invalid player number! Please enter a number between 1 and {num_players}.")
        except ValueError:
            print("Error: Invalid input! Please enter a valid integer for the player number.")


def main():
    print("=" * 60)
    print("      WELCOME TO THE MULTI-PLAYER CARD GAME SIMULATOR")
    print("=" * 60)

    deck = create_deck()
    print(f"\n[+] Created standard 52-card deck using list comprehension.")
    
    random.shuffle(deck)
    print("[+] Deck shuffled randomly.")

    num_players = get_number_of_players()
    cards_per_player = len(deck) // num_players
    remaining_cards = len(deck) % num_players

    print(f"\n[+] Distributing cards evenly:")
    print(f"    - Number of Players: {num_players}")
    print(f"    - Cards per Player: {cards_per_player}")
    if remaining_cards > 0:
        print(f"    - Extra Cards set aside for fair distribution: {remaining_cards}")

    players_hands = {
        f"Player {i + 1}": deck[i * cards_per_player : (i + 1) * cards_per_player]
        for i in range(num_players)
    }

    scores = {f"Player {i + 1}": 0 for i in range(num_players)}

    print("\n" + "=" * 60)
    print("                     GAMEPLAY START")
    print("=" * 60)

    total_rounds = cards_per_player
    for round_num in range(1, total_rounds + 1):
        print(f"\n--- ROUND {round_num} of {total_rounds} ---")
        
        cards_played = {}
        for player_name, hand in players_hands.items():
            selected_card = random.choice(hand)
            hand.remove(selected_card)
            cards_played[player_name] = selected_card

        print("Cards Played This Round:")
        for player_name, card in cards_played.items():
            print(f"  * {player_name}: {card}")

        winner_num = get_round_winner(num_players, round_num)
        winner_name = f"Player {winner_num}"
        scores[winner_name] += 1
        print(f"-> Round {round_num} Winner: {winner_name}")

    print("\n" + "=" * 60)
    print("                     GAME OVER")
    print("=" * 60)
    print("\nFinal Scores:")
    for player_name, score in scores.items():
        print(f"  * {player_name}: {score} round(s) won")

    max_score = max(scores.values())
    overall_winners = [player for player, score in scores.items() if score == max_score]

    print("\n" + "*" * 60)
    if len(overall_winners) == 1:
        print(f"[WINNER] OVERALL WINNER: {overall_winners[0]} with {max_score} rounds won!")
    else:
        winners_str = ", ".join(overall_winners)
        print(f"[TIE] IT'S A TIE! Winners: {winners_str} with {max_score} rounds won each!")
    print("*" * 60 + "\n")


if __name__ == "__main__":
    main()
