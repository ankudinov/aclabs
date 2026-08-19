#!/usr/bin/env python3
"""Display asynchronous lab startup progress in a VS Code terminal."""

import ipaddress
import json
import os
from pathlib import Path
import time
from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.theme import Theme


STATE_DIR = Path("/tmp/aclabs-lab-start")
STATE_PATH = STATE_DIR / "state.json"
LOG_PATH = STATE_DIR / "startup.log"
TERMINAL_STATES = {"READY", "FAILED"}
WAIT_TIMEOUT_SECONDS = 2400

custom_theme = Theme(
    {"info": "bold cyan", "warning": "magenta", "critical": "bold red"}
)
console = Console(theme=custom_theme, log_path=False)


def show_banner() -> None:
    console.clear()
    console.print("\n\n", end="")

    title = Text()
    title.append("c", style="grey")
    title.append("A", style="red")
    title.append("r", style="green")
    title.append("L", style="bold cyan")
    title.append("\n")

    banner = Text("   ")
    banner.append(title)
    banner.append(Text("   Containerized Arista Labs", style="white"))
    console.print(
        Panel(banner, border_style="cyan", padding=(1, 4), expand=False)
    )
    console.print("\n\n", end="")
    console.print("READ THIS FIRST!", style="critical")
    console.print("- check README.md", style="critical")
    console.print("- wait until the lab is ready", style="critical")
    console.print("\n")


def read_state() -> dict[str, Any]:
    try:
        data: Any = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def print_new_log(offset: int) -> int:
    try:
        with open(LOG_PATH, "r", encoding="utf-8", errors="replace") as log_file:
            log_file.seek(offset)
            output = log_file.read()
            new_offset = log_file.tell()
    except OSError:
        return offset

    if output:
        console.print(output, end="", markup=False)
    return new_offset


def main() -> int:
    show_banner()
    deadline = time.monotonic() + WAIT_TIMEOUT_SECONDS
    offset = 0

    while time.monotonic() < deadline:
        offset = print_new_log(offset)
        state = read_state()
        status = state.get("status")
        if status in TERMINAL_STATES:
            message = str(state.get("message", status))
            if status == "READY":
                console.log(message, style="info")
                try:
                    on_prem_cvp = (
                        ipaddress.ip_address(os.environ.get("CVURL", "")).version
                        == 4
                    )
                except ValueError:
                    on_prem_cvp = False
                if on_prem_cvp:
                    console.print(
                        "Open a new terminal to load generated runtime variables.",
                        style="warning",
                    )
                return 0
            console.log(message, style="critical")
            return 1
        time.sleep(1)

    console.log(
        f"Timed out waiting {WAIT_TIMEOUT_SECONDS} seconds "
        "for automatic lab startup.",
        style="critical",
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
