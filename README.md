# Lab 1: Grade Evaluator & Archiver
## Files
- `grade-evaluator.py` — reads a grades CSV and reports GPA, pass/fail status, and resubmission eligibility.
- `organizer.sh` — archives the current `grades.csv`, timestamps it, resets the workspace, and logs the action.
- `grades.csv` — sample grade data (assignment, group, score, weight).

## Requirements
- Python 3
- Bash (Linux/macOS, or WSL/Git Bash on Windows)

## Running `grade-evaluator.py`

```bash
python3 grade-evaluator.py
```

The script outputs:
- Formative and Summative subtotals and percentages
- Final Grade (out of 100) and GPA (out of 5.0)
- PASSED/FAILED status (requires ≥50% in **both** Formative and Summative)
- Any Formative assignment(s) eligible for resubmission (failed, highest weight among failures)

**CSV format:** `assignment,group,score,weight` where `group` is `Formative` or `Summative`. Weights must sum to 100 (60 Formative, 40 Summative).

## Running `organizer.sh`

```bash
chmod +x organizer.sh   # first time only
./organizer.sh
```

Archives `grades.csv` to `archive/grades_<YYYYMMDD-HHMMSS>.csv`, creates a fresh `grades.csv`, and logs the action to `organizer.log`.

## Typical workflow

```bash
python3 grade-evaluator.py   # evaluate the current grades.csv
./organizer.sh                # archive it and reset grades.csv for the next batch
```