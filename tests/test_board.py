import pytest
import board


@pytest.fixture
def game_board():
    return board.Board()


def test_routes_from_158(game_board):
    routes_from_158_list = [
        {'station': 141, 'ticket': 'taxi'},
        {'station': 142, 'ticket': 'taxi'},
        {'station': 157, 'ticket': 'taxi'},
        {'station': 159, 'ticket': 'taxi'}
    ]
    assert routes_from_158_list == game_board.routes_from(158)


def test_routes_from_111(game_board):
    routes_from_111_list = [
        {'station': 67, 'ticket': 'underground'},
        {'station': 79, 'ticket': 'underground'},
        {'station': 100, 'ticket': 'bus'},
        {'station': 110, 'ticket': 'taxi'},
        {'station': 112, 'ticket': 'taxi'},
        {'station': 124, 'ticket': 'taxi'},
        {'station': 124, 'ticket': 'bus'},
        {'station': 153, 'ticket': 'underground'},
        {'station': 163, 'ticket': 'underground'}
    ]
    assert routes_from_111_list == game_board.routes_from(111)
