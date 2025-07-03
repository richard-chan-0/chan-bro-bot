class DiscordBotException(Exception):
    pass


class ApiException(DiscordBotException):
    pass


class RapidApiException(ApiException):
    pass


class GameSuggestionExcepion(ApiException):
    pass


class UrbanDictionaryException(RapidApiException):
    pass
