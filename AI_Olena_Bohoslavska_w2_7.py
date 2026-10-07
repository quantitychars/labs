"""Exercise 7 - a CSV into both shapes.

COMP H2003 Artificial Intelligence, TU Dublin

    python exercise_07_csv_shapes.py

1. Read students.csv with csv.DictReader into a list of dicts.
2. Print the row count, the first record, and the TYPE of its mark field.
3. Convert the mark column to integers once, up front.
4. Turn the row shape into the column shape, then print the mean mark from the
   column.
5. Group the marks by subject and print, per subject, how many students and the
   mean to one decimal place.

Check yourself: if step 2 prints int, you are not reading the file.

setup_data.py must sit in the same folder; it writes students.csv for you.
Replace each ... with your own code.
"""

import csv

from setup_data import write_sample_files

write_sample_files()

path = '../students.csv'

# TODO 1: read into a list of dicts
with open(path, newline='', encoding='utf-8') as f:
    records = list(csv.DictReader(f))

print('rows      :', len(records))
print('first row :', records[0])
print('mark type :', type(records[0]['mark']).__name__)

# TODO 2: convert every mark to int, in place
for r in records:
    r['mark'] = int(r['mark'])
print('converted mark type :', type(records[0]['mark']).__name__)

# TODO 3: row shape -> column shape
columns = {'name':[r['name'] for r in records],
           'subject':[r['subject'] for r in records],
           'mark':[r['mark'] for r in records]}
print('mean mark :', sum(columns['mark'])/len(columns['mark']))

# TODO 4: group marks by subject and print a line each
by_subject = {}
for r in records:
    subject = r['subject']
    mark = r['mark']
    if subject not in by_subject:
        by_subject[subject] = []
    by_subject[subject].append(mark)

for subject, marks in by_subject.items():
    mean = sum(marks)/len(marks)
    print(f"{subject}: {len(marks)} students, mean mark {mean:.1f}")
