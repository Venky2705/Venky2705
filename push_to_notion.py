#!/usr/bin/env python3
"""
Script to push Granola notes from CSV to Notion database.
Reads granola_notes.csv and imports the data into the "Naidu's Granola Notes" Notion database.
"""

import csv
import os
from datetime import datetime
from notion_client import Client


def parse_date(date_string):
    """Parse ISO 8601 date string to Notion date format."""
    try:
        dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d')
    except:
        return None


def import_granola_notes(notion_token, database_id, csv_file):
    """Import granola notes from CSV to Notion database."""

    # Initialize Notion client
    notion = Client(auth=notion_token)

    # Read CSV file
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Found {len(rows)} notes to import...")

    # Import each row
    for i, row in enumerate(rows, 1):
        try:
            # Parse the date
            created_date = parse_date(row['document_created'])

            # Create page properties
            properties = {
                "Title": {
                    "title": [
                        {
                            "text": {
                                "content": row['document_title']
                            }
                        }
                    ]
                },
                "Date": {
                    "date": {
                        "start": created_date
                    } if created_date else None
                },
                "Created by": {
                    "select": {
                        "name": row['user_email']
                    }
                },
                "Link": {
                    "url": f"https://notes.granola.ai/document/{row['document_id']}"
                }
            }

            # Create page content with summary and notes
            children = []

            # Add Summary section
            if row.get('summary'):
                children.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"type": "text", "text": {"content": "Summary"}}]
                    }
                })

                # Split summary by lines and add as paragraphs
                summary_lines = row['summary'].split('\n')
                for line in summary_lines:
                    if line.strip():
                        children.append({
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {
                                "rich_text": [{"type": "text", "text": {"content": line}}]
                            }
                        })

            # Create the page
            notion.pages.create(
                parent={"database_id": database_id},
                properties=properties,
                children=children
            )

            print(f"✓ Imported {i}/{len(rows)}: {row['document_title']}")

        except Exception as e:
            print(f"✗ Error importing '{row['document_title']}': {str(e)}")
            continue

    print(f"\nImport complete! Successfully imported notes to Notion.")


def main():
    """Main function to run the import."""

    # Get Notion credentials from environment variables
    notion_token = os.getenv('NOTION_TOKEN')
    database_id = os.getenv('NOTION_DATABASE_ID')

    if not notion_token:
        print("Error: NOTION_TOKEN environment variable not set")
        print("Please set it with: export NOTION_TOKEN='your_token_here'")
        return

    if not database_id:
        print("Error: NOTION_DATABASE_ID environment variable not set")
        print("Please set it with: export NOTION_DATABASE_ID='your_database_id_here'")
        return

    csv_file = 'granola_notes.csv'

    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found")
        return

    print("Starting Granola notes import to Notion...")
    print(f"Database ID: {database_id}")
    print(f"CSV file: {csv_file}\n")

    import_granola_notes(notion_token, database_id, csv_file)


if __name__ == '__main__':
    main()
