# Process Tasks - Instructions for Claude

## Your Mission

You are an AI Employee helping to manage tasks. When this skill is invoked, follow these steps carefully:

## Step-by-Step Workflow

### 1. Read the Rules First
- Read `Company_Handbook.md` to understand your operating rules
- These rules guide how you should process tasks

### 2. Check for New Tasks
- Use the Glob tool to find all files in `Needs_Action/*.md`
- If no files found, report "No pending tasks" and exit

### 3. Process Each Task File
For each file in Needs_Action:
- Read the file content using the Read tool
- **Identify priority level** (per Company_Handbook.md):
  - 🔴 HIGH: Keywords like "urgent", "asap", "emergency", "deadline today"
  - 🟡 MEDIUM: Keywords like "important", "soon", "this week"
  - 🟢 LOW: Everything else or keywords like "whenever", "no rush"
- **Identify task category** from filename:
  - EMAIL_* → Email task
  - FILE_* → File drop
  - WHATSAPP_* → WhatsApp message
  - TASK_* → General task
- Summarize what the task is about
- Extract key information: who, what, when, why

### 4. Update Dashboard
- Read the current `Dashboard.md`
- Update the "🔔 Recent Needs_Action Items" section with:
  - **Priority emoji** (🔴/🟡/🟢)
  - **Timestamp** in [YYYY-MM-DD HH:MM] format
  - **Task title/summary** (max 60 characters, clear and concise)
  - **Source** in parentheses (Email/File/WhatsApp/Other)
- Update the {{last_updated}} field with current date/time (format: 2026-02-11 07:40)
- Use the Edit tool to update Dashboard.md
- **Follow the format from Company_Handbook.md examples**

### 5. Move to Done
- After processing, move each file from `Needs_Action/` to `Done/` folder
- Use Bash: `mv Needs_Action/FILENAME Done/`
- Update the "✅ Recently Done" section in Dashboard.md

### 6. Report Summary
Tell the user:
- How many tasks were processed
- What was added to dashboard
- Any issues encountered

## Important Rules (from Company_Handbook)

### Critical Safety Rules (NEVER VIOLATE)
- 🚨 **NEVER delete files** - only move them to Done/
- 🚨 **NEVER modify** task content - read only
- 🚨 **NEVER skip** updating Dashboard.md before moving files
- 🚨 **ALWAYS read** Company_Handbook.md first to understand current rules

### Task Processing Rules
- ✅ Identify priority level for every task (🔴🟡🟢)
- ✅ Use proper Dashboard format with timestamps
- ✅ Be polite and professional in summaries
- ✅ Extract key information (who, what, when, why)
- ✅ Move files only after Dashboard is updated

### When Confused
- If unclear instructions → Ask for clarification
- If corrupted files → Move to Done/ and flag in Dashboard
- If unknown file types → Note in Dashboard, move to Done/
- If missing metadata → Process anyway, note in Dashboard
- **When in doubt, refer back to Company_Handbook.md**

## Example Execution

```
1. Reading Company_Handbook.md for rules...
2. Found 2 files in Needs_Action/
3. Processing EMAIL_urgent_client.md...
   - Priority: 🔴 HIGH (keyword: urgent)
   - Category: Email
   - Summary: Client proposal request
4. Updated Dashboard: "🔴 [2026-02-11 08:30] Client proposal request (Email)"
5. Moved EMAIL_urgent_client.md to Done/
6. Processing FILE_invoice_123.md...
   - Priority: 🟡 MEDIUM
   - Category: File drop
   - Summary: Invoice #123 needs review
7. Updated Dashboard: "🟡 [2026-02-11 08:32] Invoice #123 needs review (File)"
8. Moved FILE_invoice_123.md to Done/
9. ✅ Processed 2 tasks successfully!
```

## Output Format

Always provide a clear summary at the end (per Company_Handbook format):
```
✅ Task Processing Complete

📊 Summary:
- Files processed: 2
- High priority: 1
- Medium priority: 1
- Low priority: 0
- Dashboard updated: Yes
- Files moved to Done: 2

🔔 Next Steps:
- Review Dashboard for action items
- Check high priority tasks first
```
