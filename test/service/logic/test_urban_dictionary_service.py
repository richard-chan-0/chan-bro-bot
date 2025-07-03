import pytest
from unittest import mock
from src.service.logic import urban_dictionary_service


@pytest.mark.asyncio
async def test_get_definition_success():
    term = "cool"
    fake_messages = ["*awesome* - user1", "*great* - user2"]

    with mock.patch(
        "src.service.logic.urban_dictionary_service.get_urban_definition",
        return_value=fake_messages,
    ):
        response = await urban_dictionary_service.get_definition(term)
        assert "the term **cool** means..." in response
        assert "- *awesome* - user1" in response
        assert "- *great* - user2" in response


@pytest.mark.asyncio
async def test_get_definition_handles_discordbotexception():
    term = "fail"
    with mock.patch(
        "src.service.logic.urban_dictionary_service.get_urban_definition",
        side_effect=urban_dictionary_service.DiscordBotException("error"),
    ):
        response = await urban_dictionary_service.get_definition(term)
        assert response == "could not lookup fail"


@pytest.mark.asyncio
async def test_get_definition_empty_messages():
    term = "empty"
    with mock.patch(
        "src.service.logic.urban_dictionary_service.get_urban_definition",
        return_value=[],
    ):
        response = await urban_dictionary_service.get_definition(term)
        assert "the term **empty** means..." in response
        # Should not add any message lines
        assert response.strip().endswith("means...")
