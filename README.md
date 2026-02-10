## Personal AI Employee – Bronze Tier (Digital FTE Foundation)

This project is an implementation of the **Bronze Tier** of the **Personal AI Employee / Digital FTE** concept from `Personal AI Employee Hackathon 0_ Building Autonomous FTEs in 2026.md`.

The goal is to build the **foundation layer** of a **Digital FTE (Full‑Time Equivalent)**: an AI employee that runs on your own machine, watches your inputs (email, files, etc.), and uses an AI reasoning engine to keep your work and life organized via a local Obsidian vault.

Instead of being “just a chatbot”, this AI behaves like a **junior operations employee** that:

- **Wakes up automatically** when something important happens (a new email, file, or message).
- **Writes tasks and summaries** into your Obsidian vault.
- **Keeps an inbox of work items** (`Needs_Action`) and a history of completed work (`Done`).

This README focuses on the **Bronze Tier** foundation and how this repo is structured for that.

---

## 1. What Is a Digital FTE?

A **Digital FTE** is a custom AI agent that you “hire” like a human employee, but:

- **Works 24/7 (168 hours/week)** instead of 40 hours/week.
- **Costs a fraction** of a human FTE.
- Can be **duplicated instantly** once designed (copy the setup, skills, and watchers).

For this Bronze Tier, we implement a **minimum viable Digital FTE**:

- A local Obsidian vault acts as the **dashboard and long‑term memory**.
- One or more **Watcher scripts** (Python) act as the **senses**.
- An AI engine (e.g. Claude Code) acts as the **brain**, reading and writing markdown in the vault.

Higher tiers (Silver/Gold/Platinum) extend this with more integrations and automation, but this project is focused on getting a **solid, working foundation**.

---

## 2. Bronze Tier Scope in This Repo

According to the hackathon spec, **Bronze Tier** includes:

- **Obsidian vault** with at least:
  - `Dashboard.md`
  - `Company_Handbook.md`
- **One working Watcher script** (e.g. Gmail watcher or file system watcher).
- **Claude Code or another LLM** successfully reading from and writing to the vault.
- **Basic folder structure** inside the vault:
  - `Inbox/` (optional depending on your design)
  - `Needs_Action/`
  - `Done/`
- All AI logic expressed as **Agent Skills** or repeatable prompts, not just ad‑hoc chats.

This repository is structured to support that foundation (code, watchers, and documentation) so you can evolve later to Silver, Gold, and Platinum tiers.

---

## 3. Tech Stack Overview

**Core components used in this project:**

- **AI Reasoning Engine**
  - Primary: **Claude Code** (via terminal / CLI).
  - Alternative: Any LLM exposed through tools that can read/write files in the vault.

- **Knowledge Base & UI**
  - **Obsidian** (local‑first Markdown vault).
  - Stores:
    - `Dashboard.md` (high‑level status).
    - `Company_Handbook.md` (rules & policies for the AI employee).
    - `Needs_Action/`, `Done/`, `Plans/`, etc. as folders.

- **Watchers (Python)**
  - Small Python scripts that run in the background:
    - Example: **File System Watcher** that moves or copies new files into `Needs_Action/`.
    - Example: **Gmail Watcher** that turns important unread emails into markdown tasks.

- **Automation & OS**
  - **Python 3.13+**
  - **macOS (Darwin)** for development.
  - Optionally: `cron`, `pm2`, or another process manager to keep watchers alive.

- **(Optional for extensions) MCP Servers**
  - For higher tiers, **Model Context Protocol (MCP)** servers can be added for:
    - Sending emails.
    - Browser automation (payments, dashboards).
    - Calendar integration.

For Bronze, you only need **Obsidian + Claude Code + Python watchers** to get started.

---

## 4. High‑Level Architecture

At a high level, the system follows this loop:

1. **Perception (Watchers)**
   - Python scripts watch external sources:
     - Email (Gmail API).
     - WhatsApp (via web automation).
     - File system folders (e.g. a “drop” folder).
   - When something interesting happens, a watcher creates a **markdown task file** in the Obsidian vault, usually in `Needs_Action/`.

2. **Reasoning (Claude Code / LLM)**
   - The AI is run periodically (manually or via cron) on the vault.
   - It reads files from `Needs_Action/`, `Inbox/`, `Accounting/`, etc.
   - It:
     - Summarizes items.
     - Writes plans (`Plans/*.md`).
     - Updates `Dashboard.md`.
     - Moves items logically from `Needs_Action/` to `Done/` as work is completed.

3. **Action (Optional MCP / Manual)**
   - In Bronze Tier, most actual “actions” (replying to emails, sending payments) are **still manual**:
     - The AI drafts the work or suggests steps.
     - You execute the final action.
   - For future tiers, MCP servers will let the AI execute certain actions automatically.

4. **Human‑in‑the‑Loop (HITL)**
   - You review what the AI produced in Obsidian.
   - You correct, approve, or reject decisions.
   - Your edits update the vault and guide the AI’s future behaviour.

Visually, you can think of it as:

- **Watchers → Obsidian (`Needs_Action/`) → Claude Code → Obsidian (`Dashboard`, `Done/`) → You**

---

## 5. Repository Structure (Bronze Tier)

Typical structure for this project:

