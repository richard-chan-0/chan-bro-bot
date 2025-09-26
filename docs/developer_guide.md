# Developer Guide

Welcome to the Bro Bot Developer Guide! This document provides useful information for developers who want to contribute to or extend the bot.

## Setting Up the Development Environment

1. **Clone the Repository:**

   ```sh
   git clone <your-repo-url>
   ```

2. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   Create a `.env` file in the project root with the following variables:

   ```env
   RAPID_API_KEY=your_rapidapi_key
   DISCORD_TOKEN=your_discord_token
   GENERAL_CHANNEL_ID=your_general_channel_id
   VIDEO_CHANNEL_ID=your_video_channel_id
   ```

4. **Run the Bot Locally:**
   ```sh
   python main.py
   ```

## Project Structure

- `src/cogs/`: Contains bot command modules (cogs) for different features.
- `src/service/`: Handles business logic and API integrations.
- `src/lib/`: Includes utility functions, configuration, and exception handling.
- `test/`: Unit tests for the bot.

## Adding a New Feature

1. **Create a New Cog:**

   - Add a new file in the `src/cogs/` directory.
   - Define a class that inherits from `commands.Cog`.

   Example:

   ```python
   from discord.ext import commands

   class NewFeature(commands.Cog):
       def __init__(self, bot):
           self.bot = bot

       @commands.command()
       async def new_command(self, ctx):
           await ctx.send("This is a new feature!")

   def setup(bot):
       bot.add_cog(NewFeature(bot))
   ```

2. **Register the Cog:**

   - Update the bot initialization code to load the new cog.

3. **Test the Feature:**
   - Write unit tests in the `test/` directory.
   - Run tests using `pytest`.

## Debugging Tips

- Use `print()` statements or logging to debug issues.
- Check the Discord Developer Portal for bot permissions and token validity.
- Use the `discord.py` documentation for reference.

## Useful Resources

- [discord.py documentation](https://discordpy.readthedocs.io/en/stable/index.html)
- [Urban Dictionary API on RapidAPI](https://rapidapi.com/mashape/api/urban-dictionary)

---

Happy coding!
