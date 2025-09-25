def create_shared_games_response(games: list) -> str:
    if not games:
        return "No shared games found."
    response = ""
    for game in games:
        response += f"- {game}\n"
    return response.strip()
