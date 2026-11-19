import platform
import sys


def system_ping() -> dict:
  return {
      "status": "OK",
      "python_version": sys.version.split()[0],
      "os": platform.system(),
      "message": "Second sync test from VS Code to GitHub succeeded!",
  }


if __name__ == "__main__":
  info = system_ping()
  for key, value in info.items():
    print(f"{key}: {value}")