import random


# Define your own functions here.
def random_strategy():
    return int(random.randint(0, 2))


# def player_strategy(chosen):
#     if player_strategy ==
#     for player_move in range (0, 2):

#     else:
#         print("PLEASE CHOOSE A VALID MOVE")


def game_result(player_1_move, player_2_move):
    if player_1_move == player_2_move:
        return 0
    if (player_1_move == 1) and (player_2_move == 0):
        return 1
    elif (player_1_move == 2) and (player_2_move == 1):
        return 1
    elif (player_1_move == 0) and (player_2_move == 2):
        return 1
    else:
        return 2


def string_converter(player_1_move, player_2_move):
    rps = ["ROCK", "PAPER", "SCISSORS"]
    player_1_move = rps[player_1_move]
    player_2_move = rps[player_2_move]
    return player_1_move, player_2_move


def score_counter(player_1_score, player_2_score, result):
    if result == 1:
        player_1_score += 1
    elif result == 2:
        player_2_score += 1
    return player_1_score, player_2_score


def main():
    player_1_score = 0
    player_2_score = 0
   
    results = {
        0: "DRAW",
        1: "PLAYER 1 WINS",
        2: "PLAYER 2 WINS",
    }  # I found this strategy online to convert the results easier
    
    for round_number in range(1, 6):
         player_1_move = random_strategy()
         player_2_move = random_strategy()
         winner = game_result(player_1_move, player_2_move)
         player_1_score, player_2_score = score_counter(player_1_score, player_2_score, winner)
         player_1_thrown, player_2_thrown = string_converter(player_1_move, player_2_move)
         print("ROUND", round_number)
         print("MOVES", player_1_thrown, "VS", player_2_thrown)
         print("SCORE:", player_1_score, "TO", player_2_score)
         print(results[winner])
    pass
    # Build your playable game here, calling your functions.#pass


if __name__ == "__main__":
    main()
