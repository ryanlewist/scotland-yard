import pytest
import figure


@pytest.fixture
def mr_x():
    return figure.Figure(0, 45)


@pytest.fixture
def agent():
    return figure.Figure(1, 11)


def test_mr_x_starting_position(mr_x):
    assert 45 == mr_x.position


def test_agent_starting_position(agent):
    assert 11 == agent.position
