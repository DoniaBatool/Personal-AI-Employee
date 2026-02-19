---
name: process-tasks
description: Process files from Needs_Action folder, update Dashboard.md following Company_Handbook rules
author: Donia
version: 1.0
category: automation
tags: [bronze-tier, task-processing, dashboard, automation]
invocation: /process-tasks
---

# 🤖 Process Tasks - AI Employee Skill

## Overview

This skill enables your AI Employee to automatically process incoming tasks from the `Needs_Action/` folder and update the Dashboard according to the rules defined in `Company_Handbook.md`.

**Bronze Tier Feature**: Core automation for task processing and dashboard management.

---

## What This Skill Does

When invoked, this skill will:

1. ✅ **Read Operating Rules**
   - Loads `Company_Handbook.md` to understand current processing rules
   - Applies priority levels (🔴 HIGH, 🟡 MEDIUM, 🟢 LOW)
   - Follows task categorization rules

2. ✅ **Scan for New Tasks**
   - Checks `Needs_Action/` folder for .md files
   - Identifies task type from filename pattern (EMAIL_*, FILE_*, WHATSAPP_*, TASK_*)

3. ✅ **Process Each Task**
   - Reads file content and metadata
   - Extracts key information (who, what, when, why)
   - Determines priority level based on keywords and metadata
   - Categorizes the task type

4. ✅ **Update Dashboard**
   - Updates `Dashboard.md` with new task information
   - Adds proper formatting: Priority emoji + Timestamp + Title + Source
   - Updates "Last updated" timestamp
   - Maintains "Recent Needs_Action Items" section

5. ✅ **Archive Processed Tasks**
   - Moves processed files from `Needs_Action/` to `Done/` folder
   - Updates "Recently Done" section in Dashboard
   - Never deletes files (safety rule from Company_Handbook)

6. ✅ **Report Summary**
   - Provides detailed summary of processing results
   - Shows priority breakdown
   - Lists any issues or blockers

---

## When to Use

### Manual Invocation
```bash
/process-tasks
```

### Automatic Triggers (Silver/Gold Tier)
- When file watcher detects new files in Needs_Action/
- Scheduled runs (e.g., every 5 minutes)
- On system startup

### Common Scenarios
- 📧 New email detected by Gmail watcher
- 📱 WhatsApp message flagged as important
- 📁 File manually dropped into Inbox folder
- 🔄 Periodic dashboard refresh

---

## Company_Handbook Integration

This skill **strictly follows** the rules defined in `Company_Handbook.md`:

### Priority Detection Rules
From Company_Handbook.md:
- **🔴 HIGH**: Keywords like "urgent", "asap", "emergency", "deadline today"
- **🟡 MEDIUM**: Keywords like "important", "soon", "this week"
- **🟢 LOW**: Everything else or keywords like "whenever", "no rush"

### Task Categories
From Company_Handbook.md:
- **EMAIL_\***: Email-related tasks → Summarize sender, subject, action needed
- **FILE_\***: File drops → Note filename and size
- **WHATSAPP_\***: WhatsApp messages → Note sender and message type
- **TASK_\***: General tasks → Extract action items

### Safety Rules
From Company_Handbook.md (CRITICAL):
- 🚨 **NEVER delete files** - only move to Done/
- 🚨 **NEVER modify** task content - read only
- 🚨 **NEVER skip** updating Dashboard.md
- 🚨 **ALWAYS read** Company_Handbook.md first

### Dashboard Format
From Company_Handbook.md:
```markdown
- 🟡 **[2026-02-11 08:30]** Task title here (Source Type)
  - **Additional details** if needed
```

---

## Example Workflow

### Input: New File in Needs_Action

**File**: `EMAIL_client_proposal_2026-02-11.md`
```yaml
---
type: email
from: client@example.com
subject: Urgent: Proposal needed by Friday
priority: high
---
Client needs proposal for Q1 project by end of week.
```

### Processing Steps

