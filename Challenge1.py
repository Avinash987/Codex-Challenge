from datetime import date

import pandas
import io
import tempfile
import os
from pathlib import Path


def diff_days(csv_contents: str) -> int:
    with tempfile.TemporaryDirectory() as td:
        fname = Path(td)/'abc.csv'
        with fname.open('w') as f:
            f.write(csv_contents)

        data = pandas.read_csv(str(fname))
        earliest = min(data['Date'])
        latest = max(data['Date'])
    return (date.fromisoformat(latest) - date.fromisoformat(earliest)).days


# Examples
print(diff_days("Date,Price,Volume\n2014-01-27,550.50,1387\n2014-06-23,910.83,4361\n2014-05-20,604.51,5870"))
print(diff_days('Date\n2000-01-01\n2000-01-01\n'))

# The last expression evaluated is always shown when
# you run your code, just like a Jupyter notebook cell.
"Good luck!"