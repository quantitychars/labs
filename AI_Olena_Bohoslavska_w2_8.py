"""Exercise 8 - a round trip that does not round trip.

COMP H2003 Artificial Intelligence, TU Dublin

    python exercise_08_json_round_trip.py

1. Build a dict with INTEGER keys whose values are TUPLES; print the types of a
   key and a value.
2. Write it to trip.json with indent=2, then print the file's raw text.
3. Read it back and print the same two types again.
4. Test equality with the original, then try to reach the entry with the
   original integer key and catch the error.
5. Try to serialise a set and print the error. Then repair the loaded structure
   so that it equals the original again.

Replace each ... with your own code.
"""

import json

original = {1: ('Ada', 'CS'), 2: ('Alan', 'Maths')}
print('key type  :', type(list(original)[0]).__name__)
print('value type:', type(original[1]).__name__)

# TODO 1: write it to trip.json with indent=2
with open('trip.json', 'w', encoding ='utf-8') as f:
    json.dump(original, f, indent=2)
# TODO 2: print the raw file text
with open('trip.json', 'r', encoding ='utf-8') as f:
    raw_text = f.read()
# TODO 3: read it back into `back`
with open('trip.json', 'r', encoding ='utf-8') as f:
    back =  json.load(f)
print('key type  :', type(list(back)[0]).__name__)
print('value type:', type(back['1']).__name__)
print('equal?    :', back == original)

# TODO 4: reach back[1] and catch the error
try:
    print(back[1])
except KeyError as e:
    print('KeyError:', e)
# TODO 5: try json.dumps on a set, catch the error
try:
    json.dumps({1,2,3})
except TypeError as e:
    print('TypeError:', e)
# TODO 6: repair - rebuild int keys and tuple values
repaired = {int(key): tuple(value) for key, value in back.items()}
print(repaired == original)
