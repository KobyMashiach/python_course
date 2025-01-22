arr = [[32, 15], [1, 7, 12], [8, 14, 6, 11]]
max_total = 0

for p in arr:
    total = sum(p)
    if total > max_total:
        max_total = total

print(max_total)
