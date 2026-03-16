# Naidu's Personal Productivity Suite

This repository contains two tools:
1. **Neo Bot** - Your personal Slack assistant (@neo)
2. **Granola Notes Importer** - Imports Granola meeting notes to Notion

---

## 🤖 Neo - Personal Slack Assistant

Neo is your personal Slack assistant that responds to @neo mentions, /neo commands, and direct messages.

### Features

- **@neo mentions** - Mention @neo in any channel to get help
- **/neo command** - Quick slash command access
- **Direct messages** - DM Neo for private assistance
- **Morning briefs** - Get daily briefings
- **Weekly reviews** - Weekly summaries and insights

### Setup Neo Bot

**1. Create the Slack App:**

- Go to https://api.slack.com/apps
- Click "Create New App" → "From an app manifest"
- Select your workspace
- Copy the contents of `slack_app_manifest.yaml` and paste it
- Click "Create"

**2. Get Your Credentials:**

After creating the app:

- **Bot Token**: Go to "OAuth & Permissions" → Copy "Bot User OAuth Token" (starts with `xoxb-`)
- **App Token**: Go to "Basic Information" → "App-Level Tokens" → "Generate Token and Scopes"
  - Name it "Socket Mode Token"
  - Add scope: `connections:write`
  - Copy the token (starts with `xapp-`)
- **Signing Secret**: Go to "Basic Information" → Copy "Signing Secret"

**3. Configure Environment Variables:**

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your credentials
nano .env  # or use your preferred editor
```

Add your tokens:
```
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
SLACK_SIGNING_SECRET=your-signing-secret
```

**4. Install Dependencies:**

```bash
pip install -r requirements.txt
```

**5. Run Neo:**

```bash
python neo_bot.py
```

You should see: `🚀 Starting Neo Slack Bot...`

**6. Test in Slack:**

- Mention @neo in a channel: `@neo hello`
- Use the slash command: `/neo help`
- Send a DM to Neo
- Open the Neo app home tab

### Using Neo

**Available Commands:**
- `@neo morning brief` - Get your morning briefing
- `@neo weekly review` - Weekly summary
- `@neo help` - Show available commands

**Examples:**
```
@neo morning brief
/neo weekly review
DM: help
```

---

## 📝 Granola Notes to Notion Importer

This tool imports Granola meeting notes from a CSV file into your Notion database "Naidu's Granola Notes".

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get your Notion credentials:**

   **Notion Token:**
   - Go to https://www.notion.so/my-integrations
   - Click "+ New integration"
   - Give it a name (e.g., "Granola Importer")
   - Copy the "Internal Integration Token"

   **Database ID:**
   - Open your "Naidu's Granola Notes" database in Notion
   - Click the "..." menu → "Connect to" → Select your integration
   - Copy the database ID from the URL:
     - URL format: `https://notion.so/[workspace]/[database_id]?v=...`
     - The database_id is the part between workspace and `?v=`

3. **Set environment variables:**
   ```bash
   export NOTION_TOKEN='your_notion_token_here'
   export NOTION_DATABASE_ID='your_database_id_here'
   ```

## Usage

Run the import script:

```bash
python push_to_notion.py
```

The script will:
- Read all entries from `granola_notes.csv`
- Create pages in your Notion database for each note
- Include the title, date, creator email, summary, and link to the original Granola note

## CSV Format

The CSV file should have these columns:
- `document_id` - Unique identifier for the Granola note
- `user_email` - Email of the creator
- `document_title` - Title of the meeting/note
- `workspace_name` - Workspace name
- `document_created` - ISO 8601 timestamp
- `summary` - Meeting summary (markdown formatted)
- `notes` - Additional notes

## Database Schema

The Notion database should have these properties:
- **Title** (title field) - Document title
- **Date** (date field) - Created date
- **Created by** (select field) - Creator email
- **Link** (URL field) - Link to original Granola note

The summary content is added as page content blocks.
