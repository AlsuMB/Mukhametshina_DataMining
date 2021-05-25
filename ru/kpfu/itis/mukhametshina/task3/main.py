import csv
import random

seq = dict()
count = 0
with open('generated.csv') as File:
    reader = csv.reader(File, delimiter=';')
    for row in reader:
        count += 1
        if row[0] in seq.keys():
            seq[row[0]] = seq[row[0]] + 1
        else:
            seq[row[0]] = 1


def zero_moment(seq):
    return len(seq)


def first_moment(seq):
    f1 = 0
    for v in seq.values():
        f1 = + v
    return f1


def AMSestimate(seq, counter, num_samples=100):
    inds = list(range(len(seq)))
    random.shuffle(inds)
    inds = sorted(inds[: num_samples])

    d = {}

    for i, c in enumerate(seq):
        if i in inds and c not in d:
            d[c] = 0
        if c in d:
            d[c] += 1

    sum_ = 0
    for v in d.values():
        sum_ += counter * (2 * v - 1)
    return sum_ / num_samples


print(zero_moment(seq))
print(first_moment(seq))
print(AMSestimate(seq, count, num_samples=100))
print(AMSestimate(seq, count, num_samples=500))
