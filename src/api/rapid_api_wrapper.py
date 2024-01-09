from requests import get
from logging import getLogger
from src.exceptions.exceptions import RapidApiException

logger = getLogger(__name__)


async def request_rapid_api(key: str, url: str, host: str, query: dict) -> dict:
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": host,
    }
    try:
        logger.info("sending api request")
        api_response = get(url, headers=headers, params=query)
        return api_response.json()
    except Exception as err:
        logger.error(err)
        raise RapidApiException(err)
