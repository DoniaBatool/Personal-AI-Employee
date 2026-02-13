# Process Tasks Skill

**Name:** process-tasks
**Description:** Process files from Needs_Action folder and update Dashboard

## What This Skill Does

This skill helps the AI Employee process incoming tasks by:
1. Reading all files from the `Needs_Action/` folder
2. Following rules from `Company_Handbook.md`
3. Updating the `Dashboard.md` with new items
4. Moving processed files to the `Done/` folder

## When to Use

- When new files appear in Needs_Action folder
- When you want to update the dashboard with pending tasks
- When manually invoked by user with `/process-tasks`

## Example Usage

```
/process-tasks
```

The AI will automatically:
- Check Needs_Action folder
- Read Company_Handbook.md for rules
- Update Dashboard.md with task summaries
- Move processed files to Done folder
