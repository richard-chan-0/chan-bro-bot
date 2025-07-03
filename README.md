# Discord Bot

A Discord bot built with [discord.py](https://discordpy.readthedocs.io/en/stable/index.html) that provides Urban Dictionary lookups, greetings, and nightly notifications.

## Features

- **Urban Dictionary Lookup:** Query Urban Dictionary for slang definitions using `!define_slang <term>`.
- **Greeting Detection:** Responds to greetings in chat.
- **Good Night Notifications:** Sends a nightly message to a configured channel.

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

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with the following variables:

   ```
   RAPID_API_KEY=your_rapidapi_key
   DISCORD_TOKEN=your_discord_token
   GENERAL_CHANNEL_ID=your_general_channel_id
   VIDEO_CHANNEL_ID=your_video_channel_id
   ```

4. Run the bot:
   ```sh
   python main.py
   ```

## Usage

- Use `!define_slang <term>` in your Discord server to get Urban Dictionary definitions.
- The bot will automatically respond to greetings and send nightly good night messages.

## Project Structure

- `src/cogs/`: Discord bot command modules (cogs)
- `src/service/`: Business logic and API integrations
- `src/lib/`: Configuration and exception handling
- `test/`: Unit tests

## Testing

Run tests with [pytest](https://docs.pytest.org/):

```sh
pytest
```

## Resources

- [discord.py documentation](https://discordpy.readthedocs.io/en/stable/index.html)

- [Urban Dictionary API on RapidAPI](https://rapidapi.com/mashape/api/urban-dictionary)

---

\*Inspired by [Real Python's Discord bot tutorial](https://realpython.com/how-to-make-a-discord-bot-python/#connecting-a-bot)
