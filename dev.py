# filepath: dev.py
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import sys
import logging
import threading

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class RestartHandler(FileSystemEventHandler):
    def __init__(self, command, debounce_time=0.5):
        self.command = command
        self.process = None
        self.debounce_time = debounce_time
        self.restart_timer = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        self.process = subprocess.Popen(self.command)

    def debounce_restart(self):
        """
        Debounce multiple rapid file changes to avoid multiple restarts.
        """
        logger.info("Debouncing restart...")
        if self.restart_timer:
            self.restart_timer.cancel()
        logger.info("Scheduling restart in %s seconds...", self.debounce_time)
        self.restart_timer = threading.Timer(self.debounce_time, self.start_process)

        logger.info("Restart scheduled.")
        self.restart_timer.start()

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            logger.info(f"Detected change in {event.src_path}, scheduling restart...")
            self.debounce_restart()


def run_dev_server():
    path = "."
    command = [sys.executable, "main.py"]
    event_handler = RestartHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    logger.info("Development server started. Watching for file changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Shutting down development server...")
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()
    observer.join()


if __name__ == "__main__":
    run_dev_server()
