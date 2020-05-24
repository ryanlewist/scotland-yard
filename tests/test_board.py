import pytest
import board
import os

# Change working directory to project folder in order to be able to import yml files
os.chdir('..')

@pytest.fixture
def sy_board():
    return board.Board()


def test_routes_from_158(sy_board):
    routes_from_158_list = [
        {'station': 141, 'ticket': 'taxi'},
        {'station': 142, 'ticket': 'taxi'},
        {'station': 157, 'ticket': 'taxi'},
        {'station': 159, 'ticket': 'taxi'}
    ]
    assert routes_from_158_list == sy_board.routes_from(158)


def test_routes_from_111(sy_board):
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
    assert routes_from_111_list == sy_board.routes_from(111)
