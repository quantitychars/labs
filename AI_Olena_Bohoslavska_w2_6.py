"""Exercise 6 - follow the data through four containers.

COMP H2003 Artificial Intelligence, TU Dublin

    python exercise_06_container_conversion.py

1. Read a comma-separated list of words, deliberately repeating one or two.
2. Print it as a list with its length, then as a sorted set with its length.
3. Report how many items the set conversion discarded.
4. Build a dict mapping each word to its length, convert that dict back to a
   list, and compare it with the original list.
5. Deduplicate the original keeping first-seen order, then print the words
   sorted by how often they appeared.

Replace each ... with your own code.
"""


def ask(prompt, default):
    """input() with a default, so this script can also be run unattended."""
    try:
        value = input(f'{prompt} [{default}]: ').strip()
    except (EOFError, OSError):
        value = ''
    return value or default


raw = ask('words, comma separated', 'ai, ml, ai, data')
words = [w.strip() for w in raw.split(',') if w.strip()]
print('1 list  :', words, len(words))

# TODO 1: as a set, printed sorted, with its length
as_set = set(words)
print('2 set   :', sorted(as_set), len(as_set))

# TODO 2: how many were discarded?
print('3 lost  :', len(words) - len(as_set))

# TODO 3: dict of word -> length
lengths = {word: len(word) for word in words}
print('4 dict  :', lengths)

# TODO 4: convert the dict back to a list. Keys or pairs?
back = list(lengths)
print('5 back  :', back, back == words)

# TODO 5: dedupe keeping order, then count and sort
unique = list(dict.fromkeys(words))
counts = {word: words.count(word) for word in unique}
sorted_counts = sorted(unique, key=lambda word: counts[word], reverse=True,)
print('6 sorted:', sorted_counts, [counts[w] for w in sorted_counts])