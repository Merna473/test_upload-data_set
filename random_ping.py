from datetime import datetime
import random


def generate_ping_log() -> None:
  ping_id = random.randint(1000, 9999)
  now = datetime.now().strftime("%H:%M:%S")
  log_line = f"Ping #{ping_id} verified at {now}\n"

  with open("sync_log.txt", "a", encoding="utf-8") as file:
    file.write(log_line)

  print(f"Done! Logged: {log_line.strip()}")


if __name__ == "__main__":
  generate_ping_log()