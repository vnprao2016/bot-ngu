# Discord Bot

A Python Discord bot with basic command handling and message response functionality.

## Features

- 🤖 Basic command framework with prefix system (`!`)
- 💬 Message handling and response system
- 📊 Server and bot information commands
- 🎲 Fun commands (dice rolling, coin flip, quotes)
- 🛡️ Error handling and logging
- 🔧 Environment variable configuration
- 📝 Comprehensive logging system

## Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `!hello` | Greet the bot | `!hello` |
| `!ping` | Check bot latency | `!ping` |
| `!info` | Display bot information | `!info` |
| `!serverinfo` | Display server information | `!serverinfo` |
| `!roll` | Roll dice | `!roll 6` or `!roll 2d6` |
| `!flip` | Flip a coin | `!flip` |
| `!quote` | Get inspirational quote | `!quote` |
| `!about` | About this bot | `!about` |
| `!help` | Show help message | `!help` or `!help <command>` |

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Discord Developer Account

### 1. Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to "Bot" section in the left sidebar
4. Click "Add Bot"
5. Copy the bot token (you'll need this later)
6. Under "Privileged Gateway Intents", enable:
   - Message Content Intent (required for reading message content)

### 2. Invite Bot to Server

1. In the Developer Portal, go to "OAuth2" > "URL Generator"
2. Select these scopes:
   - `bot`
   - `applications.commands`
3. Select these bot permissions:
   - Send Messages
   - Use Slash Commands
   - Read Message History
   - Add Reactions
   - Embed Links
4. Copy the generated URL and open it in your browser
5. Select your server and authorize the bot

### 3. Install Dependencies

```bash
pip install discord.py python-dotenv
