# Feature Overview

This document provides an overview of the features implemented in Bro Bot.

## Urban Dictionary Lookup

- **Command:** `!define_slang <term>`
- **Description:** Fetches the definition of a slang term from Urban Dictionary.
- **Implementation:**
  - Located in `src/cogs/urban_dictionary.py`.
  - Uses the `rapid_api_wrapper` module in `src/lib/` to interact with the Urban Dictionary API.

## Game Suggestions

- **Command:** `!suggest_game`
- **Description:** Suggests a random game or games based on guild members' activity.
- **Implementation:**
  - Located in `src/cogs/game_suggestion.py`.
  - Uses the `game_suggestion_service` in `src/service/game_suggestion_api/`.

## Greeting Detection

- **Description:** Automatically responds to greetings like "hello" or "hi."
- **Implementation:**
  - Located in `src/cogs/greetings.py`.

## Nightly Notifications

- **Description:** Sends a nightly "Good Night" message to a configured channel.
- **Implementation:**
  - Located in `src/cogs/notification.py`.

## Custom Messaging

- **Description:** Allows sending custom messages to specific channels.
- **Implementation:**
  - Located in `src/cogs/messager.py`.

---

For more details, refer to the source code in the respective modules.
