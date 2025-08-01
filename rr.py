def round_robin(pID, AT, BT, TQ):
    n = len(pID)
    remaining_time = BT.copy()
    complete = 0
    t = 0
    queue = []
    visited = [False] * n
    WT = [0] * n
    TAT = [0] * n

    while complete < n:
        for i in range(n):
            if AT[i] <= t and not visited[i]:
                queue.append(i)
                visited[i] = True

        if not queue:
            t += 1
            continue

        current = queue.pop(0)
        time_given = min(TQ, remaining_time[current])
        t += time_given
        remaining_time[current] -= time_given

        for i in range(n):
            if AT[i] <= t and not visited[i]:
                queue.append(i)
                visited[i] = True

        if remaining_time[current] > 0:
            queue.append(current)
        else:
            complete += 1
            TAT[current] = t - AT[current]
            WT[current] = TAT[current] - BT[current]

    print("PID\tAT\tBT\tWT\tTAT")
    for i in range(n):
        print(f"{pID[i]}\t{AT[i]}\t{BT[i]}\t{WT[i]}\t{TAT[i]}")

pID = ['P1', 'P2', 'P3', 'P4', 'P5']
AT = [0, 1, 2, 3, 4]
BT = [6, 8, 7, 3, 5]
TQ = 3

round_robin(pID, AT, BT, TQ)
