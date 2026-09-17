# Static Analysis

## Analysis Branch

All analysis-related changes are performed on the `static-analysis` branch.

The `main` branch remains unchanged and serves as the baseline for comparison.

## Tools

- Pylint
- Python

## Analysis Process

1. Preserve the original project on `main`.
2. Create the `static-analysis` branch.
3. Run static analysis on the original code.
4. Record the findings.
5. Identify issues that should be addressed.
6. Apply appropriate changes.
7. Run static analysis again.
8. Compare the results with the baseline.

## Pylint 

### Linux
```bash
pylint *.py
```
### Windows
```powershell
python -m pylint baccarat-cli.py baccarat-sim.py cards.py hands.py players.py rules.py
```

All test results are to be kept in the [`pylint/`](pylint/) directory

## Findings

**`docs/findings.md`** is where I'd put the **actual tables of problems**.

For example:

```markdown
# Static Analysis Findings

## Initial Findings

The following issues were identified during the initial static analysis of the project.

| ID | File | Line | Finding | Category | Status |
|----|------|------|---------|----------|--------|
| F001 | cards.py | 12 | Example finding | Code Quality | Fixed |
| F002 | players.py | 24 | Example finding | Maintainability | Fixed |
| F003 | rules.py | 41 | Example finding | Readability | Pending |

## Finding Details

### F001 — Example Finding

**File:** `cards.py`  
**Line:** 12  
**Category:** Code Quality

#### Description

Describe what the static analyzer reported and why it is considered an issue.

#### Original Code

```python
# original code