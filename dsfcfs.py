def dsfcfs(requests, start_head):
    head = start_head
    total_movement = 0

   
    filtered_requests = [r for r in requests if r != start_head]

    for req in filtered_requests:
        total_movement += abs(req - head)
        head = req

    print("Total Seek Operations:", total_movement)



requests = [176, 39, 114, 90, 26]
start_head = 39

dsfcfs(requests, start_head)
