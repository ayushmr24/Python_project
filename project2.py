#!/usr/bin/env python3
import csv

class student:
    def __init__(self, StudentID, Name, Math, Physics, Chemistry, Biology):
        self.id = StudentID
        self.name = Name
        self.m = int(Math)
        self.p = int(Physics)
        self.c = int(Chemistry)
        self.b = int(Biology)

    def avg(self):
        return (self.m + self.p + self.c + self.b) / 4


students = []

with open("grades.csv") as f:
    r = csv.reader(f)
    next(r)  # skip header
    for row in r:
        students.append(student(*row))


n = len(students)

math_avg = sum(s.m for s in students) / n
phy_avg  = sum(s.p for s in students) / n
chem_avg = sum(s.c for s in students) / n
bio_avg  = sum(s.b for s in students) / n

overall_avg = (math_avg + phy_avg + chem_avg + bio_avg) / 4

top3 = sorted(students, key=lambda s: s.avg(), reverse=True)[:3]

above90 = [s for s in students if max(s.m, s.p, s.c, s.b) > 90]


with open("report.txt", "w") as f:

    f.write(f"Total Students {n}\n\n")
    f.write("Subject Averages\n")
    f.write(f"Math: {math_avg:.2f}\n")
    f.write(f"Physics: {phy_avg:.2f}\n")
    f.write(f"Chemistry: {chem_avg:.2f}\n")
    f.write(f"Biology: {bio_avg:.2f}\n\n")

    f.write(f"Overall Class Average: {overall_avg:.2f}\n\n")

    f.write("Top 3 Students:\n")
    for s in top3:
        f.write(f"{s.id} {s.name} - {s.avg():.2f}\n")

    f.write("\nStudents scoring > 90 in any subject:\n")
    for s in above90:
        f.write(f"{s.id} {s.name}\n")

    f.write("\nHighest & Lowest Scores:\n")
    f.write(f"Math: {max(s.m for s in students)} / {min(s.m for s in students)}\n")
    f.write(f"Physics: {max(s.p for s in students)} / {min(s.p for s in students)}\n")
    f.write(f"Chemistry: {max(s.c for s in students)} / {min(s.c for s in students)}\n")
    f.write(f"Biology: {max(s.b for s in students)} / {min(s.b for s in students)}\n")

print("Report generated")

