import csv
import random

with open("generated.csv", mode="w", newline='') as w_file:
    writer = csv.writer(w_file)
    for i in range(1000000):
        writer.writerow([random.randint(0, 1000)])