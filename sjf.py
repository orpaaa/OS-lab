processes = [
    { "pid": "P1", "arrival": 0, "burst": 5 },
    { "pid": "P2", "arrival": 1, "burst": 3 },
    { "pid": "P3", "arrival": 2, "burst": 1 },
    { "pid": "P4", "arrival": 3, "burst": 2 }
]

processes.sort(key=lambda p: p["arrival"])

done = []
current_time = 0
total_waiting = 0
total_turnaround = 0

print("PID\tArrival\tBurst\tWaiting\tTurnaround")

while len(done) < len(processes):
    available = [p for p in processes if p["arrival"] <= current_time and p not in done]

    if not available:
        current_time += 1
        continue

    shortest = min(available, key=lambda p: p["burst"])

    shortest["waiting"] = current_time - shortest["arrival"]
    shortest["turnaround"] = shortest["waiting"] + shortest["burst"]

    total_waiting += shortest["waiting"]
    total_turnaround += shortest["turnaround"]

    current_time += shortest["burst"]
    done.append(shortest)

    print(f'{shortest["pid"]}\t{shortest["arrival"]}\t{shortest["burst"]}\t{shortest["waiting"]}\t{shortest["turnaround"]}')

avgWT = total_waiting / len(processes)
print(f"\nAverage Waiting Time: {avgWT:.2f}")
