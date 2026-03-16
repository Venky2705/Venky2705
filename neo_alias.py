#!/usr/bin/env python3
"""
Neo Alias - Simple message forwarder
Listens for '@neo' or 'neo' mentions and forwards to Claude bot
"""

import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Claude bot user ID
CLAUDE_BOT_ID = "U0A2TRBH7T6"

# Initialize the Slack app (minimal setup)
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.event("message")
def handle_neo_alias(event, client, say):
    """
    Listen for 'neo' or '@neo' in messages and forward to Claude.
    This creates a simple alias: neo -> Claude bot
    """
    # Ignore bot messages
    if event.get('subtype') or event.get('bot_id'):
        return

    # Only handle channel messages (not DMs)
    if event.get('channel_type') == 'im':
        return

    text = event.get('text', '').lower()

    # Check if message starts with 'neo' or '@neo' (case insensitive)
    if text.startswith('neo ') or text.startswith('@neo'):
        user = event['user']
        channel = event['channel']
        thread_ts = event.get('thread_ts', event['ts'])

        # Extract the actual message (remove 'neo' prefix)
        original_message = event.get('text', '')
        if original_message.lower().startswith('@neo'):
            message_content = original_message[4:].strip()  # Remove '@neo'
        else:
            message_content = original_message[3:].strip()  # Remove 'neo'

        logger.info(f"Forwarding Neo request from {user}: {message_content}")

        # Forward to Claude bot with mention
        forwarded_message = f"<@{CLAUDE_BOT_ID}> {message_content}"

        # Send in the same thread
        say(
            text=forwarded_message,
            thread_ts=thread_ts
        )

        # Optionally acknowledge with a quick emoji reaction
        try:
            client.reactions_add(
                channel=channel,
                timestamp=event['ts'],
                name="robot_face"  # 🤖 emoji to show Neo received it
            )
        except Exception as e:
            logger.warning(f"Could not add reaction: {e}")


def main():
    """
    Main function to start the Neo alias bot.
    """
    # Verify required environment variables
    required_vars = ['SLACK_BOT_TOKEN', 'SLACK_APP_TOKEN', 'SLACK_SIGNING_SECRET']
    missing_vars = [var for var in required_vars if not os.environ.get(var)]

    if missing_vars:
        logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        logger.error("Please set them in your .env file or environment")
        return

    logger.info("🤖 Starting Neo Alias (forwarding to Claude)...")
    logger.info(f"All 'neo' or '@neo' messages will be forwarded to <@{CLAUDE_BOT_ID}>")

    # Start the app using Socket Mode
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()


if __name__ == "__main__":
    main()
