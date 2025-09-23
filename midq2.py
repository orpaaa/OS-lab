def sstf(requests, head):
    n = len(requests)
    visited = [False] * n
    total_seek = 0
    sequence = [head]

    for _ in range(n):
        idx = -1
        min_dist = float('inf')

        for i in range(n):
            if not visited[i]:
                dist = abs(head - requests[i])
                if dist < min_dist:
                    min_dist = dist
                    idx = i

        visited[idx] = True
        total_seek += abs(head - requests[idx])
        head = requests[idx]
        sequence.append(head)

    return sequence, total_seek

requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53

sequence, total_seek = sstf(requests, head)

print("Seek Sequence:", " -> ".join(map(str, sequence)))
print("Total Seek Operations =", total_seek)
