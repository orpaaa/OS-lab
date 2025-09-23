import sys

processes = [
    {"pid": 1, "at": 0, "bt": 6, "ct": 0, "tat": 0, "wt": 0, "rem_bt": 6},
    {"pid": 2, "at": 1, "bt": 8, "ct": 0, "tat": 0, "wt": 0, "rem_bt": 8},
    {"pid": 3, "at": 2, "bt": 7, "ct": 0, "tat": 0, "wt": 0, "rem_bt": 7},
    {"pid": 4, "at": 3, "bt": 3, "ct": 0, "tat": 0, "wt": 0, "rem_bt": 3},
]

n = len(processes)
t = 0
completed = 0
avg_tat = 0
avg_wt = 0

while completed < n:
    idx = -1
    min_bt = sys.maxsize

    for i in range(n):
        if processes[i]["at"] <= t and processes[i]["rem_bt"] > 0:
            if processes[i]["rem_bt"] < min_bt:
                min_bt = processes[i]["rem_bt"]
                idx = i

    if idx != -1:
        processes[idx]["rem_bt"] -= 1
        t += 1

        if processes[idx]["rem_bt"] == 0:
            processes[idx]["ct"] = t
            processes[idx]["tat"] = processes[idx]["ct"] - processes[idx]["at"]
            processes[idx]["wt"] = processes[idx]["tat"] - processes[idx]["bt"]
            avg_tat += processes[idx]["tat"]
            avg_wt += processes[idx]["wt"]
            completed += 1
    else:
        t += 1 

print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    print(f"P{p['pid']}\t{p['at']}\t{p['bt']}\t{p['ct']}\t{p['tat']}\t{p['wt']}")

print(f"\nAverage TAT = {avg_tat/n:.2f}")
print(f"Average WT = {avg_wt/n:.2f}")
