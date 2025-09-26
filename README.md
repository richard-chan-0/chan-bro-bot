# Bro Bot

Bro Bot is a feature-rich Discord bot built with [discord.py](https://discordpy.readthedocs.io/en/stable/index.html). It offers a variety of functionalities, including Urban Dictionary lookups, game suggestions, greetings, and nightly notifications.

## Features

- **Urban Dictionary Lookup:** Query Urban Dictionary for slang definitions using `!define_slang <term>`.
- **Game Suggestions:** Get suggestions based on guild members' games or random game ideas.
- **Greeting Detection:** Responds to greetings in chat.
- **Good Night Notifications:** Sends a nightly message to a configured channel.
- **Custom Messaging:** Allows sending custom messages to specific channels.

## Setup

### Prerequisites

- Python 3.11+
- [Discord API Token](https://discord.com/developers/applications)
- [RapidAPI Key](https://rapidapi.com/mashape/api/urban-dictionary)

### Installation

1. Clone the repository:

   ```sh
   git clone <your-repo-url>
   ```

2. Navigate to the project directory:

   ```sh
   cd bro-bot
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables:

   ```env
   RAPID_API_KEY=your_rapidapi_key
   DISCORD_TOKEN=your_discord_token
   GENERAL_CHANNEL_ID=your_general_channel_id
   VIDEO_CHANNEL_ID=your_video_channel_id
   ```

5. Run the bot:

   ```sh
   python main.py
   ```

## Usage

- **Urban Dictionary Lookup:** Use `!define_slang <term>` in your Discord server to get Urban Dictionary definitions.
- **Game Suggestions:** Use `!suggest_game` to get a random game suggestion or suggestions based on guild members' games.
- **Greetings:** The bot will automatically respond to greetings like "hello" or "hi."
- **Nightly Notifications:** Sends a nightly "Good Night" message to a configured channel.
- **Custom Messaging:** Use specific commands to send messages to designated channels.

## Project Structure

- `src/cogs/`: Contains bot command modules (cogs) for different features, such as game suggestions and Urban Dictionary lookups.
- `src/service/`: Handles business logic and API integrations, including game suggestion and Urban Dictionary APIs.
- `src/lib/`: Includes utility functions, configuration, and exception handling.
- `test/`: Unit tests for the bot.

## Testing

Run tests with [pytest](https://docs.pytest.org/):

```sh
pytest
```

## Resources

- [discord.py documentation](https://discordpy.readthedocs.io/en/stable/index.html)
- [Urban Dictionary API on RapidAPI](https://rapidapi.com/mashape/api/urban-dictionary)

---

_Inspired by [Real Python's Discord bot tutorial](https://realpython.com/how-to-make-a-discord-bot-python/#connecting-a-bot)_
