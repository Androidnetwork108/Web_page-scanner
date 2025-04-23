import requests
import time
import sys
import re
from urllib.parse import urlparse

# Colors using ANSI escape codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Typing animation function
def hacker_typing(text, delay=0.09):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Get webpage title
def get_webpage_title(html):
    title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
    return title_match.group(1).strip() if title_match else "N/A"

while True:
    # Header lines
    hacker_typing(BOLD + RED + "═" * 50 + RESET)
    hacker_typing(BOLD + GREEN + "★ This tool maked by:- " + YELLOW + "@Hindu_papa ★" + RESET)
    hacker_typing(BOLD + CYAN + " " * 18 + "version:- 1.0" + RESET)
    hacker_typing(BOLD + RED + "═" * 50 + RESET)

    # URL input
    URL = input(BLUE + "Enter web URL:- " + RESET)

    # Option 2: URL format check
    parsed = urlparse(URL)
    if not parsed.scheme:
        print(YELLOW + "\n[!] URL scheme missing. Auto fixing with http://" + RESET)
        URL = "http://" + URL

    # Option 10: Final URL format fix (add trailing slash if missing)
    if not URL.endswith("/"):
        URL += "/"

    print(CYAN + "Scanning " + URL + " → Please wait..." + RESET)
    time.sleep(3)

    try:
        req = requests.get(URL)

        # Status code check
        if req.status_code == 200:
            print(GREEN + "\n★ Website is live ✓" + RESET)
        else:
            print(RED + f"\n★ Error: Status code {req.status_code}" + RESET)

        # Extra feature: Show Webpage Title
        title = get_webpage_title(req.text)
        hacker_typing(BOLD + CYAN + f"\nWEBPAGE NAME:- {title}" + RESET, delay=0.06)

        print(YELLOW + "\n★ Webpage Response Start ★\n\n" + RESET)

        # Slow scroll effect
        for line in req.text.splitlines():
            print(line)
            time.sleep(0.007)

        print(GREEN + "\n\n★ DONE ✓ ★" + RESET)

    except requests.exceptions.RequestException as e:
        print(RED + f"\nRequest failed: {e}" + RESET)

    # Option to try again or exit
    print("\n")
    choice = input(YELLOW + "Press Enter to try again or type 'exit' to quit: " + RESET)
    if choice.lower() == 'exit':
        print(RED + "\nExited. Goodbye!" + RESET)
        break
