"""S3: print file name, size in KB and row count for every CSV in site_exports."""
import csv
from pathlib import Path

FOLDER = Path.home() / "Documents" / "learning-log" / "data" / "raw" / "site_exports"

# TODO 1: make a sorted list of every .csv file in FOLDER.
# Hint: FOLDER.glob("*.csv") finds them; sorted(...) puts them in order.
csv_files = sorted(FOLDER.glob("*.csv"))

# TODO 2: loop over that list with a for loop. For each file:
#   - size in KB: path.stat().st_size / 1024, rounded to 1 decimal place with round(..., 1)
#   - row count: open the file with encoding="utf-8-sig" and newline="",
#     read it with csv.DictReader, and count the rows
#   - print the name, size and row count on one line    

for file in csv_files:
    count = 0
    size_kb = round(file.stat().st_size / 1024, 1)
    with open(file, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            count +=1
    print(file.name, size_kb, "KB",  count, "rows")


    
        
            
    