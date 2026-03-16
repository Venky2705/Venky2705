# 🚀 Neo Quick Start - 5 Minute Setup

## Goal: Use `@neo` to quickly access Claude bot

Instead of typing `<@U0A2TRBH7T6>`, just use `@neo`!

---

## ✨ Option 1: Slack Workflow (No Code - FASTEST!)

**Time: 5 minutes**

1. **In Slack:**
   - Click your **workspace name** (top left)
   - Select **Tools** → **Workflow Builder**

2. **Create workflow:**
   - Click **Create**
   - Choose **Blank workflow**
   - Name: `Ask Neo`

3. **Set trigger:**
   - Select **Shortcut**
   - Description: "Quick access to Neo assistant"

4. **Add step:**
   - Click **Add Step**
   - Choose **Send a message**
   - In "Message text", type:
     ```
     <@U0A2TRBH7T6> {{Ask a question}}
     ```
   - Set variable: "Ask a question" → Label: "What do you need?"

5. **Publish:**
   - Click **Publish** (top right)

**✅ Done! Now use it:**
- In any Slack channel, click the ⚡ **lightning bolt** icon
- Search for "Ask Neo"
- Type your question
- Submit!

---

## 📱 Option 2: Text Expansion (Mac/iPhone)

**Time: 2 minutes**

### Mac:
1. **System Preferences** → **Keyboard** → **Text**
2. Click **+** button
3. Replace: `@neo` → With: `<@U0A2TRBH7T6>`
4. Done!

### iPhone/iPad:
1. **Settings** → **General** → **Keyboard** → **Text Replacement**
2. Click **+**
3. Phrase: `<@U0A2TRBH7T6>` → Shortcut: `@neo`
4. Done!

**✅ Now when you type `@neo` it auto-expands!**

---

## 🤖 Option 3: Auto-Forward Script (For Advanced Users)

**Time: 15 minutes** (requires Slack app setup)

**Quick version:**
```bash
# 1. Set up minimal Slack app (see NEO_ALIAS_SETUP.md)
# 2. Add tokens to .env file
# 3. Run:
python neo_alias.py
```

This automatically forwards any message starting with "neo" to Claude.

**Full instructions:** See [NEO_ALIAS_SETUP.md](NEO_ALIAS_SETUP.md)

---

## 🎯 Which One?

| Method | Time | Ease | Auto? |
|--------|------|------|-------|
| **Workflow** | 5 min | ⭐⭐⭐ Easy | No (click ⚡) |
| **Text Expansion** | 2 min | ⭐⭐⭐ Easy | Yes (Mac/iOS) |
| **Script** | 15 min | ⭐⭐ Medium | Yes |

**💡 Recommended:** Start with **Workflow** (Option 1) - works everywhere, no coding!

---

## ❓ Need Help?

- **Workflow not showing?** Try searching in the ⚡ menu
- **Text expansion not working?** Type `@neo` + space
- **Script issues?** Check `.env` file has all tokens

**Full documentation:** [NEO_ALIAS_SETUP.md](NEO_ALIAS_SETUP.md)

---

## ✅ Test It!

Try these commands:
- `⚡ Ask Neo` → "morning brief"
- `⚡ Ask Neo` → "help"
- `⚡ Ask Neo` → "weekly review"

**Enjoy your Neo assistant! 🎉**
