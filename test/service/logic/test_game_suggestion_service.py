import pytest
from unittest import mock
from src.service.logic import game_suggestion_service


def test_create_shared_games_response_with_games():
    games = ["Game A", "Game B", "Game C"]
    result = game_suggestion_service.create_shared_games_response(games)
    assert result == "- Game A\n- Game B\n- Game C"


def test_create_shared_games_response_empty():
    games = []
    result = game_suggestion_service.create_shared_games_response(games)
    assert result == "No shared games found."


@mock.patch("src.service.logic.game_suggestion_service.get_shared_games")
@mock.patch("src.service.logic.game_suggestion_service.CONFIG")
def test_get_shared_game_suggestions_with_games(mock_config, mock_get_shared_games):
    mock_config.steam_ids = [123, 456]
    mock_get_shared_games.return_value = ["Game X", "Game Y"]
    result = game_suggestion_service.get_shared_game_suggestions()
    assert "Here are the shared games:" in result
    assert "- Game X" in result
    assert "- Game Y" in result


@mock.patch("src.service.logic.game_suggestion_service.get_shared_games")
@mock.patch("src.service.logic.game_suggestion_service.CONFIG")
def test_get_shared_game_suggestions_no_games(mock_config, mock_get_shared_games):
    mock_config.steam_ids = [123, 456]
    mock_get_shared_games.return_value = []
    result = game_suggestion_service.get_shared_game_suggestions()
    assert result == "Here are the shared games:\nNo shared games found."
