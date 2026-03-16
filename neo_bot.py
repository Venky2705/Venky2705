#!/usr/bin/env python3
"""
Neo - Personal Assistant Slack Bot
Responds to @neo mentions and /neo slash commands
"""

import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Slack app
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


# Response handler for @neo mentions
@app.event("app_mention")
def handle_mention(event, say, client):
    """
    Handle @neo mentions in channels and threads.
    """
    user = event['user']
    text = event['text']
    channel = event['channel']
    thread_ts = event.get('thread_ts', event['ts'])

    # Remove the bot mention from the text
    message = text.split('>', 1)[-1].strip()

    logger.info(f"Received mention from {user}: {message}")

    # Process the request
    response = process_neo_request(message, user)

    # Send response in thread
    say(
        text=response,
        thread_ts=thread_ts
    )


# Direct message handler
@app.event("message")
def handle_direct_message(event, say, logger):
    """
    Handle direct messages to Neo.
    """
    # Ignore bot messages and threaded messages handled elsewhere
    if event.get('subtype') or event.get('bot_id'):
        return

    # Only respond to DMs (channel type is 'im')
    if event.get('channel_type') != 'im':
        return

    user = event['user']
    text = event.get('text', '')

    logger.info(f"Received DM from {user}: {text}")

    # Process the request
    response = process_neo_request(text, user)

    say(response)


# Slash command handler
@app.command("/neo")
def handle_neo_command(ack, command, respond):
    """
    Handle /neo slash command.
    Usage: /neo <command>
    """
    ack()

    user = command['user_id']
    text = command.get('text', '')

    logger.info(f"Received /neo command from {user}: {text}")

    # Process the request
    response = process_neo_request(text, user)

    respond(response)


def process_neo_request(message, user_id):
    """
    Process Neo assistant requests.
    This is where you'd integrate with your AI/assistant logic.

    Args:
        message: The user's message/request
        user_id: The Slack user ID

    Returns:
        Response message
    """
    message = message.lower().strip()

    # Default responses for common requests
    if not message or message in ['help', 'hello', 'hi', 'hey']:
        return """👋 Hello! I'm Neo, your personal assistant.

Here's how you can interact with me:
• **@neo [request]** - Mention me in any channel
• **/neo [request]** - Use the slash command
• **DM me** - Send me a direct message

*Common commands:*
• `morning brief` - Get your morning briefing
• `weekly review` - Weekly summary
• `help` - Show this help message

How can I assist you today?"""

    elif 'morning brief' in message or 'morning' in message:
        return """🌅 *Good morning!* Here's your brief:

📅 *Today's Schedule:*
• No meetings scheduled yet

📝 *Recent Updates:*
• Granola notes integration active
• Notion database synced

💡 *Suggestions:*
• Review yesterday's notes
• Plan your day's priorities

Need anything else?"""

    elif 'weekly review' in message or 'weekly' in message:
        return """📊 *Weekly Review*

Here's a summary of your week:

✅ *Completed:*
• Granola notes to Notion integration
• Slack bot setup (@neo handle)

📈 *Stats:*
• Notes imported: Check your Notion database
• Active integrations: Granola, Notion, Slack

🎯 *Next Steps:*
• Configure additional Neo features
• Set up automated workflows

Great week! 🎉"""

    else:
        return f"""I received your request: "{message}"

I'm still learning! Here are some things I can help with:
• `morning brief` - Daily briefing
• `weekly review` - Weekly summary
• `help` - Show available commands

What would you like me to do?"""


# App home opened event
@app.event("app_home_opened")
def handle_app_home_opened(client, event, logger):
    """
    Handle when a user opens the App Home.
    """
    user_id = event["user"]

    try:
        client.views_publish(
            user_id=user_id,
            view={
                "type": "home",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Welcome to Neo! 👋*\n\nYour personal assistant is ready to help."
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*How to use Neo:*\n• Mention @neo in any channel\n• Use the /neo slash command\n• Send me a direct message"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Quick Commands:*\n• `@neo morning brief`\n• `@neo weekly review`\n• `@neo help`"
                        }
                    }
                ]
            }
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


def main():
    """
    Main function to start the Slack bot.
    """
    # Verify required environment variables
    required_vars = ['SLACK_BOT_TOKEN', 'SLACK_APP_TOKEN', 'SLACK_SIGNING_SECRET']
    missing_vars = [var for var in required_vars if not os.environ.get(var)]

    if missing_vars:
        logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        logger.error("Please set them in your .env file or environment")
        return

    logger.info("🚀 Starting Neo Slack Bot...")

    # Start the app using Socket Mode
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()


if __name__ == "__main__":
    main()
