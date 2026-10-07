"""Exercise 5 - the same record, three ways.

COMP H2003 Artificial Intelligence, TU Dublin

    python exercise_05_record_three_ways.py

1. Read one record as name,subject,mark and convert the mark to an int.
2. Build it as a plain tuple, a namedtuple and a dataclass.
3. Print each, and reach the mark from each.
4. For the namedtuple print _fields, _asdict() and _replace(mark=mark+5), then
   confirm the original is unchanged.
5. Confirm the namedtuple still equals the plain tuple, then try assigning to
   the mark on the namedtuple and on the dataclass.

Replace each ... with your own code.
"""

from collections import namedtuple
from dataclasses import dataclass, asdict


def ask(prompt, default):
    """input() with a default, so this script can also be run unattended."""
    try:
        value = input(f'{prompt} [{default}]: ').strip()
    except (EOFError, OSError):
        value = ''
    return value or default


raw = ask('name,subject,mark', 'Ada,CS,72')
name, subject, mark_text = [p.strip() for p in raw.split(',')]
mark = int(mark_text)

as_tuple = (name, subject, mark)

# TODO 1: define Person with fields name subject mark
Person = namedtuple('Person',['name', 'subject', 'mark'])
as_named = Person(name,subject,mark)
print('namedtuple:', as_named, '->', as_named.mark)
print('  fields  :', as_named._fields)
print('  as dict :', as_named._asdict())
print('  bumped  :', as_named._replace(mark = mark+5))          # +5, as a NEW record
print('  original:', as_named)     # unchanged?
print('  == tuple:', as_named == as_tuple)

# TODO 2: a dataclass with the same three fields
@dataclass
class Person:
    name: str
    subject: str
    mark: int
stdnt_1 = Person(name,subject,mark)
print('dataclass :', stdnt_1, '->', stdnt_1.subject, ':', stdnt_1.mark)
print('  as dict  :', asdict(stdnt_1))
# TODO 3: try as_named.mark = 99 and as_dc.mark = 99
try:
    as_named.mark = 99
except AttributeError as e:
    print('namedtuple assignment error:', e)
stdnt_1.mark = 99
print('dataclass changed:', stdnt_1)
