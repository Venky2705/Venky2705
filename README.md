# Granola Notes to Notion Importer

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
