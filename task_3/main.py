"""Module for Task 3."""

import sys
import re

from datetime import datetime
from collections import Counter
from typing import Generator
from pathlib import Path

pattern = re.compile(r'^([\d\:\-\s]+) (DEBUG|INFO|WARNING|ERROR) (.+)\n$')

def read_file(file_path: str) -> Generator[str, None, None]:
    """Read file line by line.

    Args:
        file_path (str): Path to file

    Raises:
        FileNotFoundError: If file not found

    Yields:
        Generator[str, None, None]: Generator of lines in file
    """
    path = Path(file_path)
    if not path.exists() or not path.is_file():
        raise ValueError("Файл не знайдено.")

    with open(path, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line


def parse_log_line(line: str) -> dict:
    """Parses log line with reqex.

    Args:
        line (str): Log line to parse

    Returns:
        dict: Parsed dictionary
    """
    match = re.match(pattern, line)
    if match:
        date_object =  datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
        log_level = match.group(2)
        message = match.group(3)
        return {
            'date': date_object,
            'log_level': log_level.upper(),
            'message': message,
        }
    else:
        raise ValueError("Неочікуваний формат логу.")


def load_logs(file_path: str) -> list:
    """Load logs from file.

    Args:
        file_path (str): Path to file

    Returns:
        list: List of parsed logs
    """
    logs = []
    for log in read_file(file_path):
        log_entry = parse_log_line(log)
        logs.append(log_entry)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by log level.

    Args:
        logs (list): List of logs
        level (str): Log level to filter by

    Returns:
        list: Filtered list of logs
    """
    return [log for log in logs if log["log_level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    """Count logs by log level.

    Args:
        logs (list): List of logs

    Returns:
        dict: Dictionary with count of logs by log level
    """
    counts = Counter(log["log_level"] for log in logs)
    return dict(counts)


def display_log_counts(counts: dict):
    """Display log counts.

    Args:
        counts (dict): Dictionary with log counts
    """
    print("Рівень логування | Кількість")
    print("---------------- | ---------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    """Main function."""

    if len(sys.argv) not in (2, 3):
        print("Використання:")
        print(f"{"\tpython main.py <log_file_path>":<60} \
              - виведе загальну статистику за рівнями логування")
        print(f"{"\tpython main.py <log_file_path> <debug|info|warning|error>":<60} \
              - виведе загальну статистику за рівнями, а також детальну інформацію для вибраного рівня")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) == 3 else None

    try:
        logs = load_logs(log_file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if log_level:
            log_level = log_level.upper()
            if log_level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
                raise ValueError("Невірний рівень логування. Виберіть один із: debug, info, warning, error")

            print(f"\nДеталі логів для рівня '{log_level}':")
            for log_entry in filter_logs_by_level(logs, log_level):
                print(f"{log_entry["date"].strftime('%Y-%m-%d %H:%M:%S')} - {log_entry["message"]}")

    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
