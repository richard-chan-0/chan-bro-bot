# Discord Bot

A Discord bot built with [discord.py](https://discordpy.readthedocs.io/en/stable/index.html) that provides Urban Dictionary lookups, greetings, and nightly notifications.

## Features

- **Urban Dictionary Lookup:** Query Urban Dictionary for slang definitions using `!define_slang <term>`.
- **Greeting Detection:** Responds to greetings in chat.
- **Good Night Notifications:** Sends a nightly message to a configured channel.

---

## AWS Lambda & SAM Deployment

This project can be deployed as a serverless application using AWS Lambda and the AWS Serverless Application Model (SAM).

### Prerequisites

- Python 3.11+
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) configured with your credentials
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [Discord API Token](https://discord.com/developers/applications)
- [RapidAPI Key](https://rapidapi.com/mashape/api/urban-dictionary)

### Lambda Layer Setup

To include shared dependencies (like `requests`) in a Lambda Layer:

1. Create the layer directory structure:
   ```sh
   mkdir -p src/layer/python
   ```
2. Install your dependencies into the layer:
   ```sh
   python3.11 -m pip install -r requirements.txt -t src/layer/python
   ```
   _(You can create a separate requirements file for just the layer if needed.)_

### Build and Deploy with SAM

1. **Build the application:**

   ```sh
   sam build
   ```

2. **Deploy the application:**

   ```sh
   sam deploy --guided
   ```

   - The first time, SAM will prompt you for stack name, AWS region, and other settings.
   - After deployment, SAM will output the API endpoint URL.

3. **Update Environment Variables:**
   - You can set or update environment variables in `template.yaml` under `Environment`.

### Project Structure (Serverless)

- `template.yaml`: AWS SAM template defining Lambda functions, layers, and API Gateway.
- `src/lambda/`: Lambda handler code.
- `src/layer/python/`: Python dependencies for the Lambda Layer.

---

## Local Development

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

---

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
- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)

---

\*Inspired by [Real Python's Discord bot tutorial](https://realpython.com/how-to-make-a-discord-bot-python/#connecting-a-bot)
