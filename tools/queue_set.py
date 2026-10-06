#!/usr/bin/env python3
"""Safely update job_queue.csv. Usage: queue_set.py <company> <status> [attempts] [note-to-append]
Writes to a temp file and replaces atomically. Rows are read with csv.reader (extra fields tolerated)."""
import csv, os, sys, tempfile
p = os.path.join(os.path.dirname(__file__), "..", "applications", "job_queue.csv")
company, status = sys.argv[1], sys.argv[2]
attempts = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] != '-' else None
note = sys.argv[4] if len(sys.argv) > 4 else None
rows = list(csv.reader(open(p, newline='')))
hit = 0
for r in rows[1:]:
    if len(r) >= 14 and r[1] == company:
        r[11] = status
        if attempts: r[12] = attempts
        if note: r[13] += ' | ' + note
        hit += 1
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p))
with os.fdopen(fd, 'w', newline='') as fh:
    csv.writer(fh).writerows(rows)
os.replace(tmp, p)
print(f'{hit} row(s) updated')
