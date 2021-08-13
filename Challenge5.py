import itertools
from typing import List


def count_arrangements(sizes: List[int]) -> int:
    if len(sizes) < 2:
        return 0
    combinations = itertools.permutations(sizes)
    arrangements = list(
        filter(lambda bucket_combo: bucket_combo[0] > bucket_combo[1], combinations)
    )
    return len(arrangements)
# Examples
print(count_arrangements([1, 3, 1]))
print(count_arrangements([1, 2]))