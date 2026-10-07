"""Exercise 4 - count and group in one pass.

COMP H2003 Artificial Intelligence, TU Dublin

    python exercise_04_count_and_group.py

1. Read a line of subject:name pairs.
2. Split it into (subject, name) tuples, stripping whitespace.
3. In one pass, build a dict counting entries per subject and a dict grouping
   names per subject.
4. Print a line per subject: how many entries, how many unique names, and the
   names sorted.
5. Print the busiest subject, then the subjects sorted by count, highest first.

Check yourself: CS should show 3 entries but only 2 unique names.

Replace each ... with your own code.
"""


def ask(prompt, default):
    """input() with a default, so this script can also be run unattended."""
    try:
        value = input(f'{prompt} [{default}]: ').strip()
    except (EOFError, OSError):
        value = ''
    return value or default


raw = ask('subject:name pairs', 'CS:Ada, Maths:Alan, CS:Grace, CS:Ada')

pairs = []
for chunk in raw.split(','):
    chunk = chunk.strip()
    if not chunk:
        continue
    # TODO 1: split on ':' and append a (subject, name) tuple
    subject, name = chunk.split(':')
    pairs.append((subject.strip(), name.strip()))
print(pairs)

counts, by_subject = {}, {}
for subject, name in pairs:
    # TODO 2: add one to this subject's count
    counts[subject] = counts.get(subject, 0) + 1
    # TODO 3: append the name to this subject's list
    by_subject.setdefault(subject, []).append(name)

# # TODO 4: a line per subject, sorted
for subject in sorted(counts):
    count = counts[subject]
    unique_names = set(by_subject[subject])
    print(f'{subject}: {count} entries, {len(unique_names)} unique names, '
          f'names: {sorted(unique_names)}')
# # TODO 5: the busiest subject
busiest = max(counts, key=counts.get)
print('busiest subject:', busiest)
# TODO 6: subjects sorted by count, highest first
for subject in sorted(counts, key=counts.get, reverse=True):
    print(subject, counts[subject])
