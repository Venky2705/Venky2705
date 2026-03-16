# Neo Alias - Simple Setup Guide

## What is Option C (Neo Alias)?

Option C is the **simplest way** to create a `@neo` handle without requiring full Slack bot registration. It creates an alias that forwards messages to your existing Claude bot (`<@U0A2TRBH7T6>`).

## 🎯 Three Ways to Use Neo Alias

### **Method 1: Slack Workflow Shortcut** ⚡ (Recommended - No Code!)

This is the easiest method and requires **no coding or bot setup**.

**Setup Steps:**

1. **Open Workflow Builder in Slack:**
   - Click your workspace name → **Tools** → **Workflow Builder**
   - Click **Create** → **Start from scratch**

2. **Set up the trigger:**
   - Name: `Ask Neo`
   - Select trigger type: **Shortcut**
   - Description: `Quick access to Claude (Neo assistant)`

3. **Add a step:**
   - Click **Add Step** → **Send a message**
   - Channel: **Select "Same channel as shortcut was used"**
   - Message text: `<@U0A2TRBH7T6> {{user_input}}`
   - Add a variable: Click **Add a variable** → **Ask a question**
     - Question: `What would you like to ask Neo?`
     - Variable name: `user_input`

4. **Publish:**
   - Click **Publish** in the top right

**How to use:**
- Click the ⚡ **lightning bolt** icon in any Slack channel
- Search for "Ask Neo"
- Type your question → Submit
- Claude will respond as if you mentioned it directly!

---

### **Method 2: Keyword Forwarder Script** 🤖

A lightweight Python script that listens for "neo" mentions and forwards to Claude.

**Setup Steps:**

1. **Create a minimal Slack app** (simpler than full bot):
   - Go to https://api.slack.com/apps → **Create New App** → **From scratch**
   - Name: `Neo Alias`
   - Pick your workspace

2. **Add basic permissions:**
   - Go to **OAuth & Permissions** → Add these Bot Token Scopes:
     - `channels:history`
     - `channels:read`
     - `chat:write`
     - `reactions:write`
   - Install app to workspace
   - Copy the **Bot User OAuth Token** (starts with `xoxb-`)

3. **Enable Socket Mode:**
   - Go to **Socket Mode** → Enable
   - Go to **Basic Information** → **App-Level Tokens**
   - Generate token with scope: `connections:write`
   - Copy the **App Token** (starts with `xapp-`)

4. **Configure and run:**
   ```bash
   # Add to .env file
   SLACK_BOT_TOKEN=xoxb-your-token
   SLACK_APP_TOKEN=xapp-your-token
   SLACK_SIGNING_SECRET=your-signing-secret

   # Run the alias forwarder
   python neo_alias.py
   ```

**How it works:**
- Type `neo morning brief` or `@neo help` in any channel
- Script automatically forwards to `<@U0A2TRBH7T6>`
- Adds 🤖 reaction to show it received your message

---

### **Method 3: Text Expansion (Mac/iOS)** 💻

Create a text replacement shortcut on Mac or iOS.

**Mac Setup:**
1. System Preferences → **Keyboard** → **Text**
2. Click **+** to add new replacement
3. Replace: `@neo` → With: `<@U0A2TRBH7T6>`

**iOS Setup:**
1. Settings → **General** → **Keyboard** → **Text Replacement**
2. Add new: Phrase: `<@U0A2TRBH7T6>` → Shortcut: `@neo`

**Usage:**
- Type `@neo` and it auto-expands to `<@U0A2TRBH7T6>`
- Works system-wide (not just Slack)

---

## 🔍 Comparison

| Method | Difficulty | Setup Time | Works Where | Best For |
|--------|-----------|------------|-------------|----------|
| **Workflow Shortcut** | Easy | 5 min | Slack only | Quick access, no code |
| **Forwarder Script** | Medium | 15 min | Slack only | Automatic forwarding |
| **Text Expansion** | Easy | 2 min | System-wide | Mac/iOS users |

---

## 💡 Recommended Approach

**Start with Method 1 (Workflow Shortcut)** - It's the fastest and requires no coding or bot registration!

If you want automatic message forwarding (type "neo" directly), use Method 2.

For Mac/iOS users who want system-wide expansion, add Method 3.

---

## ❓ Troubleshooting

**Workflow not showing up?**
- Make sure you published it in Workflow Builder
- Try searching for it using the ⚡ lightning bolt menu

**Forwarder script not working?**
- Check that your .env file has all three required tokens
- Ensure the bot is invited to the channels you're testing in
- Check the console for error messages

**Text expansion not working?**
- Make sure you've saved the text replacement
- Try typing the full shortcut followed by a space

---

## 🎉 Success!

Once set up, you can use `@neo` or the shortcut to quickly access Claude without typing the full mention!

**Example commands:**
- `⚡ Ask Neo` → "morning brief"
- Type: `neo weekly review`
- Mac: Type `@neo` (auto-expands)

All methods forward to your existing Claude bot, no separate bot needed!
