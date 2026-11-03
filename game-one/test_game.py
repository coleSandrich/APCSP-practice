import pytest
import game

# Replace this template with at least three tests per game function:
# def test_describe_the_case():
# assert game.your_function(chosen_input) == expected_result

# equal distribution of 0, 1, 2
# returns an integer, not a string or float
# returns values only in the range


def test_random_strategy_in_range():
    for i in range(0, 100, 1):
        result = game.random_strategy()
        assert result == 0 or result == 1 or result == 2


def test_random_strategy_distribution():
    counts = [0, 0, 0]
    for i in range(0, 10000, 1):
        result = game.random_strategy()
        counts[result] += 1
    assert counts == pytest.approx([3333, 3333, 3333], rel=0.05)


def test_random_strategy_is_int():
    result = game.random_strategy()
    assert result == int(result)


def test_game_result_draw():
    assert game.game_result(0, 0) == 0
    assert game.game_result(1, 1) == 0
    assert game.game_result(2, 2) == 0

def test_p1_winning_conditions():
    assert game.game_result(0, 2) == 1
    assert game.game_result(2, 1) == 1
    assert game.game_result(1, 0) == 1




if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
