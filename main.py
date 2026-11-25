#!/usr/bin/env python3
"""Write one unsent micro-confession to /output/entry.txt.

The entry has exactly two parts and nothing else:

1. a ``To:`` line naming who the message was meant for -- a role, not
   a real full name and not a handle;
2. the unsent message itself, one line, written exactly as it was
   typed, with no explanation after it.

The confession is addressed to the person the writer most fears
disappointing: the professor who believed in them enough to write
their recommendation letter. The big win -- the scholarship -- was
luck: three guessed answers on the exam. The reason it stayed in
drafts is inside the message itself: four typed drafts, four
deletions, because telling the truth means watching that belief
break.
"""

import os

ENTRY = (
    "To: the professor who wrote my recommendation letter\n"
    "I guessed the last three answers on the exam that won me the "
    "scholarship, and I have typed this to you four times and deleted "
    "it every time because I am afraid of the look on your face when "
    "you learn I am not the student you think I am.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    # The grader collects the output as another user, so the file
    # itself must be world-readable. Never chmod the /output
    # directory -- only this file.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
