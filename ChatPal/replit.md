# Discord Bot

## Overview

A Python-based Discord bot built with the discord.py library that provides basic command handling and interactive features for Discord servers. The bot implements a modular command system with prefix-based commands (`!`) and includes utility, information, and entertainment features. It's designed as a foundation that can be easily extended with additional functionality.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Architecture
- **Modular Design**: Separation of concerns with distinct files for bot logic (`bot.py`), command definitions (`commands.py`), and entry point (`main.py`)
- **Event-Driven Architecture**: Uses discord.py's event system to handle messages, bot readiness, and command execution
- **Command Framework**: Built on discord.py's `commands.Bot` extension for structured command handling with automatic help generation

### Bot Configuration
- **Intents System**: Configured with `message_content` intent enabled for reading message content
- **Command Prefix**: Uses `!` as the command prefix with case-insensitive command matching
- **Error Handling**: Comprehensive logging system with both file and console output

### Command System
- **Prefix Commands**: Traditional `!command` format for user interactions
- **Built-in Help**: Automatic help command generation with per-command documentation
- **Response Patterns**: Mix of simple text responses and rich Discord embeds for enhanced user experience

### Logging and Monitoring
- **Multi-Level Logging**: File-based logging (`discord_bot.log`) combined with console output
- **Bot Status Tracking**: Monitors guild connections, latency, and system information
- **Error Tracking**: Comprehensive error logging with traceback information

## External Dependencies

### Discord API
- **discord.py**: Primary library for Discord API interaction and bot functionality
- **Discord Developer Portal**: Bot token management and application configuration

### System Dependencies
- **Python Standard Library**: asyncio for async operations, logging for system monitoring, os for environment variables
- **dotenv**: Environment variable management for secure token storage
- **psutil**: System resource monitoring for bot information commands
- **platform**: System information gathering

### Configuration
- **Environment Variables**: `DISCORD_BOT_TOKEN` for secure bot authentication
- **Bot Permissions**: Requires message content intent and basic bot permissions in Discord servers