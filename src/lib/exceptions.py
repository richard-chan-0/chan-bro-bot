class DiscordBotException(Exception):
    pass


class RapidApiException(DiscordBotException):
    pass


class UrbanDictionaryException(RapidApiException):
    pass
