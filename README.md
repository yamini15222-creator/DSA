# Days 1–40 DSA Revision

This project contains six checkpoint problems from the Days 1–40 DSA consolidation assignment.

## Problems

1. Two Sum — hashmap stores previously seen values and their indexes.
2. Longest Unique Substring — sliding window shrinks when a repeated character is found.
3. Subarray Sum Equals K — prefix-sum frequency map counts earlier prefix sums.
4. Search Insert Position — binary search maintains a valid search interval.
5. Subsets — backtracking chooses, explores, and undoes choices.
6. Balanced Binary Tree — helper returns subtree height, or `-1` when unbalanced.

## Requirements

- Python 3.10 or newer
- `pytest` for running tests

## Run the examples

```bash
python main.py
```

## Run the tests

```bash
python -m pip install pytest
python -m pytest -v
```

## Suggested workflow for each problem

1. Write the input/output contract.
2. Dry-run a small example.
3. Implement without copying.
4. Test normal, boundary, and tricky cases.
5. Explain time and auxiliary-space complexity.
6. Record mistakes and their causes in `REVISION_NOTES.md`.

## GitHub

See `GITHUB_STEPS.md` for commands to create a Git repository and push it to GitHub.
