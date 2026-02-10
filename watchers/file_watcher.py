import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

# 🔁 CHANGE THIS PATH to your AI_Employee_Vault path
VAULT_PATH = Path(r"./AI_Employee_Vault")

INBOX = VAULT_PATH / "Inbox"
NEEDS_ACTION = VAULT_PATH / "Needs_Action"

class InboxHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        source_path = Path(event.src_path)
        target_path = NEEDS_ACTION / source_path.name

        time.sleep(1)  # safety delay
        shutil.move(str(source_path), str(target_path))

        print(f"📥 New file moved to Needs_Action: {source_path.name}")

if __name__ == "__main__":
    INBOX.mkdir(exist_ok=True)
    NEEDS_ACTION.mkdir(exist_ok=True)

    event_handler = InboxHandler()
    observer = Observer()
    observer.schedule(event_handler, str(INBOX), recursive=False)
    observer.start()

    print("👀 File Watcher is running... (Ctrl+C to stop)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
