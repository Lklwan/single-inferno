"""Simple mood tracker - record how you feel each day."""

import datetime


MOOD_FILE = "mood.md"


def add_mood(mood: str) -> None:
    """Append a mood entry with today's date to the mood journal."""
    today = datetime.date.today().isoformat()
    entry = f"\n## {today}\n\n{mood}\n"
    with open(MOOD_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"Recorded: {mood} ({today})")


def show_history() -> None:
    """Display all mood entries."""
    try:
        with open(MOOD_FILE, encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("No mood history yet. Try adding one first!")


def main() -> None:
    print("=== Single Inferno Mood Tracker ===")
    print("1. Add today's mood")
    print("2. View mood history")
    print("q. Quit")
    print()

    choice = input("Choose an option: ").strip()

    if choice == "1":
        mood = input("How are you feeling today? ")
        add_mood(mood)
    elif choice == "2":
        show_history()
    elif choice == "q":
        print("Bye! 👋")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