- `Personal AI Employee Hackathon 0_ Building Autonomous FTEs in 2026.md`
  - Original hackathon architecture & rules (spec document).

- `watchers/`
  - Python watcher scripts (e.g. `file_watcher.py`, `gmail_watcher.py`, `base_watcher.py`).
  - Responsible for **detecting events** and **writing markdown tasks** into the vault.

- `README.md`
  - This file – explains the project, architecture, and how to use/extend it.

You will also have an **Obsidian vault folder** somewhere on disk (often outside this repo) with:

- `Dashboard.md`
- `Company_Handbook.md`
- `Needs_Action/`
- `Done/`
- `Plans/`
- `Logs/` (optional)

---

## 6. How the Bronze Tier Works End‑to‑End

Example flow with a **File System Watcher**:

1. You drop a new file (e.g. an invoice PDF or a client brief) into a **watched folder**.
2. The **file watcher script** detects the new file.
3. The watcher:
   - Copies or moves the file into your Obsidian vault under `Needs_Action/FILE_<name>`.
   - Creates a small markdown metadata file (e.g. `FILE_<name>.md`) that describes what needs to be done.
4. Next time you run **Claude Code** against the vault:
   - It sees the new `Needs_Action` items.
   - It can:
     - Summarize them.
     - Add TODOs and next steps.
     - Update `Dashboard.md` with “New item: review FILE_<name>”.
5. You open Obsidian, see the dashboard and tasks, and work through them.
6. Once done, the AI (or you) moves the task files from `Needs_Action/` to `Done/`.

The same pattern works for **Gmail** and **WhatsApp**:

- Watchers convert **messages** into **markdown task files**.
- The AI reasons over those markdown files, not raw APIs.

---

## 7. Setting Up Your Own Bronze Tier

**Prerequisites (high‑level)**  
See the full hackathon spec for detailed links, but in summary:

- Install:
  - **Claude Code**
  - **Obsidian**
  - **Python 3.13+**
- Create an Obsidian vault, e.g. `AI_Employee_Vault`, with:
  - `Dashboard.md`
  - `Company_Handbook.md`
  - `Needs_Action/`, `Done/` folders.
- Configure **one watcher** (file system or Gmail) to write into the vault’s `Needs_Action/`.
- Run **Claude Code** pointing at the vault directory and test:
  - Reading `Needs_Action/`.
  - Writing updates to `Dashboard.md`.

Once this loop is working end‑to‑end, you have achieved the **Bronze Tier**.

---

## 8. Where Can This Be Used? (Use Cases & Industries)

The same core architecture (Watchers → Vault → AI Reasoning → Optional Actions) can be applied across many domains:

- **Solo Founders & Freelancers**
  - Track client emails, invoices, and deadlines.
  - Weekly “CEO briefing” summarizing revenue, overdue tasks, and risks.

- **Agencies & Service Businesses**
  - Collect leads from email, WhatsApp, and forms into a single `Needs_Action` queue.
  - Auto‑draft replies, proposals, and follow‑up sequences (you approve before sending).

- **Education & Training**
  - Watch assignment folders or LMS exports.
  - Summarize student progress, late submissions, and generate weekly reports.

- **Finance & Accounting (lightweight)**
  - Watch bank CSV exports or accounting files.
  - Highlight unusual transactions, recurring subscriptions, or potential savings.

- **Customer Support**
  - Turn new tickets/emails into structured markdown tasks.
  - Propose responses and tag priority based on rules in `Company_Handbook.md`.

- **Personal Productivity**
  - Collect notes, screenshots, PDFs into a single `Needs_Action` stream.
  - Generate summaries and action lists for your personal life and projects.

In all these scenarios, the **key advantages** are:

- **Local‑first privacy** (your data lives in Obsidian on your machine).
- **Always‑on watchers** catching important events automatically.
- **Consistent execution** of rules defined in `Company_Handbook.md`.

---

## 9. How to Extend Beyond Bronze

Once the Bronze Tier foundation is stable, you can grow the project by:

- Adding **more watchers**:
  - WhatsApp, LinkedIn, Facebook, Instagram, X (Twitter), calendar, etc.
- Introducing **MCP servers**:
  - To actually send emails, schedule meetings, or post on social media.
- Implementing the **Ralph Wiggum loop**:
  - A persistence pattern so the AI keeps iterating until a task is truly done.
- Adding a **weekly “Monday Morning CEO Briefing”**:
  - Automatic audit of tasks and transactions with a briefing file in Obsidian.

This README will still serve as the **high‑level overview**, while more detailed docs for Silver/Gold/Platinum tiers can be added in separate markdown files as the project evolves.

---

## 10. Summary

- This project is the **Bronze Tier foundation** of a **Personal AI Employee / Digital FTE**.
- It combines:
  - **Watchers** (Python) for perception,
  - **Obsidian** as memory and UI,
  - **Claude Code / LLM** as the reasoning brain.
- It is designed to be:
  - **Local‑first**, **privacy‑aware**, and **extensible** to higher tiers.

If someone reads only this `README.md`, they should understand:

- **What the project is** (a local autonomous AI employee foundation),
- **How it is built** (tech stack and architecture),
- **What it can do today** (Bronze tier features),
- **How it can be extended** (towards full autonomous Digital FTEs in many industries).

