import random
MOVES = ["rock", "paper", "scissors"]

def basic_ai():
    """Basic strategy: randomly pick a move."""
    return random.choice(MOVES)


def frequency_ai(history):
    """
    Predict the player's next move by choosing the move 
    that beats the player's most frequent past move.
    """
    if not history:
        return basic_ai()
    
    most_common = max(history, key=history.count)
    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"


def pattern_ai(history):
    """
    VERY simple sequence detection:
    If the last two moves repeat, assume they'll repeat again.
    """
    if len(history) < 3:
        return frequency_ai(history)

    if history[-1] == history[-2]:
        repeat = history[-1]
        if repeat == "rock":
            return "paper"
        elif repeat == "paper":
            return "scissors"
        else:
            return "rock"

    return frequency_ai(history)


def choose_ai_move(history):
    """Choose AI strategy (you can change this)."""
    # Use pattern + frequency strategy
    return pattern_ai(history)


def determine_winner(player, ai):
    if player == ai:
        return "tie"
    if (
        (player == "rock" and ai == "scissors") or
        (player == "scissors" and ai == "paper") or
        (player == "paper" and ai == "rock")
    ):
        return "player"
    return "ai"
def play_game():
    player_score = 0
    ai_score = 0
    history = []

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player = input("\nEnter your move (rock/paper/scissors or 'quit'): ").lower()

        if player == "quit":
            print("\nThanks for playing!")
            break

        if player not in MOVES:
            print("Invalid input. Try again.")
            continue
        ai = choose_ai_move(history)
        history.append(player)
        winner = determine_winner(player, ai)

        print(f"AI chose: {ai}")
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("AI wins this round!")
            ai_score += 1
        print(f"Score → You: {player_score} | AI: {ai_score}")
play_game()