1. **Read Company_Handbook.md** ✓
2. **Scan Needs_Action/** → Found 1 file ✓
3. **Analyze file**:
   - Filename pattern: EMAIL_* → Email task
   - Metadata priority: high
   - Keywords: "Urgent", "by Friday" → 🔴 HIGH
   - Summary: Client proposal request
4. **Update Dashboard.md**:
   ```markdown
   ## 🔔 Recent Needs_Action Items
   - 🔴 **[2026-02-11 09:15]** Client proposal needed by Friday (Email)
     - **From:** client@example.com
     - **Deadline:** Friday
   ```
5. **Move file**: `Needs_Action/EMAIL_client_proposal_2026-02-11.md` → `Done/`
6. **Update Recently Done** section
7. **Report**:
   ```
   ✅ Processed 1 high-priority email task
   📊 Dashboard updated successfully
   ```

---

## Output Format

After processing, you'll receive a detailed report:

```
✅ Task Processing Complete

📊 Summary:
- Files processed: 3
- High priority: 1
- Medium priority: 1
- Low priority: 1
- Dashboard updated: Yes
- Files moved to Done: 3

🔔 Priority Breakdown:
- 🔴 HIGH: Client proposal needed by Friday (Email)
- 🟡 MEDIUM: Invoice #123 needs review (File)
- 🟢 LOW: Team meeting notes (Task)

📝 Dashboard Status:
- Last updated: 2026-02-11 09:15
- Active tasks tracked: 3
- Completed tasks: 3

🎯 Next Steps:
- Review high priority tasks first
- Check Dashboard for action items
```

---

## Technical Details

### Files Modified
- **Read**: `Company_Handbook.md` (rules)
- **Read**: All `Needs_Action/*.md` files
- **Write**: `Dashboard.md` (updates)
- **Move**: Files from `Needs_Action/` to `Done/`

### Tools Used
- **Glob**: Find .md files in Needs_Action/
- **Read**: Read file contents and metadata
- **Edit**: Update Dashboard.md
- **Bash**: Move files with `mv` command

### Error Handling
- Corrupted files → Move to Done/, flag in Dashboard
- Missing metadata → Process anyway, note in Dashboard
- Unknown file types → Note in Dashboard, move to Done/
- No files found → Report "No pending tasks" and exit

---

## Bronze Tier Requirements

This skill fulfills the Bronze tier requirements:

- ✅ Obsidian vault integration
- ✅ Dashboard.md auto-update
- ✅ Company_Handbook.md rule following
- ✅ Folder structure management (Needs_Action → Done)
- ✅ Claude Code file operations
- ✅ Implemented as Agent Skill

---

## Troubleshooting

### Skill Not Found
If `/process-tasks` shows "Unknown skill":
1. Verify `.claude/skills/process-tasks/` folder exists
2. Check `SKILL.md` and `CLAUDE.md` are present
3. Restart Claude Code session
4. Try `claude --reload-skills` (if available)

### Dashboard Not Updating
1. Check Dashboard.md has proper structure
2. Verify {{last_updated}} placeholder exists
3. Check file permissions (read/write access)

### Files Not Moving
1. Verify Done/ folder exists
2. Check file permissions
3. Ensure Company_Handbook safety rule being followed

---

## Related Files

- **📘 Company_Handbook.md**: Operating rules and guidelines
- **📊 Dashboard.md**: Main dashboard (updated by this skill)
- **🤖 CLAUDE.md**: Detailed instructions for Claude
- **📁 Needs_Action/**: Input folder for new tasks
- **✅ Done/**: Archive folder for processed tasks

---

## Version History

- **v1.0** (2026-02-11): Initial Bronze tier implementation
  - Basic task processing
  - Dashboard auto-update
  - Company_Handbook integration
  - Priority detection
  - File movement and archival

---

## Next Steps (Future Enhancements)

**Silver Tier** additions:
- Multiple watcher integration
- Plan.md generation
- Human-in-the-loop approval workflow
- MCP server integration

**Gold Tier** additions:
- Ralph Wiggum loop for autonomous processing
- Multi-step task completion
- Error recovery and retry logic
- Comprehensive audit logging

---

**Remember**: This skill always operates within the rules defined in `Company_Handbook.md`. When in doubt, it asks for clarification rather than taking risky actions.

---

*Built for Bronze Tier - Personal AI Employee Hackathon 0*
