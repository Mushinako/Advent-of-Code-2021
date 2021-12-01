# pyright: reportMissingTypeStubs=false
"""
Get input from and submit answer to AOC
"""

from __future__ import annotations

from time import sleep
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from string import Template
from pathlib import Path
from typing import TYPE_CHECKING

import requests
import yaml
from bs4 import BeautifulSoup
from colorama import Fore, init

if TYPE_CHECKING:
    from typing import Literal

init(autoreset=True)

_CONFIG_PATH = Path(__file__).resolve().parent / "config.yml"
with _CONFIG_PATH.open("r") as f:
    _CONFIG = yaml.safe_load(f)

DATA_URL = Template("https://adventofcode.com/2021/day/${day}/input")
ANSWER_URL = Template("https://adventofcode.com/2021/day/${day}/answer")

_COOKIES = _CONFIG["cookies"]

_DAY_CHOICES = set(range(1, 26))
_LEVEL_CHOICES = {1, 2}


def download_input(day: int, input_path: Path) -> None:
    """
    Download input from AOC website
    Args:
        day        (1..25)       : The day of AOC
        input_path (pathlib.Path): Path of file to write input to
    """
    if day not in _DAY_CHOICES:
        raise ValueError(f"{day=} is not in range 1..25")
    target_time_est = datetime(
        2021, 12, day, 23, 59, 59, 500_000, tzinfo=ZoneInfo("EST")
    ) - timedelta(days=1)
    target_time_local = datetime.fromtimestamp(target_time_est.timestamp())

    while (now := datetime.now()) < target_time_local:
        diff = target_time_local - now
        seconds = diff.days * 86400 + diff.seconds
        if seconds > 3600:
            print(f"{seconds} seconds until problem opens. Too early...")
        elif seconds > 1:
            print(f"{seconds} seconds until problem opens. Waiting...")
        sleep(max(diff.seconds - 1, 1))

    for _ in range(3):
        with requests.get(DATA_URL.substitute(day=day), cookies=_COOKIES) as response:
            data = response.content
            if not response.ok:
                print(Fore.RED + data.decode("utf-8").strip())
                sleep(1)
                continue
            break
    else:
        raise ConnectionError("Download failed!")

    print(
        Fore.GREEN
        + f"Got input with {len(data)} characters and {len(data.splitlines())} lines"
    )
    with input_path.open("wb") as input_fp:
        input_fp.write(data)


def submit_output(day: int, level: Literal[1, 2], answer: str | int) -> None:
    """
    Upload solution to AOC website
    Args:
        day    (1..25)    : The day of AOC
        level  (1, 2)     : Whether the submission is for part 1 or 2
        answer (str | int): Answer to be submitted
    Returns:
        (str): Success/failure string, with coloring
    """
    if day not in _DAY_CHOICES:
        raise ValueError(f"{day=} is not in range 1..25")
    if level not in _LEVEL_CHOICES:
        raise ValueError(f"{level=} is not 1 or 2")

    for _ in range(3):
        with requests.post(
            ANSWER_URL.substitute(day=day),
            {"level": level, "answer": answer},
            cookies=_COOKIES,
        ) as response:
            data = response.content
            if not response.ok:
                print(Fore.RED + data.decode("utf-8").strip())
                sleep(1)
                continue
            break
    else:
        raise ConnectionError("Failed to submit response.")

    html = BeautifulSoup(data, "html.parser")
    response_text: str = html.article.p.text
    if response_text.startswith("You don't"):
        print(Fore.YELLOW + response_text)
    elif response_text.startswith("That's the"):
        print(Fore.GREEN + response_text)
    elif response_text.startswith("That's not"):
        print(Fore.RED + response_text)
    elif response_text.startswith("You gave"):
        print(Fore.RED + response_text)
    else:
        raise ValueError(f"Unknown response text: {response_text}")
