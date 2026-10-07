"""Exercise 1 - marks into a list.

COMP H2003 Artificial Intelligence, TU Dublin

    python exercise_01_marks_list.py

1. Read a line of marks separated by commas.
2. Turn it into a list of integers, coping with the spaces.
3. Print the count, highest, lowest and mean.
4. Print the list sorted, then print the original and confirm it is unchanged.
5. Build a list of the passing marks (40 or over) and print the pass rate as a
   percentage.

Check yourself: after sorted(marks) the original must still be in input order.

Replace each ... with your own code. The script runs as it stands, but the
output will be nonsense until you do.
"""
from numpy.ma.extras import average


def ask(prompt, default):
    """input() with a default, so this script can also be run unattended."""
    try:
        value = input(f'{prompt} [{default}]: ').strip()
    except (EOFError, OSError):
        value = ''
    return value or default


raw = ask('Enter marks separated by commas', '72, 35, 68, 91, 55')

# TODO 1: split on commas, strip spaces, make ints
marks = [int(m.strip()) for m in raw.split(',')]
import statistics
print('as a list  :', marks)
print('count      :', len(marks))
print('highest    :', max(marks))
print('lowest     :', min(marks))
print('mean       :', statistics.mean(marks))

# TODO 2: a sorted COPY, then show the original
print('sorted     :', sorted(marks))
print('original   :', marks)

# TODO 3: the passing marks, and the rate
passed = [m for m in marks if m >= 40]
print('passed     :', passed)
print('pass rate  :', len(passed) / len(marks) * 100, '%')
