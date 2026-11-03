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
    if (player_1_move == 1) and (player_2_move == 0):
        return "PLAYER 1 WINS"
    elif (player_1_move == 2) and (player_2_move == 1):
        return "PLAYER 1 WINS"
    elif (player_1_move == 0) and (player_2_move == 2):
        return "PLAYER 1 WINS"
    else:
        return "PLAYER 2 WINS"


def string_converter(player_1_move, player_2_move):
    rps = ["ROCK", "PAPER", "SCISSORSS"]
    player_1_move = rps[player_1_move]
    player_2_move = rps[player_2_move]
    return player_1_move, player_2_move


def main():
    player_1_move = random_strategy()
    player_2_move = random_strategy()
    winner = game_result(player_1_move, player_2_move)
    # player_1_thrown, player_2_thrown = string_converter(player_1_move, player_2_move)
    # print(player_1_thrown)
    # print(player_2_thrown)
    print(winner)
    pass
    # Build your playable game here, calling your functions.#pass


if __name__ == "__main__":
    main()
