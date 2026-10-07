"""Sample data files for the Compound Types lab.

COMP H2003 Artificial Intelligence, TU Dublin

Run this once before demo_6_file_formats.py or exercise_07_csv_shapes.py:

    python setup_data.py

It writes five files into the current folder holding the same four student
records: notes.txt, students.csv, students.json, students.xml, students.db.
The other scripts import write_sample_files() from here.
"""

import json
import sqlite3
from pathlib import Path

STUDENTS = [
    {'id': 1, 'name': 'Ada',    'subject': 'CS',    'mark': 72},
    {'id': 2, 'name': 'Alan',   'subject': 'Maths', 'mark': 91},
    {'id': 3, 'name': 'Grace',  'subject': 'CS',    'mark': 68},
    {'id': 4, 'name': 'Edsger', 'subject': 'CS',    'mark': 85},
]


def write_sample_files(folder='.'):
    """Write the five sample files into `folder` and return the folder path."""
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)

    # 1. plain text
    (folder / 'notes.txt').write_text(
        '# attendance notes - lines are name,subject,mark\n'
        + '\n'.join(f"{s['name']},{s['subject']},{s['mark']}" for s in STUDENTS)
        + '\n', encoding='utf-8')

    # 2. csv
    (folder / 'students.csv').write_text(
        'name,subject,mark\n'
        + '\n'.join(f"{s['name']},{s['subject']},{s['mark']}" for s in STUDENTS)
        + '\n', encoding='utf-8')

    # 3. json
    (folder / 'students.json').write_text(json.dumps(
        {'module': 'COMP H2003',
         'students': [{k: v for k, v in s.items() if k != 'id'} for s in STUDENTS]},
        indent=2), encoding='utf-8')

    # 4. xml
    rows = '\n'.join(
        f"  <student id=\"{s['id']}\">\n"
        f"    <name>{s['name']}</name>\n"
        f"    <subject>{s['subject']}</subject>\n"
        f"    <mark>{s['mark']}</mark>\n"
        f"  </student>" for s in STUDENTS)
    (folder / 'students.xml').write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<students>\n{rows}\n</students>\n',
        encoding='utf-8')

    # 5. sqlite
    db_path = folder / 'students.db'
    db_path.unlink(missing_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute('CREATE TABLE students '
                 '(id INTEGER PRIMARY KEY, name TEXT, subject TEXT, mark INTEGER)')
    conn.executemany('INSERT INTO students VALUES (:id, :name, :subject, :mark)',
                     STUDENTS)
    conn.commit()
    conn.close()

    return folder


if __name__ == '__main__':
    where = write_sample_files()
    written = sorted(p.name for p in where.glob('students.*'))
    print('wrote:', ', '.join(written), 'and notes.txt')
