"""Exercise 3 - two lists, four questions.

COMP H2003 Artificial Intelligence, TU Dublin

    python exercise_03_attendance_sets.py

1. Read two comma-separated attendance lists, one per week. Duplicates are
   allowed.
2. Print how many entries and how many unique names each week had.
3. Print who attended both weeks, week 1 only, week 2 only, and either week.
4. Print who attended exactly one of the two weeks, using a single set operator.
5. Print anyone who signed in twice in week 1, then week 1 deduplicated with
   order kept.

Check yourself: wrap every set in sorted() before printing, or your output
order is not reproducible.

Replace each ... with your own code.
"""


def ask(prompt, default):
    """input() with a default, so this script can also be run unattended."""
    try:
        value = input(f'{prompt} [{default}]: ').strip()
    except (EOFError, OSError):
        value = ''
    return value or default


a_raw = ask('Week 1 attendance', 'Ada, Alan, Ada, Grace')
b_raw = ask('Week 2 attendance', 'Ada, Grace, Edsger')

week1 = [n.strip() for n in a_raw.split(',') if n.strip()]
week2 = [n.strip() for n in b_raw.split(',') if n.strip()]

# TODO 1: make sets from the two lists
s1, s2 = set(week1), set(week2)

print('week 1 entries:', len(week1), 'unique:', len(s1))
print('week 2 entries:', len(week2), 'unique:', len(s2))

# TODO 2: the four comparisons, each sorted
print('both weeks  :', sorted(s1 & s2))
print('week 1 only :', sorted(s1 - s2))
print('week 2 only :', sorted(s2 - s1))
print('either week :', sorted(s1 | s2))

# TODO 3: exactly one week, with ONE operator
print('exactly one :', sorted(s1 ^ s2))

# TODO 4: who signed twice, then dedupe keeping order
twice = [n for n in week1 if week1.count(n) > 1]

print('signed twice:', twice)