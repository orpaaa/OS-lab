processes = [
    {"pid": "P1", "arrival": 0, "burst": 5},
    {"pid": "P2", "arrival": 1, "burst": 3},
    {"pid": "P3", "arrival": 2, "burst": 8},
    {"pid": "P4", "arrival": 3, "burst": 6},
    {"pid": "P5", "arrival": 4, "burst": 9}
]

processes.sort(key=lambda x: x["arrival"])

current_time = 0
total_waiting = 0
total_turnaround = 0

print("PID\tArrival\tBurst\tWaiting\tTurnaround")

for p in processes:
    if current_time < p["arrival"]:
        current_time = p["arrival"]
    p["waiting"] = current_time - p["arrival"]
    p["turnaround"] = p["waiting"] + p["burst"]

    current_time += p["burst"]
    total_waiting += p["waiting"]
    total_turnaround += p["turnaround"]

    print(f'{p["pid"]}\t{p["arrival"]}\t{p["burst"]}\t{p["waiting"]}\t{p["turnaround"]}')

avg_waiting = total_waiting / len(processes)
print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
