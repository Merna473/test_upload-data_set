from datetime import datetime


def verify_connection(project_name: str, a: int, b: int) -> str:
  total = a + b
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  return f"[{timestamp}] {project_name} is synced! Test sum: {a} + {b} = {total}"


if __name__ == "__main__":
  print(verify_connection("VS Code + GitHub Check", 10, 15))