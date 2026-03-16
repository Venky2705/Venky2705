# Naidu's Personal Productivity Suite

This repository contains two tools:
1. **Neo Bot** - Your personal Slack assistant (@neo)
2. **Granola Notes Importer** - Imports Granola meeting notes to Notion

---

## 🤖 Neo - Personal Slack Assistant

**Multiple Setup Options Available!**

Choose the approach that fits your needs:
- **Option A (Full Bot)** - Complete standalone bot with full features
- **Option B (Keyword Integration)** - Integration with existing Claude bot
- **Option C (Simple Alias)** - ⭐ **RECOMMENDED** - Quickest setup, no bot registration needed!

Neo provides quick access to Claude (`<@U0A2TRBH7T6>`) for personal assistance tasks.

### Available Features

- **Quick access to Claude** - Use `@neo` instead of `<@U0A2TRBH7T6>`
- **Workflow shortcuts** - ⚡ Lightning menu shortcuts
- **Morning briefs** - Get daily briefings
- **Weekly reviews** - Weekly summaries and insights
- **Custom commands** - Extensible command system

---

## 📋 Setup Options

### ⭐ Option C: Simple Alias (RECOMMENDED - 5 minutes)

**Best for:** Quick setup, no coding required, uses existing Claude bot

This is the **easiest and fastest** method. No Slack app registration needed!

**[📖 See detailed setup guide: NEO_ALIAS_SETUP.md](NEO_ALIAS_SETUP.md)**

**Quick Start:**
1. Open Slack → Workspace menu → **Tools** → **Workflow Builder**
2. Create → **Shortcut** → Name: "Ask Neo"
3. Add step → **Send a message** → Text: `<@U0A2TRBH7T6> {{user_input}}`
4. Publish!

**Usage:**
- Click ⚡ lightning bolt → "Ask Neo" → Type your question
- Or use the keyword forwarder script: `python neo_alias.py`

---

### 🤖 Option A: Full Neo Bot (Advanced - 20 minutes)

**Best for:** Complete control, standalone bot, advanced features

This creates a fully independent Neo bot with its own identity.

**Note:** This requires Slack app registration and running a bot server. For simpler setup, see Option C above.

**Setup Steps:**

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
- Morning brief - `@neo morning brief` or `⚡ Ask Neo → "morning brief"`
- Weekly review - `@neo weekly review`
- Help - `@neo help`

**Examples:**

*Option C (Workflow):*
- Click ⚡ → "Ask Neo" → type "morning brief"

*Option C (Forwarder):*
```
neo morning brief
@neo weekly review
```

*Option A (Full Bot):*
```
@neo morning brief
/neo weekly review
DM: help
```

---

## 🔍 Which Option Should I Choose?

| Feature | Option C (Alias) | Option A (Full Bot) |
|---------|-----------------|---------------------|
| Setup Time | 5 minutes | 20 minutes |
| Requires Coding | No (workflow) / Minimal (script) | Yes |
| App Registration | No | Yes |
| Server Required | No (workflow) / Yes (script) | Yes |
| Works Immediately | ✅ Yes | After setup |
| Customizable | Limited | Fully customizable |
| **Best For** | Quick personal use | Team/production use |

**💡 Recommendation:** Start with **Option C** (workflow shortcut). It takes 5 minutes and requires no coding!

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
