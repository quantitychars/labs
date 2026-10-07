"""Exercise 2 - records, unpacking and slicing.

COMP H2003 Artificial Intelligence, TU Dublin

    python exercise_02_records_tuples.py

1. Read one record as name,subject,mark.
2. Split it into a tuple, stripping spaces; print the tuple, its type and its
   length.
3. Unpack it into three names, convert the mark to an int, print a sentence.
4. Use (name, subject) as a dictionary key. Then try the same with a list and
   print the error.
5. Slice the record, then try to assign to record[0] and print that error too.

Replace each ... with your own code.
"""


def ask(prompt, default):
    """input() with a default, so this script can also be run unattended."""
    try:
        value = input(f'{prompt} [{default}]: ').strip()
    except (EOFError, OSError):
        value = ''
    return value or default


raw = ask('name,subject,mark', 'Ada,CS,72')

# TODO 1: split, strip, make a tuple
record = tuple(item.strip() for item in raw.split(','))
print('record :', record)
print('type   :', type(record).__name__)

# TODO 2: unpack into three names, mark -> int
name, subject, mark_text = record
mark = int(mark_text)
print(f'{name} scored {mark} in {subject}')

# TODO 3: tuple as a dict key, then a list as a key
results = {record[:2]: mark}
print('as a key:', results)
try:
    {[name, subject]: mark}
except TypeError as e:
    print('list as key ->', e)

# TODO 4: slice it, then try to assign to record[0]
sliced = record[0:]
print('sliced :', sliced)
try:
    record[0] = 'Bob'
except TypeError as e:
    print('assign to record[0] ->', e)