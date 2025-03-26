import sys

class ProgressTracker:
    def __init__(self, total_steps: int, task_name: str = "Loading", bar_length: int = 20):
        self.total_steps = total_steps
        self.current_step = 0
        self.task_name = task_name
        self.bar_length = bar_length

    def update(self, step: int = 1, message: str = ""):
        self.current_step += step
        percent = self.current_step / self.total_steps
        bar_length = self.bar_length  # Länge des Balkens
        filled_length = int(bar_length * percent)
        bar = "#" * filled_length + "-" * (bar_length - filled_length)
        sys.stdout.write(f"\r[{bar}] {int(percent * 100)}% - {self.task_name}: {message}")
        sys.stdout.flush()

    def done(self):
        sys.stdout.write("\r" + " " * (self.bar_length + 50) + "\r")  # Leert die Zeile
        sys.stdout.write(f"[{'#' * self.bar_length}] 100% - {self.task_name}: Done!\n")
        sys.stdout.flush()  # springt in neue Zeile, wenn fertig