require
'test/unit'
require
'game'


class TestGame < Test::


    Unit::TestCase


def setup
    @game

    = Game.new

    @game.figures

    [0].position = 56

    @game.figures

    [1].position = 84

    @game.figures

    [2].position = 37

    @game.figures

    [3].position = 23

    @game.figures

    [4].position = 111


end


def test_initial_setup
    assert_equal
    5,

    @game.figures.length
    @game.figures.each

    do | figure |
    assert [111, 56, 84, 37, 159, 23].include?(figure.position)


end
assert_equal
0,


@game.turns


assert_equal[],


@game.mrx_log


assert_equal[],


@game.agents_log


end


def test_moving
    assert

    @game.move(0, 91,

    :taxi)
    assert_equal
    91,

    @game.figures

    [0].position
    assert_equal
    98,

    @game.figures

    [0].tickets[:taxi]
    refute @ game.move(0, 1,: taxi)
    assert_equal
    1,

    @game.turns

    assert_equal[0],

    @game.mrx_log


end


def test_moving_agent_on_agent
    @game.figures

    [1].position = 22

    @game.figures

    [2].position = 34
    refute @ game.move(2, 22,: bus)
    end

    def test_game_over_with_turns
        @game.turns

        = 20
        assert

        @game.move(0, 42,

        :taxi)
        assert_equal
        21,

        @game.turns

        assert

        @game.over

        ?
        end

        def test_game_over_because_caught
            @game.figures

            [0].position = 77

            @game.figures

            [1].position = 94
            assert

            @game.move(1, 77,

            :bus)
            assert

            @game.over

            ?
            end

        end