import difflib
from typing import Tuple
from collections import Counter


def diff_files(source: str, target: str) -> Tuple[int, int]:
    if source and not source.endswith('\n'):
        source = source + '\n'
    if target and not target.endswith('\n'):
        target = target + '\n'
    diff = difflib.unified_diff(source.splitlines(keepends=True), target.splitlines(keepends=True), n=10)
    diff = list(diff)
    diff = [d[0] for d in diff[3:]]
    cts = Counter(diff)
    return cts['+'], cts['-']
    

# Examples
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana\nMango'))
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana'))
print(diff_files('0', ''))