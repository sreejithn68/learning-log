"""Build the practice files for the Python sessions.

Run it once from your learning-log folder:
    python3 make_practice_data.py
It creates data/raw/ with deliberately messy files.
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
RAW = Path(__file__).parent / "data" / "raw"
SITES = ["LBA4", "MAN1", "BHX2", "EMA1", "LCY3", "DER1"]


def write_csv(path, header, rows, encoding="utf-8"):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding=encoding) as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def site_exports():
    """Topic 1: one file per site, with inconsistent names. EMA1 came from Excel."""
    folder = RAW / "site_exports"
    names = {
        "LBA4": "site_LBA4.csv",
        "MAN1": "site_MAN1.csv",
        "BHX2": "Site-BHX2.csv",
        "EMA1": "site_ema1_FINAL.csv",
        "LCY3": "site LCY3 (copy).csv",
        "DER1": "site_DER1.csv",
    }
    start = date(2026, 9, 7)
    for site, name in names.items():
        rows = []
        for d in range(random.randint(20, 35)):
            day = start + timedelta(days=d)
            for shift in ("Day", "Night"):
                planned = random.randint(80, 220)
                actual = planned + random.randint(-25, 15)
                rows.append([day.isoformat(), shift, planned, actual])
        encoding = "utf-8"
        if site == "EMA1":
            encoding = "utf-8-sig"
        write_csv(folder / name, ["date", "shift", "planned_heads", "actual_heads"], rows, encoding)
    (folder / "notes.txt").write_text("Exports pulled on Monday. EMA1 came from Excel.\n", encoding="utf-8")


def messy_forecast():
    """pandas: a weekly volume forecast with every common mess in it."""
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%d-%b-%Y", "%d.%m.%y"]
    start = date(2026, 10, 5)
    rows = []
    for site in SITES:
        for w in range(8):
            week = start + timedelta(weeks=w)
            volume = random.randint(40_000, 160_000)
            volume_text = str(volume)
            if random.random() < 0.3:
                volume_text = f"{volume:,}"
            site_text = site
            if random.random() < 0.25:
                site_text = site + " "
            if random.random() < 0.15:
                site_text = site_text.lower()
            comment = random.choice(["", "", "", "peak", "Peak "])
            rows.append([site_text, week.strftime(random.choice(formats)), volume_text, comment])
    rows.insert(10, ["", "", "", ""])
    rows.append(rows[3])
    rows.append(["MAN1", "2026-11-02", "n/a", ""])
    write_csv(RAW / "volume_forecast_messy.csv", ["site", "week_start", "volume", "comment"], rows)


def headcount():
    """pandas: plan and actual in separate files with different column names."""
    start = date(2026, 10, 5)
    plan = []
    actual = []
    for site in SITES:
        for w in range(8):
            week = (start + timedelta(weeks=w)).isoformat()
            planned = random.randint(300, 900)
            plan.append([site, week, planned])
            missing = site == "LCY3" and w == 7
            if not missing:
                actual.append([week, site, planned + random.randint(-90, 40)])
    write_csv(RAW / "headcount_plan.csv", ["site", "week_start", "planned_heads"], plan)
    write_csv(RAW / "headcount_actual.csv", ["Week", "Site Code", "Actual HC"], actual)


def wide_forecast():
    """pandas: one column per week, the shape spreadsheets love."""
    weeks = [date(2026, 11, 2) + timedelta(weeks=w) for w in range(6)]
    header = ["site"] + [f"wk_{d.isoformat()}" for d in weeks]
    rows = []
    for site in SITES:
        rows.append([site] + [random.randint(40_000, 160_000) for _ in weeks])
    write_csv(RAW / "forecast_wide.csv", header, rows)


def daily_volume():
    """Dates: a year of daily volume, plus a file that numbers weeks the US way."""
    start = date(2026, 1, 1)
    rows = []
    for d in range(365):
        day = start + timedelta(days=d)
        base = 100_000
        if day.month in (11, 12):
            base = 140_000
        if day.weekday() >= 5:
            base = base * 0.7
        rows.append([day.isoformat(), int(base * random.uniform(0.85, 1.15))])
    write_csv(RAW / "daily_volume_2026.csv", ["date", "volume"], rows)

    us_rows = []
    for d in range(0, 365, 7):
        day = start + timedelta(days=d)
        us_week = int(day.strftime("%U")) + 1
        us_rows.append([day.year, us_week, random.randint(500, 900)])
    write_csv(RAW / "labour_hours_by_week_US.csv", ["year", "week", "labour_hours"], us_rows)


def main():
    site_exports()
    messy_forecast()
    headcount()
    wide_forecast()
    daily_volume()
    for path in sorted(RAW.rglob("*")):
        if path.is_file():
            print(path.relative_to(RAW))
    print("Done. Practice data is in", RAW)


if __name__ == "__main__":
    main()