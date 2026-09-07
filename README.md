# Learning Log — Python & Problem Solving

A structured, public record of me learning programming properly — not tutorial-following, but building the ability to solve problems unaided.

**Foundation language:** Python
**Cadence:** 4 sessions/week · 45 minutes each · timer on
**Rule:** every session ends with at least one commit. No commit = the session didn't happen.

---

## Why this exists

I can follow tutorials but struggle to build things on my own. That gap closes one way only: reps on problems I haven't seen the answer to. This repo is the paper trail of closing it.

**What I'm building toward:** writing practical scripts without help — reading messy files, reshaping data, calling APIs, failing gracefully, and pairing Python with SQL.

---

## How it's structured

```
learning-log/
├── README.md              ← you are here (the plan + rules)
├── PROGRESS.md            ← running log, one line per session
├── notes/                 ← theory notes per topic — the reference library
├── scripts/               ← the real work, one folder per topic
│   ├── 01_files/
│   ├── 02_pandas/
│   ├── 03_dates/
│   ├── 04_structure/
│   ├── 05_apis/
│   ├── 06_robustness/
│   └── 07_sql/
├── data/
│   ├── raw/               ← inputs, deliberately messy
│   └── output/            ← gitignored
├── python-basics/         ← early foundational exercises
│   └── week1/
└── leetcode/              ← fluency drills, one file per problem
```

Exercises carry built-in tests. Run the file; ✅ means solved, a red error means keep going.

---

## The path — 12 weeks, 48 sessions

| Sessions | Topic | What I'll be able to do |
|---|---|---|
| 1 | Setup | Repo, venv, workflow |
| 2–5 | **Files & Paths** | Find, open, merge and rename files across a folder tree |
| 6–16 | **pandas** | Clean messy data, group, merge, pivot, write formatted Excel |
| 17–20 | **Dates & Time** | Parse any date format, build calendars, resample to weekly |
| 21–25 | **Structuring a Script** | Turn a one-off script into a tool someone else can run |
| 26–30 | **APIs & JSON** | Pull from an API, flatten nested JSON, handle pagination |
| 31–35 | **Making It Not Break** | Validate input, handle errors specifically, log properly |
| 36–42 | **Python + SQL** | Query from Python, write results back, split work correctly |
| 43–46 | **Capstone** | One script that uses all of it, end to end |
| 47–48 | Buffer | Catch-up, or revisit whatever hurt most |

**The target:** hand me a small unfamiliar problem and I build a working solution without a tutorial.

### Session shape

**Theory session** (first of each topic) — 25 min reading the note, 20 min typing out the examples and breaking them deliberately.

**Build session** (all the rest) — 5 min writing the approach, 35 min attempting it cold, 5 min committing and logging.

### LeetCode

Two Easy problems a week, side channel only. Arrays, strings, hash tables — for fluency with loops, dicts and comprehensions, not for algorithms. Trees, graphs and DP are skipped deliberately: interview furniture, irrelevant to writing scripts.

---

## Rules that keep this alive

1. **45 minutes, timer on.** When it rings, commit whatever I have and stop.
2. **Write the approach before the code.** Even one sentence.
3. **Struggle 20 minutes before looking anything up.** The struggle is the training.
4. **Never read the solution before attempting.** Reading working code feels like learning and isn't.
5. **Four sessions a week is the floor, not the target.** Extra is welcome, never required.
6. **The tracker only goes on my website after a 3-week streak.**

See [PROGRESS.md](./PROGRESS.md) for the running log.
