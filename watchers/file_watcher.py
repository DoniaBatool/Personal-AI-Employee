import time
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# 🔁 CHANGE THIS PATH to your AI_Employee_Vault path if needed
VAULT_PATH = Path("./AI_Employee_Vault")

INBOX = VAULT_PATH / "Inbox"


class DropFolderHandler(FileSystemEventHandler):
    """
    Watches the Inbox folder and copies any new file into
    the vault's Needs_Action folder with metadata, following
    the filesystem_watcher pattern from the hackathon docs.
    """

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.needs_action = self.vault_path / "Needs_Action"

        # Ensure Needs_Action exists
        self.needs_action.mkdir(exist_ok=True)

    def on_created(self, event):
        if event.is_directory:
            return

        source = Path(event.src_path)
        dest = self.needs_action / f"FILE_{source.name}"

        # Copy instead of move so the original drop location is preserved if needed
        shutil.copy2(source, dest)
        self.create_metadata(source, dest)

        print(f"📥 New file copied to Needs_Action: {dest.name}")

    def create_metadata(self, source: Path, dest: Path):
        meta_path = dest.with_suffix(".md")
        meta_path.write_text(
            f"""---
type: file_drop
original_name: {source.name}
size: {source.stat().st_size}
---

New file dropped for processing.
""",
            encoding="utf-8",
        )


if __name__ == "__main__":
    # Make sure Inbox exists
    INBOX.mkdir(exist_ok=True)

    handler = DropFolderHandler(str(VAULT_PATH))
    observer = Observer()
    observer.schedule(handler, str(INBOX), recursive=False)
    observer.start()

    print("👀 File Watcher is running... (Ctrl+C to stop)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
